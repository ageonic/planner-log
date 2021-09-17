<template>
  <header class="flex items-end justify-between mb-4">
    <h2 v-if="!hideTitle" class="text-lg">{{ title }}</h2>
    <button
      @click="setMode('create')"
      class="
        p-2
        border border-gray-200
        rounded
        focus:outline-none
        focus:ring-2 focus:ring-indigo-200
      "
    >
      <PlusIcon class="w-4" />
    </button>
  </header>
  <div class="shadow overflow-hidden border-b border-gray-200 rounded">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th
            v-for="column in columns"
            :key="column.name"
            scope="col"
            class="
              px-6
              py-3
              text-left text-xs
              font-medium
              text-gray-500
              uppercase
              tracking-wider
            "
          >
            {{ column.label }}
          </th>
          <th scope="col" class="relative px-6 py-3">
            <span class="sr-only">Actions</span>
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="d in data" :key="d[primaryColumn]">
          <td
            v-for="column in columns"
            :key="column.name"
            class="px-6 py-2 whitespace-nowrap"
          >
            <div
              v-if="column.type === 'text'"
              class="text-sm font-medium text-gray-900"
            >
              {{ d[column.name] }}
            </div>
            <input
              v-if="column.type === 'checkbox'"
              type="checkbox"
              :checked="d[column.name]"
              disabled
            />
          </td>
          <td class="px-6 py-2 flex justify-center items-center">
            <button
              class="
                p-1
                rounded
                focus:outline-none
                focus:ring-2 focus:ring-indigo-200
              "
              @click="
                setMode('edit');
                Object.assign(currentData, d);
              "
            >
              <PencilIcon class="w-4" />
            </button>
            <button
              @click="$emit('delete', d[primaryColumn])"
              class="
                ml-4
                p-1
                rounded
                focus:outline-none
                focus:ring-2 focus:ring-indigo-200
              "
            >
              <TrashIcon class="w-4" />
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <DataTableEditor
    v-if="mode === 'create' || mode === 'edit'"
    :header="mode + ' ' + title"
    closeLabel="Cancel"
    :columns="columns"
    :data="currentData"
    @save="
      $emit(mode === 'create' ? 'create' : 'update', currentData);
      setMode('read');
      resetCurrentData();
    "
    @close="
      setMode('read');
      resetCurrentData();
    "
  />
</template>

<script>
import { reactive, ref } from "@vue/reactivity";
import { PlusIcon, PencilIcon, TrashIcon } from "@heroicons/vue/solid";
import DataTableEditor from "./DataTableEditor.vue";

export default {
  components: { DataTableEditor, PlusIcon, PencilIcon, TrashIcon },
  props: {
    title: { type: String },
    hideTitle: { type: Boolean, default: false },
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
    primaryColumn: { type: String, required: true },
    data: { type: Array, required: true },
  },
  emits: ["create", "update", "delete"],
  setup(props) {
    // work with three modes: read, create, edit
    const mode = ref("read");
    const currentData = reactive({});

    const resetCurrentData = () => {
      Object.assign(
        currentData,
        props.columns.reduce((obj, col) => ({ ...obj, [col.name]: null }), {
          [props.primaryColumn]: null,
        })
      );
    };

    const setMode = (val) => {
      mode.value = val;
    };

    return {
      mode,
      currentData,
      resetCurrentData,
      setMode,
    };
  },
};
</script>

<style>
</style>