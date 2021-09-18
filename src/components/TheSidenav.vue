<template>
  <nav class="h-full w-full bg-gray-200">
    <ul class="">
      <li class="hover:bg-gray-50">
        <router-link class="px-6 py-2 block" to="/">Home</router-link>
      </li>
      <li class="hover:bg-gray-50">
        <router-link class="px-6 py-2 block" to="/daily">Today</router-link>
      </li>
      <li class="hover:bg-gray-50">
        <router-link class="px-6 py-2 block" to="/settings">
          Settings
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {};
</script>

<style>
</style>