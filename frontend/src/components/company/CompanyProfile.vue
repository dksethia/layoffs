<script setup lang="ts">
import type { Company } from "@/types/Company";
import { ref } from "vue";
import PieChart from "../PieChart.vue";

const company: Company = {
  id: "1234",
  name: "YouTube",
  email: "email@yt.com",
  recruited: 900,
  sustainabilityScore: 0.9,
  inclusivityScore: 0.5,
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
    <div class="flex flex-col bg-[#1a1c23] p-8 rounded-[40px] shadow-lg">
      <div class="flex justify-center">
        <v-avatar size="20em" :image="company.logoUrl" />
      </div>
      <div class="font-bold text-3xl">{{ company.name }}</div>
      <div class="mt-5">
        {{ company.description }}
      </div>
      <div class="flex justify-around mt-5">
        <a
          :href="`mailto:${company.email}`"
          class="bg-purple-300 hover:bg-purple-200 text-black p-3 rounded"
          >Email</a
        >
        <a
          :href="company.website"
          target="_blank"
          class="bg-purple-300 hover:bg-purple-200 text-black p-3 rounded"
          >Website</a
        >
      </div>
    </div>
    <div class="w-1/2 flex flex-col gap-5 justify-between">
      <div
        class="flex justify-around bg-[#1a1c23] p-8 rounded-[40px] shadow-lg grow"
      >
        <div class="flex flex-col items-center">
          <div class="text-center text-xl font-bold">Sustainability Score</div>
          <PieChart :p="company.sustainabilityScore * 100" big="true" />
        </div>
        <div class="flex flex-col items-center text-xl font-bold">
          <div class="text-center">Inclusivity Score</div>
          <PieChart :p="company.inclusivityScore * 100" big="true" />
        </div>
      </div>
      <div
        class="flex justify-around bg-[#1a1c23] p-8 rounded-[40px] shadow-lg"
      >
        <div class="flex flex-col items-center text-4xl">
          Recruited
          <div class="font-bold text-9xl">{{ companyRec }}</div>
          People!
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
</style>
