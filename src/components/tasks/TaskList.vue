<template>
  <div v-for="task in tasks" :key="task.id" class="my-2">
    <TaskListItem
      :taskId="task.id"
      :name="task.name"
      :status="task.status.label"
      :color="task.status.color"
      :clockRunning="task.has_running_clock"
      :clockSeconds="task.running_clock_time"
      @select="handleClick(task.id)"
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