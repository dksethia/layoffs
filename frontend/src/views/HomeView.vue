<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import UserView from "./UserView.vue";
import RoleView from "@/components/company/RoleView.vue";
</script>

<template>
  <div class="flex grow">
    <UserView v-if="useAuthStore().isUser()" />
    <RoleView v-else />
  </div>
</template>
