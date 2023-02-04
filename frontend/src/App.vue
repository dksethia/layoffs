<script setup lang="ts">
import NavBar from "./components/NavBar.vue";
import { useAuthStore } from "./stores/auth";
useAuthStore().initAuth();
</script>

<template>
  <div
    v-if="useAuthStore().userType"
    class="flex min-h-screen flex-col bg-primary"
  >
    <NavBar />
    <RouterView />
  </div>
  <button
    v-else
    @click="useAuthStore().updateUser({ type: 'user', ID: 'SFDSF' })"
  >
    Please log in
  </button>
</template>
