<script setup lang="ts">
import router from "@/router";
import { useCompanyStore } from "@/stores/company";
import Role from "@/components/company/RoleCard.vue"

const companyRoles = [
    {id: "1", name:"Frontend Developer"},
    {id: "2", name:"Backend Developer"}
]

</script>

<template>
    <div>
        <h1 class="text-2xl font-bold ">Roles</h1>
        <button @click="router.push({ name: 'addRole'})"> Add new role </button> 
        <div 
            v-for="role in companyRoles" 
            :key="role.id" 
            @click="router.push({ name: 'role', params: { id: role.id } })" 
        >
            <Role :role=role />
        </div>
    </div>
</template>