<script setup lang="ts">
import { ref, computed } from "vue";
const d = ref(4);

const double = computed(() => d.value * 2);
</script>
<template>
  <div>
    <button @click="d++">inc</button>
    <h1>{{ double }}This is the profile page</h1>
  </div>
</template>
