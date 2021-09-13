<template>
  <div class="w-full flex items-center justify-center">
    <section class="p-8 w-96 bg-white">
      <span v-if="errorMessage" class="text-red-400">{{ errorMessage }}</span>
      <LoginForm @submit="submit" />
    </section>
  </div>
</template>

<script>
import { ref } from "@vue/reactivity";
import LoginForm from "../components/LoginForm.vue";
import UserAuth from "../services/UserAuth";
import { router } from "../router";
import { getTaskStatusList } from "../services/TaskApi";
import UserStore from "../store/User";
import TaskStore from "../store/Task";

export default {
  components: { LoginForm },
  setup() {
    const errorMessage = ref("");

    const submit = (auth_data) => {
      UserAuth.login(auth_data).then((error) => {
        // display error if an error message is returned
        if (error) errorMessage.value = error;

        // first check whether the auth token was successfully stored
        if (UserStore.getters.authToken()) {
          // store the list of task statuses for the current user
          // as this is a resource that does not change very often
          getTaskStatusList().then((statusList) =>
            TaskStore.methods.setStatusList(statusList)
          );

          return router.push("/");
        }
      });
    };

    return { errorMessage, submit };
  },
};
</script>

<style>
</style>