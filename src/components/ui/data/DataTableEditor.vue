<template>
  <ModalWindow>
    <template v-slot:content>
      <div v-for="column in columns" :key="column.name">
        <TextInput
          v-if="column.type === 'text'"
          :label="column.label"
          :name="column.name"
          :type="column.type"
          v-model="data[column.name]"
        />
        <CheckboxInput
          v-if="column.type === 'checkbox'"
          :label="column.label"
          :name="column.name"
          v-model="data[column.name]"
        />
      </div>
    </template>
    <template v-slot:actions>
      <button
        @click="$emit('save')"
        class="
          px-4
          py-2
          bg-indigo-500
          hover:bg-indigo-600
          text-white
          rounded
          focus:outline-none
          focus:ring-2 focus:ring-indigo-200
        "
      >
        Save
      </button>
    </template>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../ModalWindow.vue";
import CheckboxInput from "../inputs/CheckboxInput.vue";
import TextInput from "../inputs/TextInput.vue";

export default {
  components: { ModalWindow, CheckboxInput, TextInput },
  props: {
    columns: {
      type: Array,
      required: true,
      validator(value) {
        return value.every((column) =>
          ["name", "label", "type"].every((key) =>
            Object.keys(column).includes(key)
          )
        );
      },
    },
    data: { type: Object, default: () => ({}) },
  },
  emits: ["save"],
};
</script>

<style>
</style>