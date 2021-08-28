import axios from "axios";

export function createOneTask(taskData) {
  return axios
    .post("/api/task", taskData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.message));
}

export function getOneTask(taskId) {
  if (!taskId) {
    console.error("no task id specified");
    return;
  }

  return axios
    .get(`/api/task/${taskId}`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.message));
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
    .catch((error) => console.error(error.message));
}

export function deleteOneTask(taskId) {
  if (!taskId) {
    console.error("no task id specified");
    return;
  }

  return axios
    .delete(`/api/task/${taskId}`)
    .catch((error) => console.error(error.message));
}

export function getAllTasks() {
  return axios
    .get("/api/task")
    .then((response) => {
      return response.data;
    })
    .catch((error) => console.error(error.message));
}
