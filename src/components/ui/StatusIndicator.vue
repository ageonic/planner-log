<template>
  <div class="p-1 rounded-full" :style="'background-color:' + color">
    <div class="p-1 bg-white rounded-full"></div>
  </div>
</template>

<script>
export default {
  props: {
    color: { type: String, default: "red" },
  },
};
</script>