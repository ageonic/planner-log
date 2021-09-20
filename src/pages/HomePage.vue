<template>
  <button v-if="!showEditor" @click="showEditor = true">New</button>
  <TaskEditor
    v-if="showEditor"
    @create="
      refreshTasks();
      showEditor = false;
    "
    @cancel="showEditor = false"
  />
  <TaskList :tasks="tasks" @select="router.push(`/task/${$event}`)"></TaskList>
</template>

<script>
import { reactive, onMounted, ref } from "vue";
import { getFilteredTasks } from "../services/TaskApi";
import TaskEditor from "../components/tasks/TaskEditor.vue";
import TaskList from "../components/tasks/TaskList.vue";
import { router } from "../router";

export default {
  components: { TaskEditor, TaskList },
  setup() {
    const tasks = reactive([]);
    const showEditor = ref(false);

    const refreshTasks = () => {
      tasks.splice(0);
      getFilteredTasks({ parent_id: 0 }).then((data) => {
        if (data) tasks.push(...data);
      });
    };

    onMounted(() => {
      refreshTasks();
    });

    return {
      router,
      tasks,
      showEditor,
      refreshTasks,
    };
  },
};
</script>

<style>
</style>