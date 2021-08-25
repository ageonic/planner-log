<template>
  <button @click="showModal = true">
    <slot name="label">
      <span class="capitalize">{{ mode }}</span>
    </slot>
  </button>
  <Teleport to="body">
    <ModalWindow v-if="showModal" :header="mode" @close="showModal = false">
      <template v-slot:content>
        <TaskDetail v-if="mode === 'view'" :taskId="taskId" />
        <TaskForm
          v-if="mode !== 'view'"
          :taskId="taskId"
          ref="taskForm"
        ></TaskForm>
      </template>
      <template v-slot:actions>
        <button
          v-if="mode !== 'view'"
          class="
            px-4
            py-2
            bg-green-400
            text-white
            rounded-md
            hover:bg-green-500
          "
          @click.prevent="submitTask"
        >
          {{ submitButtonLabel }}
        </button>
      </template>
    </ModalWindow>
  </Teleport>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import ModalWindow from "../ui/ModalWindow.vue";
import TaskDetail from "./TaskDetail.vue";
import TaskForm from "./TaskForm.vue";

export default {
  components: { ModalWindow, TaskDetail, TaskForm },
  props: {
    taskId: { type: Number },
    mode: {
      validator(value) {
        return ["create", "view", "edit"].includes(value);
      },
      default: "create",
    },
  },
  setup(props) {
    const showModal = ref(false);
    const taskForm = ref(null);
    const submitButtonLabel = computed(() =>
      props.mode === "edit" ? "Save" : "Add"
    );

    const submitTask = () => {
      taskForm.value.submit(props.mode === "edit");
      showModal.value = false;
    };

    return { showModal, taskForm, submitButtonLabel, submitTask };
  },
};
</script>

<style>
</style>