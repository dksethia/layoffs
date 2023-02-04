<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import UserView from "./UserView.vue";
</script>

<template>
  <div class="flex grow">
    <UserView v-if="useAuthStore().userType == 'user'"/>
    <h1>This is the home page</h1>
  </div>
</template>
