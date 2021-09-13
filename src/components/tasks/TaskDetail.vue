<template>
  <article class="h-auto w-full shadow-lg bg-white rounded-md flex flex-col">
    <section
      name="header"
      class="border-b-2 border-gray-100 flex items-center px-8 py-4"
    >
      <div class="flex flex-grow justify-between">
        <div v-if="task.status" class="">
          <TaskStatusEditor :taskId="taskId" :taskStatus="task.status" />
        </div>
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
      <p class="mt-6 tracking-wider leading-6 whitespace-pre-wrap">
        {{ task.description }}
      </p>
    </section>
    <section v-if="editMode" name="task-editor" class="p-8">
      <TaskEditor
        :taskId="task.id"
        :name="task.name"
        :description="task.description"
        :statusId="task.status.id"
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
      <TaskList :tasks="task.subtasks" />
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
        @create="
          refresh();
          showSubtaskCreator = false;
        "
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
import TaskStatusEditor from "../tasks/TaskStatusEditor.vue";
import TaskEditor from "./TaskEditor.vue";
import TaskList from "./TaskList.vue";

export default {
  components: { PlusIcon, TaskStatusEditor, TaskEditor, TaskList },
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

    const refresh = () => {
      getOneTask(props.taskId).then((t) => {
        Object.assign(task, t);
      });
    };

    onMounted(() => {
      refresh();
    });

    return {
      task,
      editMode,
      showSubtaskCreator,
      handleUpdate,
      deleteTask,
      refresh,
    };
  },
};
</script>

<style>
</style>