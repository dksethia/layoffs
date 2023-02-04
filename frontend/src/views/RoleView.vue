<script setup lang="ts">
import { useCompanyStore } from "@/stores/company";

const companyRoles = [
    {id: "1", name:"Frontend Developer"},
    {id: "2", name:"Backend Developer"}
]

</script>

<template>
    <div>
        <h1 class="text-2xl font-bold ">Roles</h1>
        <div v-for="role in companyRoles" :key="role.id" :href="role.id">{{ role.name }}</div>
    </div>
</template>