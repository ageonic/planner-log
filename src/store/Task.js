import { reactive, readonly } from "vue";

const state = reactive({
  runningClock: {
    taskId: null,
  },
});

const statusList = reactive([]);

const methods = {
  setRunningClock(taskId) {
    state.runningClock.taskId = taskId;
  },
  setStatusList(sl) {
    statusList.push(...sl);
  },
};

export default {
  state: readonly(state),
  statusList: readonly(statusList),
  methods,
};
