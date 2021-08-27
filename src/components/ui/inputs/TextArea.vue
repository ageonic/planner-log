<template>
  <label :for="name" class="block text-sm font-medium text-gray-500 capitalize">
    {{ label }}
  </label>
  <textarea
    :id="name"
    :name="name"
    :placeholder="placeholder"
    :required="required"
    :rows="rows"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    class="
      mt-1
      p-2
      block
      w-full
      shadow-sm
      sm:text-sm
      border border-gray-200
      rounded-md
      focus:outline-none
      focus:ring-2 focus:ring-indigo-200
    "
  ></textarea>
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    label: { type: String, required: true },
    rows: { type: Number, default: 4 },
    placeholder: { type: String },
    required: { type: Boolean, default: false },
    modelValue: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>