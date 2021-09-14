<template>
  <TaskList :tasks="tasks"></TaskList>
</template>

<script>
import { onBeforeMount, reactive, watch } from "@vue/runtime-core";
import { useRoute } from "vue-router";
import PlannerApi from "../services/PlannerApi";
import TaskList from "../components/tasks/TaskList.vue";

export default {
  components: { TaskList },
  setup() {
    const route = useRoute();
    const tasks = reactive([]);

    const setTasks = (data) => {
      // clear the reactive array of tasks
      tasks.splice(0);

      // extract task details from the list of task entries (if they exist)
      if (data.task_entries)
        tasks.push(...data.task_entries.map((entry) => entry.task));
    };

    const refreshTasks = () => {
      if (route.params.id) {
        PlannerApi.getEntry(route.params.id).then((data) => setTasks(data));
      } else {
        PlannerApi.getToday().then((data) => setTasks(data));
      }
    };

    onBeforeMount(() => refreshTasks());
    watch(route, () => refreshTasks());

    return { tasks };
  },
};
</script>

<style>
</style>