<template>
  <div class="mx-3 truncate text-gray-300 capitalize">
    {{ timestamp }}
  </div>
  <button v-if="!running" title="Start timer" @click="start" class="">
    <PlayIcon class="w-6 text-indigo-400 hover:text-indigo-600" />
  </button>
  <button v-if="running" title="Stop timer" @click="stop" class="">
    <StopIcon class="w-6 text-indigo-400 hover:text-indigo-600" />
  </button>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import { PlayIcon, StopIcon } from "@heroicons/vue/solid";
export default {
  components: { PlayIcon, StopIcon },
  props: {
    seconds: { type: Number, default: 0 },
    running: { type: Boolean, default: false },
  },
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
    };

    const stop = () => {
      clearInterval(timer);
      running.value = false;
    };

    return { running, seconds, timestamp, start, stop };
  },
};
</script>

<style>
</style>