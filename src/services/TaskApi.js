import axios from "axios";
import UserStore from "../store/User";

axios.interceptors.request.use(
  (config) => {
    const token = UserStore.getters.authToken();
    if (token) {
      config.headers["Authorization"] = "Bearer " + token;
    }
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

export function getTaskStatusList() {
  return axios
    .get("/api/task/status")
    .then((response) => response.data)
    .then((data) => {
      return data;
    })
    .catch((error) => console.error(error.response.data.message));
}

export function createOneTask(taskData) {
  return axios
    .post("/api/task", taskData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.response.data.message));
}

export function getOneTask(taskId) {
  if (!taskId) {
    console.error("no task id specified");
    return;
  }

  return axios
    .get(`/api/task/tree/${taskId}`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.log(error.response.data.message));
}

export function updateOneTask(taskId, taskData) {
  if (!taskId) {
    console.error("no task id specified");
    return;
  }

  return axios
    .put(`/api/task/${taskId}`, taskData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.response.data.message));
}

export function deleteOneTask(taskId) {
  if (!taskId) {
    console.error("no task id specified");
    return;
  }

  return axios
    .delete(`/api/task/${taskId}`)
    .catch((error) => console.error(error.response.data.message));
}

export function getFilteredTasks(params) {
  return axios
    .get("/api/task", { params: params })
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.response.data.message));
}

export function getAllTasks() {
  return axios
    .get("/api/task")
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.response.data.message));
}
