<template>
  <article class="h-auto w-full shadow-lg bg-white rounded-md flex flex-col">
    <section
      name="header"
      class="border-b-2 border-gray-100 flex items-center px-8 py-4"
    >
      <div class="flex flex-grow items-center">
        <div class="mr-2"><StatusIndicator color="#7896FF" /></div>
        <div class="flex-grow capitalize text-gray-300">task status</div>
        <div v-if="!editMode">
          <button
            @click="editMode = true"
            class="
              p-2
              rounded
              border border-transparent
              hover:border-gray-200
              focus:outline-none
              focus:ring-2 focus:ring-indigo-200
            "
          >
            Edit task
          </button>
        </div>
      </div>
    </section>
    <section v-if="!editMode" name="details" class="p-8">
      <h1 class="text-2xl">{{ task.name }}</h1>
      <p class="mt-6 tracking-wider leading-6">
        Candy chocolate cake toffee powder ice cream cheesecake. Candy canes
        cake jujubes dragée jujubes croissant lemon drops. Bear claw jelly-o
        jelly-o donut dragée candy candy canes jujubes chupa chups. Jelly halvah
        candy canes marshmallow tart.
      </p>
    </section>
    <section v-if="editMode" name="task-editor" class="p-8">
      <TaskEditor
        :taskId="task.id"
        :name="task.name"
        :parentId="task.parent_id"
        @update="handleUpdate"
        @cancel="editMode = false"
      />
    </section>
    <section
      name="subtasks"
      class="p-8 bg-gray-50 border-t-2 border-b-2 border-gray-100"
    >
      <h2>Subtasks for {{ task.name }}</h2>
      <button
        v-if="!showSubtaskCreator"
        @click="showSubtaskCreator = true"
        class="
          mt-2
          p-2
          rounded
          border border-gray-200
          hover:bg-gray-200
          focus:outline-none
          focus:ring-2 focus:ring-indigo-200
        "
      >
        <PlusIcon class="h-4 w-4" />
      </button>
      <TaskEditor
        v-if="showSubtaskCreator"
        :parentId="task.id"
        @create="showSubtaskCreator = false"
        @cancel="showSubtaskCreator = false"
      />
    </section>
    <section name="footer" class="px-8 py-4">
      <button
        @click="deleteTask"
        class="
          p-2
          rounded
          border border-transparent
          hover:border-gray-200
          focus:outline-none
          focus:ring-2 focus:ring-indigo-200
        "
      >
        Delete task
      </button>
    </section>
  </article>
</template>

<script>
import { onMounted, reactive, ref } from "@vue/runtime-core";
import { PlusIcon } from "@heroicons/vue/solid";
import { deleteOneTask, getOneTask } from "../../services/TaskApi.js";
import StatusIndicator from "../ui/StatusIndicator.vue";
import TaskEditor from "./TaskEditor.vue";

export default {
  components: { PlusIcon, StatusIndicator, TaskEditor },
  props: {
    taskId: { type: Number, required: true },
  },
  setup(props, { emit }) {
    const task = reactive({});
    const editMode = ref(false);
    const showSubtaskCreator = ref(false);

    const handleUpdate = (updatedTask) => {
      Object.assign(task, updatedTask);
      editMode.value = false;
    };

    const deleteTask = () => {
      deleteOneTask(props.taskId).then(emit("delete"));
    };

    onMounted(() => {
      getOneTask(props.taskId).then((t) => {
        Object.assign(task, t);
      });
    });

    return { task, editMode, showSubtaskCreator, handleUpdate, deleteTask };
  },
};
</script>

<style>
</style>