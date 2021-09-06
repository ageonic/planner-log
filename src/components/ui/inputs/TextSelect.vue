<template>
  <label :for="name" class="block text-sm font-medium text-gray-500 capitalize">
    {{ label }}
  </label>
  <select
    :id="name"
    :name="name"
    :autocomplete="autocomplete"
    :required="required"
    :value="modelValue"
    @change="$emit('update:modelValue', $event.target.value)"
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
  >
    <option v-for="option in options" :key="option.value" :value="option.value">
      {{ option.label }}
    </option>
  </select>
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    label: { type: String, required: true },
    autocomplete: { type: String, default: "off" },
    required: { type: Boolean, default: false },
    options: {
      type: Array,
      validator(value) {
        return value.every((v) =>
          ["label", "value"].every((k) => Object.keys(v).includes(k))
        );
      },
      required: true,
    },
    modelValue: {
      type: [String, Number],
      default: "",
    },
  },
};
</script>

<style>
</style>