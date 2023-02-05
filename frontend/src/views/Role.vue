<script setup lang="ts">
import router from '@/router';
import { useRoute } from 'vue-router';
import { useCompanyStore } from '@/stores/company';
import CandidateCard from '@/components/company/CandidateCard.vue';

const route = useRoute()
</script>

<template>
  <div>
    <CandidateCard
      v-for="candidate in useCompanyStore().getCandidates(route.params.id[0])"
      :key="candidate.id"
      :candidate="candidate"
    />
  </div>
</template>