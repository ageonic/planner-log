<template>
  <div v-if="running" class="mx-3 truncate text-gray-300 capitalize">
    {{ timestamp }}
  </div>
  <button
    v-if="!running"
    title="Start timer"
    @click="
      $emit('start');
      start();
    "
    class="p-1 focus:outline-none focus:ring-2 focus:ring-indigo-200"
  >
    <PlayIcon class="w-6 text-indigo-400 hover:text-indigo-600" />
  </button>
  <button
    v-if="running"
    title="Stop timer"
    @click="
      $emit('stop');
      stop();
    "
    class="p-1 focus:outline-none focus:ring-2 focus:ring-indigo-200"
  >
    <StopIcon class="w-6 text-indigo-400 hover:text-indigo-600" />
  </button>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import { onMounted, watch } from "@vue/runtime-core";
import { PlayIcon, StopIcon } from "@heroicons/vue/solid";
import TaskStore from "../../store/Task";

export default {
  components: { PlayIcon, StopIcon },
  props: {
    taskId: { type: Number, required: true },
    running: { type: Boolean, default: false },
    seconds: { type: Number, default: 0 },
  },
  emits: ["start", "stop"],
  setup(props) {
    const running = ref(props.running);
    const seconds = ref(props.seconds);
    const timestamp = computed(() =>
      new Date(1000 * seconds.value).toISOString().substr(11, 8)
    );

    let timer;

    const start = () => {
      timer = setInterval(() => seconds.value++, 1000);
      running.value = true;
      TaskStore.methods.setRunningClock(props.taskId);
    };

    const stop = () => {
      clearInterval(timer);
      running.value = false;
      seconds.value = 0;
    };

    onMounted(() => {
      if (props.running) start();
    });

    watch(TaskStore.state, () => {
      if (
        running.value &&
        TaskStore.state.runningClock.taskId !== props.taskId
      ) {
        stop();
      }
    });

    return { running, timestamp, start, stop };
  },
};
</script>

<style>
</style>