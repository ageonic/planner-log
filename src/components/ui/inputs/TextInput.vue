<template>
  <label :for="name" class="block text-sm font-medium text-gray-500 capitalize">
    {{ label }}
  </label>
  <input
    :name="name"
    :id="name"
    :type="type"
    :placeholder="placeholder"
    :autocomplete="autocomplete"
    :required="required"
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
  />
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    label: { type: String, required: true },
    type: {
      type: String,
      validator(value) {
        return ["password", "text"].includes(value);
      },
      default: "text",
    },
    placeholder: { type: String },
    autocomplete: { type: String, default: "off" },
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