<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useCompanyStore } from '@/stores/company';

const route = useRoute()
const candidates = useCompanyStore().getCandidates()
</script>

<template>
    <div>
        {{ route.params.id }}
    </div>
</template>