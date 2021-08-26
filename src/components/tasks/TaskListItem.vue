<template>
  <div class="p-3 rounded-sm bg-white flex items-center">
    <div class="mx-3">
      <StatusIndicator :color="color" />
    </div>
    <div class="mx-3 flex-grow truncate">
      {{ name }}
    </div>
    <div class="mx-3 truncate text-gray-300 capitalize">
      {{ status }}
    </div>
  </div>
</template>

<script>
import StatusIndicator from "../ui/StatusIndicator.vue";

export default {
  components: { StatusIndicator },
  props: {
    taskId: { type: Number, required: true },
    name: { type: String, required: true },
    status: { type: String, required: true },
    color: { type: String, required: true },
  },
};
</script>

<style>
</style>