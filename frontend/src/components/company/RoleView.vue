<script setup lang="ts">
import router from "@/router";
import {ref} from 'vue';
import { useCompanyStore } from "@/stores/company";
import RoleCard from "@/components/company/RoleCard.vue";
import type { RoleDB } from "@/types/Role";

const roles = ref<RoleDB[]>([])
// let companyId = ''

// fetch(`/api/user_query/developer`)
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data.response[0].company.company_id)
//       companyId = data.response[0].company.company_id
//     });

fetch(`/api/get_roles/117`)
    .then((response) => response.json())
    .then((data) => {
      const items: RoleDB[] = data.items;
      items.forEach((item) => roles.value.push(item))
    });

</script>

<template>
  <div class="p-5 flex flex-col grow">
    <h1 class="text-2xl font-bold">Roles</h1>
    <div class="flex justify-end pb-3">
      <v-btn @click="router.push({ name: 'addRole' })">Add new role </v-btn>
    </div>
    <RoleCard
      tabindex="0"
      v-for="role in roles"
      @keyup.enter="router.push({ name: 'role', params: { id: role.role_id } })"
      :key="role.role_id"
      @click="router.push({ name: 'role', params: { id: role.role_id } })"
      :role="role"
    />
  </div>
</template>
