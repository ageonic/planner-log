<template>
  <div class="w-full flex items-center justify-center">
    <section class="p-8 w-96 bg-white">
      <LoginForm @submit="submit" />
    </section>
  </div>
</template>

<script>
import LoginForm from "../components/LoginForm.vue";
import UserAuth from "../services/UserAuth";
import { router } from "../router";
import { getTaskStatusList } from "../services/TaskApi";
import UserStore from "../store/User";
import TaskStore from "../store/Task";

export default {
  components: { LoginForm },
  setup() {
    const submit = (auth_data) => {
      UserAuth.login(auth_data).then(() => {
        // first check whether the auth token was successfully stored
        if (UserStore.getters.authToken())
          // store the list of task statuses for the current user
          // as this is a resource that does not change very often
          getTaskStatusList().then((statusList) =>
            TaskStore.methods.setStatusList(statusList)
          );

        router.push("/");
      });
    };

    return { submit };
  },
};
</script>

<style>
</style>