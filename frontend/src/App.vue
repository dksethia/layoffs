<script setup lang="ts">
import NavBar from "./components/NavBar.vue";
import SignIn from "./components/SignIn.vue";
import { useAuthStore } from "./stores/auth";
useAuthStore().initAuth();
useAuthStore().updateUser({ type: "company", ID: "34" });
</script>

<template>
  <div
    v-if="useAuthStore().userType"
    class="text-white flex min-h-screen flex-col bg-[#121317]"
  >
    <NavBar />
    <RouterView />
  </div>
  <SignIn v-else />
</template>
