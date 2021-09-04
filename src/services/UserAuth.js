import axios from "axios";
import UserStore from "../store/User";

class UserAuth {
  login(auth_data) {
    axios
      .post(
        "/api/auth/login",
        {},
        {
          auth: auth_data,
        }
      )
      .then((resp) => resp.data)
      .then((data) => {
        UserStore.methods.setAuthToken(data.token);
      })
      .catch((e) => {
        console.log(e.response.data.message);
      });
  }

  logout() {
    UserStore.methods.removeAuthToken();
  }
}

export default new UserAuth();
