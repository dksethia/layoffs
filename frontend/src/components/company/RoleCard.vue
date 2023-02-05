<script setup lang="ts">
const props = defineProps(["role"]);
</script>

<template>
  <div class="bg-[#1a1c23] rounded my-3 p-3 cursor-pointer hover:bg-[#1f1f2d]">
    <h2 class="font-bold text-xl">{{ props.role.name }}</h2>
    <p>{{ props.role.location }}</p>
  </div>
</template>
