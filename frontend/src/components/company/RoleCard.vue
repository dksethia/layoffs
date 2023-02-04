<script setup lang="ts">
const props = defineProps(["role"]);
</script>

<template>
  <div class="bg-white rounded my-3 p-3">
    <h2 class="font-bold">{{ props.role.name }}</h2>
    <p>{{ props.role.location }}</p>
  </div>
</template>
