<script setup lang="ts">
import LinkedIn from "@/assets/LinkedIn.vue";
import Heart from "@/assets/Heart.vue";
import { useRoute } from 'vue-router';
import { useCompanyStore } from "@/stores/company";
const props = defineProps(["candidate"]);
const route = useRoute()

const companyStore = useCompanyStore()

function isInterested() {
  return companyStore.getRole(route.params.id[0]).list_people_interested_in_role.includes(props.candidate.id)
}
</script>

<template>
  <div class="flex justify-between bg-[#1a1c23] m-5 p-5 rounded-lg items-center hover:bg-[#1f1f2d]">
    <div class="pl-4">
      <div class="font-bold text-2xl">
        {{ `${props.candidate.firstName} ${props.candidate.lastName}` }}
      </div>
      <div class="text-sm pt-2">
        {{
          `ex-${props.candidate.formerRole}, ${props.candidate.formerCompany}`
        }}
      </div>
      <div class="text-sm">
        {{ `${props.candidate.experience} years of experience` }}
      </div>
    </div>
    <div class="flex flex-row justify-center">
      <div class="flex flex-col gap-4 items-center mt-5">
        <a :href="props.candidate.linkedin" target="_blank">
          <LinkedIn />
        </a>
        <a
          :href="`mailto:${props.candidate.email}`"
          class="bg-gray-800 px-3 py-1 rounded hover:bg-gray-700"
        >
          Email
        </a>
      </div>
      <div class="flex items-center px-5" :class="{ invisible: !isInterested() }">
          <Heart />
      </div>
    </div>
  </div>
</template>
