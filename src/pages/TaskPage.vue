<template>
  <TaskDetail
    :taskId="parseInt(route.params.id)"
    @subtask-select="router.push(`/task/${$event}`)"
    @delete="router.push('/')"
  />
</template>

<script>
import TaskDetail from "../components/tasks/TaskDetail.vue";
import { useRoute } from "vue-router";
import { router } from "../router";

export default {
  components: { TaskDetail },
  setup() {
    const route = useRoute();

    return { route, router };
  },
};
</script>

<style>
</style>