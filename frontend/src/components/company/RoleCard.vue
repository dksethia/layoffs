<script setup lang="ts">
const props = defineProps(['role'])
</script>

<template>
    <div>
        <div>{{ props.role.name }}</div>
    </div>
</template>