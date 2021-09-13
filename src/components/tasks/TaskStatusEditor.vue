<template>
  <div class="p-1 relative">
    <button
      @click="toggleDropdown"
      class="
        p-2
        z-10
        relative
        bg-white
        rounded-md
        focus:outline-none
        focus:ring-2 focus:ring-indigo-200
        flex
        items-center
      "
    >
      <div class="p-1">
        <StatusIndicator :color="taskStatus.color" />
      </div>
      <div v-if="showLabel" class="ml-3 flex-grow capitalize text-gray-300">
        {{ taskStatus.label }}
      </div>
    </button>
    <ul
      v-if="dropdownVisible"
      class="
        absolute
        left-0
        mt-2
        py-2
        w-48
        bg-white
        rounded-md
        shadow-xl
        z-20
        border border-gray-50
      "
    >
      <li
        v-for="status in TaskStore.statusList"
        :key="status.id"
        tabindex="0"
        @click="updateTaskStatus(status.id)"
        @keyup.enter="updateTaskStatus(status.id)"
        class="
          px-4
          py-2
          text-sm
          capitalize
          cursor-pointer
          text-gray-700
          hover:bg-indigo-100
          focus:outline-none
          focus:ring-2 focus:ring-indigo-200
          flex
          items-center
        "
      >
        <div class="p-1">
          <StatusIndicator :color="status.color" />
        </div>
        <div class="ml-3 flex-grow capitalize text-gray-600">
          {{ status.label }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { reactive, ref } from "@vue/reactivity";
import StatusIndicator from "../ui/StatusIndicator.vue";
import TaskStore from "../../store/Task";
import { updateOneTask } from "../../services/TaskApi";

export default {
  components: { StatusIndicator },
  props: {
    taskId: { type: Number, required: true },
    taskStatus: {
      type: Object,
      required: true,
      validator(value) {
        return ["color", "label"].every((key) =>
          Object.keys(value).includes(key)
        );
      },
    },
    showLabel: { type: Boolean, default: true },
  },
  setup(props) {
    const dropdownVisible = ref(false);
    const taskStatus = reactive(props.taskStatus);

    const toggleDropdown = () => {
      dropdownVisible.value = !dropdownVisible.value;
    };

    const updateTaskStatus = (selectedStatusId) => {
      updateOneTask(props.taskId, { status_id: selectedStatusId }).then((t) => {
        for (let key of Object.keys(t.status)) {
          taskStatus[key] = t.status[key];
        }
      });
      toggleDropdown();
    };

    return {
      taskStatus,
      dropdownVisible,
      TaskStore,
      toggleDropdown,
      updateTaskStatus,
    };
  },
};
</script>

<style>
</style>