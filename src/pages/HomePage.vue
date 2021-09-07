<template>
  <button
    class="my-2 p-2 bg-indigo-400 text-white rounded-md"
    v-if="showDetail"
    @click="
      showDetail = false;
      refreshTasks();
    "
  >
    Back
  </button>
  <TaskDetail
    v-if="currentTaskId && showDetail"
    :taskId="currentTaskId"
    @delete="
      showDetail = false;
      refreshTasks();
    "
  />
  <TaskList v-if="!showDetail" :tasks="tasks" @select="handleSelect"></TaskList>
</template>

<script>
import { ref, reactive, onMounted } from "vue";
import { getFilteredTasks } from "../services/TaskApi";
import TaskDetail from "../components/tasks/TaskDetail.vue";
import TaskList from "../components/tasks/TaskList.vue";

export default {
  components: { TaskDetail, TaskList },
  setup() {
    const showDetail = ref(false);
    const tasks = reactive([]);
    const currentTaskId = ref(null);

    const handleSelect = (targetId) => {
      currentTaskId.value = targetId;
      showDetail.value = true;
    };

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
      showDetail,
      tasks,
      currentTaskId,
      handleSelect,
      refreshTasks,
    };
  },
};
</script>

<style>
</style>