<script setup lang="ts">
import NavBar from "./components/NavBar.vue";
import SignIn from "./components/SignIn.vue";
import { useAuthStore } from "./stores/auth";
import UserView from "./views/UserView.vue";
useAuthStore().initAuth();
</script>

<template>
  <div
    v-if="useAuthStore().userType"
    class="dark flex min-h-screen flex-col dark:bg-slate-800"
  >
    <NavBar />
    <RouterView />
  </div>
  <SignIn v-else />
</template>
