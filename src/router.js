import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import DailyPage from "./pages/DailyPage.vue";
import TaskPage from "./pages/TaskPage.vue";
import SettingsPage from "./pages/SettingsPage.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: LoginPage },
  { path: "/daily/:id?", component: DailyPage },
  { path: "/task/:id?", component: TaskPage },
  { path: "/settings", component: SettingsPage },
];

export const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});
