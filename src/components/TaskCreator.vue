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
        v-model="name"
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
    id: { type: Number },
    name: { type: String },
    complete: { type: Boolean },
    parentId: { type: Number, default: 0 },
    mode: {
      validator(value) {
        return ["create"].includes(value);
      },
      required: true,
    },
  },
  setup(props, { emit }) {
    const createTask = () => {
      axios
        .post("/api/task", {
          name: props.name,
          complete: props.complete,
          parent_id: props.parent_id,
        })
        .then((res) => emit("create"))
        .catch((error) => console.log(error));
    };

    return {
      createTask,
    };
  },
};
</script>