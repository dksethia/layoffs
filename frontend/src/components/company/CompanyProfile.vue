<script setup lang="ts">
import type { Company } from "@/types/Company";
import { ref } from "vue";
import PieChart from "../PieChart.vue";

const company: Company = {
  id: "1234",
  name: "YouTube",
  email: "email@yt.com",
  recruited: 900,
  sustainability_score: 0.9,
  diversity_inclusive: 0.5,
  description:
    "An amazing company where you can help build the website for watching cat videos.",
  website: "youtube.com",
  logoUrl: "https://thispersondoesnotexist.com/image",
};

const companyRec = ref(0);
const interval = setInterval(() => {
  if (companyRec.value < company.recruited) {
    companyRec.value += Math.max(Math.round(company.recruited / 100), 1);
  } else {
    companyRec.value = company.recruited;
    clearInterval(interval);
  }
}, 15);
</script>
<template>
  <div class="flex justify-center p-28 gap-5">
    <div class="flex flex-col">
      <div>
        <v-avatar size="20em" :image="company.logoUrl" />
      </div>
      <div class="font-bold text-3xl">{{ company.name }}</div>
      <div class="mt-5">
        {{ company.description }}
      </div>
    </div>
    <div class="flex flex-col items-center">
      <div class="flex flex-col items-center">
        <div class="text-center">Sustainability Score</div>
        <PieChart :p="company.sustainability_score * 100" />
      </div>
      <div class="flex flex-col items-center">
        <div class="text-center">Inclusivity Score</div>
        <PieChart :p="company.diversity_inclusive * 100" />
      </div>
    </div>
    <div class="w-1/2">
      <v-text-field
        disabled
        :model-value="company.email"
        variant="outlined"
        label="Email"
      />
      <v-text-field
        disabled
        :model-value="company.website"
        variant="outlined"
        label="Website"
      />
      <div class="flex flex-col items-center text-4xl">
        Recruited
        <div class="font-bold text-9xl">{{ companyRec }}</div>
        People!
      </div>
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
</style>
