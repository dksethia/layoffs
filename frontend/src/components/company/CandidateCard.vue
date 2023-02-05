<script setup lang="ts">
import LinkedIn from "@/assets/LinkedIn.vue"

const props = defineProps(["candidate"]);
</script>

<!-- <template>
  <div class="bg-slate-400 rounded my-3 p-3 cursor-pointer">
    <h2 class="font-bold text-xl">{{ props.candidate.name }}</h2>
    <p> {{ props.candidate.formerRole }}, {{ props.candidate.formerCompany }}</p>
    
  </div>
</template> -->

<template>
  <v-card :title="props.candidate.name" :subtitle="`ex-${props.candidate.formerRole}, ${props.candidate.formerCompany}`">
    <v-card-actions>
        <LinkedIn :href="props.candidate.linkedin"/>
        <v-btn>Email</v-btn>
    </v-card-actions>
  </v-card>
</template>