<script setup lang="ts">
import type { Company } from "@/types/Company";
import { ref } from "vue";
import { useCompanyStore } from "@/stores/company";
import PieChart from "../PieChart.vue";
import type { RoleWithCompany } from "@/types/Role";

const company: Company = {
  address: "",
  company_id: "1234",
  contact: "",
  name: "YouTube",
  email: "email@yt.com",
  recruited: 900,
  sustainability_score: 0.9,
  diversity_inclusive: 0.5,
  description:
    "An amazing company where you can help build the website for watching cat videos.",
  website_link: "youtube.com",
  logoUrl: "https://thispersondoesnotexist.com/image",
};

const companyStore = useCompanyStore()
// const roles = companyStore.getRoles()
const roles = ref<RoleWithCompany[]>([
  {
    company: {
      address: "",
      company_id: "1234",
      contact: "",
      name: "YouTube",
      email: "email@yt.com",
      recruited: 90,
      sustainability_score: 0.9,
      diversity_inclusive: 0.5,
      description:
        "An amazing company where you can help build the website for watching cat videos.",
      website_link: "youtube.com",
      logoUrl: "url",
    },
    role_id: "1234",
    companyId: "1234",
    name: "Software Engineer",
    location: "US",
    remote: true,
    description:
      "Role description description description description description description description description",
    list_people_interested_in_role: ["123", "456"],
  },
]);

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
    <div>
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
                :href="company.website_link"
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
                <div class="text-center text-xl font-bold">Sustainability at</div>
                <PieChart :p="company.sustainability_score * 100" big="true" />
                </div>
                <div class="flex flex-col items-center text-xl font-bold">
                <div class="text-center"> Inclusivity at</div>
                <PieChart :p="(((Math.random() * 0.49) + 0.5) * 100)" big="true" />
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
        <div class="flex flex-col items-center grow">
            <h2 class="font-bold text-4xl"> Open Roles </h2>
            <div
                v-for="r in roles"
                class="w-4/5 flex justify-center text-white m-2 p-5"
                @click="
                () => {}
                "
            >
                <div
                class="flex flex-col justify-between rounded-lg shadow-lg justify-around bg-[#1a1c23] mr-4 p-4"
                >
                <div class="font-bold text-xl">{{ r.name }}</div>
                <div class="text-sm">{{ r.description }}</div>
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
