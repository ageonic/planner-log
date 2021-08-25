<template>
  <h2>{{ task.name }}</h2>
</template>

<script>
import { onMounted, reactive } from "@vue/runtime-core";
import { getOneTask } from "../../services/TaskApi.js";

export default {
  props: {
    taskId: { type: Number, required: true },
  },
  setup(props) {
    const task = reactive({});

    onMounted(() => {
      getOneTask(props.taskId).then((t) => {
        Object.assign(task, t);
      });
    });

    return { task };
  },
};
</script>

<style>
</style>