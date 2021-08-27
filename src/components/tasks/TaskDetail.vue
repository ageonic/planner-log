<template>
  <article class="h-auto w-full shadow-lg bg-white rounded-md flex flex-col">
    <section
      name="header"
      class="border-b-2 border-gray-100 flex items-center px-8 py-6"
    >
      <div class="flex flex-grow items-center">
        <div class="mr-2"><StatusIndicator color="#7896FF" /></div>
        <div class="flex-grow capitalize text-gray-300">task status</div>
      </div>
    </section>
    <section name="details" class="p-8">
      <h1 class="text-2xl">{{ task.name }}</h1>
      <p class="mt-6 tracking-wider leading-6">
        Candy chocolate cake toffee powder ice cream cheesecake. Candy canes
        cake jujubes dragée jujubes croissant lemon drops. Bear claw jelly-o
        jelly-o donut dragée candy candy canes jujubes chupa chups. Jelly halvah
        candy canes marshmallow tart.
      </p>
    </section>
    <section
      name="subtasks"
      class="p-8 bg-gray-50 border-t-2 border-b-2 border-gray-100"
    >
      <h2>Subtasks for {{ task.name }}</h2>
    </section>
    <section name="footer" class="p-8"></section>
  </article>
</template>

<script>
import { onMounted, reactive } from "@vue/runtime-core";
import { getOneTask } from "../../services/TaskApi.js";
import StatusIndicator from "../ui/StatusIndicator.vue";

export default {
  components: { StatusIndicator },
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