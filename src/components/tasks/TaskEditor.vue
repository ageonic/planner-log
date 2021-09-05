<template>
  <form @submit.prevent>
    <div class="grid grid-cols-2 gap-4">
      <div class="col-span-2">
        <TextInput
          v-model="form.name"
          name="task-name"
          label="Task Name"
          :required="true"
        />
      </div>
      <div class="col-span-2">
        <TextArea
          v-model="form.description"
          name="task-description"
          label="Description"
        />
      </div>
    </div>
    <div class="mt-4">
      <button
        type="submit"
        @click="submit"
        class="
          py-2
          px-4
          border border-transparent
          shadow-sm
          text-sm
          font-medium
          rounded-md
          text-white
          bg-indigo-500
          hover:bg-indigo-600
          focus:outline-none
          focus:ring-2 focus:ring-offset-2 focus:ring-indigo-200
        "
      >
        Save
      </button>
      <button
        type="button"
        @click="cancel"
        class="
          ml-2
          py-2
          px-4
          text-sm
          font-medium
          rounded-md
          text-gray-500
          focus:outline-none
          focus:ring-2 focus:ring-offset-2 focus:ring-indigo-200
        "
      >
        Cancel
      </button>
    </div>
  </form>
</template>

<script>
import { reactive } from "@vue/reactivity";
import TextArea from "../ui/inputs/TextArea.vue";
import TextInput from "../ui/inputs/TextInput.vue";
import { createOneTask, updateOneTask } from "../../services/TaskApi";

export default {
  components: { TextArea, TextInput },
  props: {
    taskId: { type: Number },
    name: { type: String, default: "" },
    description: { type: String, default: "" },
    parentId: { type: Number, default: 0 },
  },
  emits: ["cancel", "create", "update"],
  setup(props, { emit }) {
    const form = reactive({
      name: props.name,
      description: props.description,
      parent_id: props.parentId,
    });

    const submit = () => {
      if (props.taskId) {
        updateOneTask(props.taskId, form).then((t) => emit("update", t));
      } else {
        createOneTask(form).then((t) => emit("create", t));
      }
    };

    const cancel = () => {
      emit("cancel");
    };

    return { form, submit, cancel };
  },
};
</script>

<style>
</style>