<template>
  <form id="create-task">
    <div class="text-gray-700">
      <label class="block mb-1" for="form-taskname">Task Name</label>
      <input
        id="form-taskname"
        class="
          w-full
          h-10
          px-3
          text-base
          placeholder-gray-600
          border
          rounded-md
          focus:shadow-outline
        "
        type="text"
        v-model="form.name"
        required
      />
    </div>
    <button
      class="
        my-2
        px-4
        py-2
        bg-green-400
        text-white
        rounded-md
        hover:bg-green-500
      "
      @click.prevent="createTask"
    >
      Add
    </button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  props: {
    parentId: { type: Number, default: 0 },
  },
  data() {
    return {
      errors: [],
      form: {
        name: null,
        complete: false,
        parent_id: this.parentId,
      },
    };
  },
  methods: {
    createTask() {
      axios
        .post("/api/task", this.form)
        .then((res) => this.$emit("create"))
        .catch((error) => console.log(error));
    },
  },
};
</script>