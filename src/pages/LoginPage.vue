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

export default {
  components: { LoginForm },
  setup() {
    const submit = (auth_data) => {
      UserAuth.login(auth_data).then(() => router.push("/"));
    };

    return { submit };
  },
};
</script>

<style>
</style>