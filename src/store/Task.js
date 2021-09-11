import { reactive, readonly } from "vue";

const state = reactive({
  runningClock: {
    taskId: null,
  },
});

const methods = {
  setRunningClock(taskId) {
    state.runningClock.taskId = taskId;
  },
};

export default {
  state: readonly(state),
  methods,
};
