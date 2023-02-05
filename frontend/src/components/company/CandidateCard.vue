<script setup lang="ts">
import LinkedIn from "@/assets/LinkedIn.vue";

const props = defineProps(["candidate"]);
</script>

<template>
  <div class="flex justify-between bg-[#1a1c23] m-5 p-5 rounded items-center">
    <div>
      <div class="font-bold text-2xl">
        {{ `${props.candidate.firstName} ${props.candidate.lastName}` }}
      </div>
      <div>
        {{
          `ex-${props.candidate.formerRole}, ${props.candidate.formerCompany}`
        }}
      </div>
      <div>
        {{ `${props.candidate.experience} years of experience` }}
      </div>
    </div>
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
  </div>
</template>
