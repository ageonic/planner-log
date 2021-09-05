<template>
  <div
    v-for="task in tasks"
    :key="task.id"
    class="
      my-2
      cursor-pointer
      focus:outline-none
      focus:ring-2 focus:ring-indigo-200
    "
    role="button"
    tabindex="0"
    @click="handleClick(task.id)"
    @keyup.enter="handleClick(task.id)"
  >
    <TaskListItem
      :taskId="task.id"
      :name="task.name"
      :status="task.status.label"
      :color="task.status.color"
    />
  </div>
</template>

<script>
import TaskListItem from "./TaskListItem.vue";

export default {
  components: { TaskListItem },
  props: {
    tasks: { type: Array, default: [] },
  },
  emits: ["select"],
  setup(props, { emit }) {
    const handleClick = (targetId) => {
      emit("select", targetId);
    };

    return { handleClick };
  },
};
</script>

<style>
</style>