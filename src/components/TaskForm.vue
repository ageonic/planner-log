<template>
  <section v-if="mode === 'view'">
    <h1 class="text-xl font-extrabold">{{ form.name }}</h1>
  </section>
  <form v-if="mode === 'create' || mode === 'edit'" id="create-task">
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
      v-if="mode === 'create'"
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
    <button
      v-if="mode === 'edit'"
      class="
        my-2
        px-4
        py-2
        bg-green-400
        text-white
        rounded-md
        hover:bg-green-500
      "
      @click.prevent="updateTask"
    >
      Save
    </button>
  </form>
</template>

<script>
import axios from "axios";
import { onBeforeMount, reactive } from "vue";

export default {
  props: {
    taskId: { type: Number },
    mode: {
      validator(value) {
        return ["create", "view", "edit"].includes(value);
      },
      required: true,
    },
  },
  setup(props, { emit }) {
    const form = reactive({
      id: null,
      name: null,
      complete: false,
      parent_id: null,
    });

    const createTask = () => {
      axios
        .post("/api/task", form)
        .then((res) => emit("create"))
        .catch((error) => console.log(error.message));
    };

    const getTask = () => {
      if (!props.taskId) {
        console.error("no task id specified");
        return;
      }

      axios
        .get(`/api/task/${props.taskId}`)
        .then((res) => {
          for (let key of Object.keys(form)) {
            form[key] = res.data[key];
          }
        })
        .catch((error) => console.log(error.message));
    };

    const updateTask = () => {
      if (!props.taskId) {
        console.error("no task id specified");
        return;
      }

      axios
        .put(`/api/task/${props.taskId}`, form)
        .then((res) => emit("update"))
        .catch((error) => console.log(error.message));
    };

    onBeforeMount(() => {
      // prefill existing task information if in view or edit mode
      if (props.mode === "view" || props.mode === "edit") getTask();
    });

    return {
      form,
      createTask,
      getTask,
      updateTask,
    };
  },
};
</script>