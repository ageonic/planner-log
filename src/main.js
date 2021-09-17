import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";

import { router } from "./router";
import UserStore from "./store/User";

const app = createApp(App);

app.config.globalProperties.$log = console.log;

app.use(router);
app.provide("user", UserStore);
app.mount("#app");
