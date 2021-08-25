<template>
  <form @submit.prevent="">
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
        v-model="task.name"
        required
      />
    </div>
  </form>
</template>

<script>
import { onMounted, reactive } from "@vue/runtime-core";
import {
  createOneTask,
  getOneTask,
  updateOneTask,
} from "../../services/TaskApi.js";

export default {
  props: {
    taskId: { type: Number },
  },
  setup(props, { emit }) {
    const task = reactive({});

    const submit = (doUpdate) => {
      if (doUpdate) {
        updateOneTask(props.taskId, task).then((t) => emit("update", t));
      } else {
        createOneTask(task).then((t) => emit("create", t));
      }
    };

    onMounted(() => {
      if (props.taskId) {
        getOneTask(props.taskId).then((t) => Object.assign(task, t));
      }
    });

    return { task, submit };
  },
};
</script>

<style>
</style>