<script setup lang="ts">
import NavBar from "./components/NavBar.vue";
import SignIn from "./components/SignIn.vue";
import { useAuthStore } from "./stores/auth";
useAuthStore().initAuth();
</script>

<template>
  <div
    v-if="useAuthStore().userType"
    class="text-white flex min-h-screen flex-col bg-[#121317]"
  >
    <NavBar />
    <RouterView v-slot="{ Component, route }">
      <transition name="fade" mode="out-in">
        <component :is="Component" :key="route.path" />
      </transition>
    </RouterView>
  </div>
  <SignIn v-else />
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>
