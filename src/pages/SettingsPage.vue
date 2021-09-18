<template>
  <DataTable
    title="Task Status"
    primaryColumn="id"
    :columns="statusColumns"
    :data="TaskStore.statusList"
    @create="createOneTaskStatus($event).then(() => refreshTaskStatusList())"
    @update="
      updateOneTaskStatus($event.id, $event).then(() => refreshTaskStatusList())
    "
    @delete="deleteOneTaskStatus($event).then(() => refreshTaskStatusList())"
  />
  <form></form>
</template>

<script>
import TaskStore from "../store/Task";
import DataTable from "../components/ui/data/DataTable.vue";

import {
  createOneTaskStatus,
  updateOneTaskStatus,
  deleteOneTaskStatus,
  getTaskStatusList,
} from "../services/TaskApi";

export default {
  components: { DataTable },
  setup() {
    const statusColumns = [
      { label: "Label", name: "label", type: "text" },
      { label: "Color", name: "color", type: "text" },
      { label: "default", name: "default", type: "checkbox" },
      { label: "is complete status", name: "is_complete", type: "checkbox" },
    ];

    const refreshTaskStatusList = () => {
      getTaskStatusList().then((statusList) =>
        TaskStore.methods.setStatusList(statusList)
      );
    };

    return {
      TaskStore,
      statusColumns,
      createOneTaskStatus,
      updateOneTaskStatus,
      deleteOneTaskStatus,
      refreshTaskStatusList,
    };
  },
};
</script>

<style>
</style>