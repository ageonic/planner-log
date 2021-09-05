import { reactive } from "vue";

const state = reactive({
  _authToken: null,
});

const getters = {
  authToken() {
    return state._authToken;
  },
  authTokenDecoded() {
    try {
      return atob(state._authToken.split(".")[1]);
    } catch (error) {
      console.log(error.message);
    }
  },
};

const methods = {
  setAuthToken(token) {
    state._authToken = token;
  },
  removeAuthToken() {
    state._authToken = null;
  },
};

export default {
  getters,
  methods,
};
