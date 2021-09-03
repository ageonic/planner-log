<template>
  <form @submit.prevent="submit">
    <div class="my-4">
      <TextInput
        label="username"
        name="username"
        :required="true"
        v-model="username"
      />
    </div>
    <div class="my-4">
      <TextInput
        label="password"
        name="password"
        type="password"
        :required="true"
        v-model="password"
      />
    </div>
    <div class="my-4 w-full text-center">
      <button
        type="submit"
        class="py-2 w-full rounded bg-indigo-500 text-white hover:bg-indigo-600"
      >
        Login
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from "@vue/reactivity";
import TextInput from "./ui/inputs/TextInput.vue";

export default {
  components: { TextInput },
  emits: ["submit"],
  setup(props, { emit }) {
    const username = ref("");
    const password = ref("");

    const submit = () => {
      emit("submit", { username: username.value, password: password.value });
    };

    return { username, password, submit };
  },
};
</script>

<style>
</style>