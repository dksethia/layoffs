<script setup lang="ts">
import LinkedIn from "@/assets/LinkedIn.vue"

const props = defineProps(["candidate"]);

function log() {
  console.log("click")
}
</script>

<!-- <template>
  <div class="bg-slate-500 rounded my-3 p-3 cursor-pointer">
    <h2 class="font-bold text-xl">{{ `${props.candidate.firstName} ${props.candidate.lastName}` }}</h2>
    <p> {{ `ex-${props.candidate.formerRole}, ${props.candidate.formerCompany}` }} </p>
    <p> {{ `${props.candidate.experience} years of experience` }} </p>
    <v-btn :href="props.candidate.linkedin" target="_blank" :icon="LinkedIn"></v-btn>
    <v-btn :href="`mailto:${props.candidate.email}`" >Email</v-btn>
    
  </div>
</template> -->

<template>
    <v-card>
      <v-card-title> {{ `${props.candidate.firstName} ${props.candidate.lastName}` }} </v-card-title>
      <v-card-subtitle>{{ `ex-${props.candidate.formerRole}, ${props.candidate.formerCompany}` }}</v-card-subtitle>
      <v-card-subtitle>{{ `${props.candidate.experience} years of experience` }}</v-card-subtitle>
      <v-card-actions>
          <v-btn :href="props.candidate.linkedin" target="_blank" :icon="LinkedIn"></v-btn>
          <v-btn :href="`mailto:${props.candidate.email}`" >Email</v-btn>
      </v-card-actions>
    </v-card>
</template>