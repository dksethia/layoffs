<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import UserProfile from "@/components/user/UserProfile.vue";
import CompanyProfile from "@/components/company/CompanyProfile.vue";
</script>
<template>
    <div>
        <UserProfile v-if="useAuthStore().isUser()"/>
        <CompanyProfile v-else />
    </div>
</template>
