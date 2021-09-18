<template>
  <div class="flex flex-col h-screen">
    <div class="flex flex-1 overflow-hidden">
      <aside v-if="user.getters.authToken()" class="flex w-64">
        <TheSidenav />
      </aside>
      <main class="flex flex-1 flex-col shadow-lg">
        <div class="flex-1 overflow-y-auto p-8">
          <router-view />
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { inject } from "@vue/runtime-core";
import { router } from "./router";

import TheSidenav from "./components/TheSidenav.vue";

export default {
  components: { TheSidenav },
  setup() {
    const user = inject("user");

    // redirect the user to the login page if the auth token is not set
    if (!user.getters.authToken()) router.push("/login");

    return { user };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
