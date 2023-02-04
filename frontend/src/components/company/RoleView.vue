<script setup lang="ts">
import router from "@/router";
import { useCompanyStore } from "@/stores/company";
import Role from "@/components/company/RoleCard.vue"

const companyRoles = useCompanyStore().company!.roles
</script>

<template>
    <div>
        <h1 class="text-2xl font-bold ">Roles</h1>
        <button @click="router.push({ name: 'addRole'})"> Add new role </button> 
        <Role 
            v-for="role in companyRoles" 
            :key="role.id" 
            @click="router.push({ name: 'role', params: { id: role.id } })"
            :role=role 
        />
    </div>
</template>