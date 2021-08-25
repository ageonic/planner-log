<template>
  <div
    class="
      h-screen
      w-full
      bg-black bg-opacity-50
      flex
      items-center
      justify-center
      fixed
      left-0
      top-0
      z-40
    "
  >
    <div
      class="
        h-auto
        w-1/2
        text-gray-600
        flex flex-col
        rounded-md
        overflow-hidden
        z-50
      "
    >
      <header class="w-full bg-white flex items-center">
        <h1 class="flex-grow p-4 capitalize">
          {{ header }}
        </h1>
        <button class="p-4" :title="closeLabel" @click="closeModal">
          <XIcon class="h-4 w-4" />
        </button>
      </header>
      <main class="w-full bg-gray-50 border-t border-b p-4">
        <slot name="content"></slot>
      </main>
      <footer class="w-full bg-white flex items-center justify-between">
        <button class="p-4" :title="closeLabel" @click="closeModal">
          {{ closeLabel }}
        </button>
        <slot name="actions"></slot>
      </footer>
    </div>
  </div>
</template>

<script>
import { XIcon } from "@heroicons/vue/solid";

export default {
  components: { XIcon },
  props: {
    header: { type: String, required: true },
    closeLabel: { type: String, default: "Close" },
  },
  setup(props, { emit }) {
    const closeModal = () => {
      emit("close");
    };

    return { closeModal };
  },
};
</script>

<style>
</style>