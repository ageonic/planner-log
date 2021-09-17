<template>
  <label :for="name" class="block text-sm font-medium text-gray-500 capitalize">
    {{ label }}
  </label>
  <input
    :name="name"
    :id="name"
    type="checkbox"
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
    class="
      mt-1
      p-2
      block
      shadow-sm
      border border-gray-200
      rounded-md
      focus:outline-none
      focus:ring-2 focus:ring-indigo-200
    "
  />
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    label: { type: String, required: true },
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
</style>