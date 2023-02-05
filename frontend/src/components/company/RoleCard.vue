<script setup lang="ts">
const props = defineProps(["role"]);
</script>

<template>
  <div class="bg-slate-900 rounded my-3 p-3 cursor-pointer">
    <h2 class="font-bold text-xl">{{ props.role.name }}</h2>
    <p>{{ props.role.location }}</p>
  </div>
</template>
