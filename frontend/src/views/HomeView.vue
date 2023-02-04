<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import UserView from "./UserView.vue";
</script>

<template>
    <UserView v-if="useAuthStore().isUser()"/>
</template>
