<script setup lang="ts">
import router from "@/router";
import { useCompanyStore } from "@/stores/company";
import RoleCard from "@/components/company/RoleCard.vue";
</script>

<template>
  <div class="p-5 flex flex-col grow">
    <h1 class="text-2xl font-bold">Roles</h1>
    <div class="flex justify-end pb-3">
      <v-btn @click="router.push({ name: 'addRole' })"> Add new role </v-btn>
    </div>
    <RoleCard
      v-for="role in useCompanyStore().roles"
      :key="role.id"
      @click="router.push({ name: 'role', params: { id: role.id } })"
      :role="role"
    />
  </div>
</template>
