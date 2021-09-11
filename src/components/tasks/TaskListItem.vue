<template>
  <div class="p-2 rounded-sm shadow-sm bg-white flex items-center">
    <div class="mx-3">
      <StatusIndicator :color="color" />
    </div>
    <div
      @click="$emit('select')"
      @keyup.enter="$emit('select')"
      role="button"
      tabindex="0"
      class="
        mx-3
        p-1
        flex-grow
        truncate
        cursor-pointer
        focus:outline-none
        focus:ring-2 focus:ring-indigo-200
      "
    >
      {{ name }}
    </div>
    <TaskTimer
      :taskId="taskId"
      :running="clockRunning"
      :seconds="clockSeconds"
      @start="toggleClock(taskId)"
      @stop="toggleClock(taskId)"
    />
  </div>
</template>

<script>
import StatusIndicator from "../ui/StatusIndicator.vue";
import TaskTimer from "./TaskTimer.vue";
import { toggleClock } from "../../services/TaskApi";

export default {
  components: { StatusIndicator, TaskTimer },
  props: {
    taskId: { type: Number, required: true },
    name: { type: String, required: true },
    status: { type: String, required: true },
    color: { type: String, required: true },
    clockRunning: { type: Boolean, default: false },
    clockSeconds: { type: Number, default: 0 },
  },
  setup() {
    return { toggleClock };
  },
};
</script>

<style>
</style>