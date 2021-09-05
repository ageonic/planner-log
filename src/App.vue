<template>
  <div class="container mx-auto">
    <router-view />
  </div>
</template>

<script>
import { inject } from "@vue/runtime-core";
import { router } from "./router";

export default {
  setup() {
    const user = inject("user");

    // redirect the user to the login page if the auth token is not set
    if (!user.getters.authToken()) router.push("/login");
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
