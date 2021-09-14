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

class PlannerApi {
  getToday() {
    return axios
      .get("/api/planner/today")
      .then((resp) => resp.data)
      .then((data) => {
        return data;
      })
      .catch((error) => {
        Promise.reject(error);
      });
  }

  getEntry(entryId) {
    return axios
      .get(`/api/planner/${entryId}`)
      .then((resp) => resp.data)
      .then((data) => {
        return data;
      })
      .catch((error) => {
        Promise.reject(error);
      });
  }
}

export default new PlannerApi();
