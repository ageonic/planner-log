<template>
  <div
    tabindex="0"
    role="button"
    class="
      p-1
      focus:outline-none
      focus:ring-2 focus:ring-indigo-200
      flex
      items-center
    "
  >
    <div class="p-1">
      <StatusIndicator :color="taskStatus.color" />
    </div>
    <div v-if="showLabel" class="ml-3 flex-grow capitalize text-gray-300">
      {{ taskStatus.label }}
    </div>
  </div>
</template>

<script>
import StatusIndicator from "../ui/StatusIndicator.vue";

export default {
  components: { StatusIndicator },
  props: {
    taskStatus: {
      type: Object,
      required: true,
      validator(value) {
        return ["color", "label"].every((key) =>
          Object.keys(value).includes(key)
        );
      },
    },
    showLabel: { type: Boolean, default: true },
  },
  setup() {},
};
</script>

<style>
</style>