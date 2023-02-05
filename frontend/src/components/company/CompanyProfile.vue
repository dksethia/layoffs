<template></template>
<!-- <script setup lang="ts">
import type { Candidate } from "@/types/Candidate";
import type { Company } from "@/types/Company";
import { ref } from "vue";

const company: Company = {
  id: "1",
  email: "email@yt.com",
  name: "YouTube",
  recruited: number,
  sustainabilityScore: number,
  inclusivityScore: number,
  description: string,
  website: string,
  logoUrl: string,
};

// // Fetching the data in real time
// const user = ref(null)
// fetch("http://localhost:3000/api/user")
//     .then((response) => response.json())
//     .then((data) => {
//         user.value = data;
//     });
</script>
<template>
  <div class="flex justify-center p-5 gap-5">
    <div class="flex flex-col">
      <div>
        <v-avatar
          size="20em"
          image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
        />
      </div>
      <div>{{ user.firstName.toUpperCase() }}</div>
      <div class="text-2xl font-bold">{{ user.lastName.toUpperCase() }}</div>
      <div class="mt-5">
        {{ user.profileSummary }}
      </div>
    </div>
    <div class="w-1/2">
      <v-text-field
        disabled
        :model-value="user.email"
        variant="outlined"
        label="Email"
      />
      <v-text-field
        disabled
        :model-value="user.linkedin"
        variant="outlined"
        label="Linkedin"
      />
      <v-text-field
        disabled
        :model-value="user.formerCompany"
        variant="outlined"
        label="Former Company"
      />
      <v-text-field
        disabled
        :model-value="user.formerRole"
        variant="outlined"
        label="Most recent role"
      />
      <v-text-field
        disabled
        :model-value="user.location"
        variant="outlined"
        label="Lives in"
      />
      <v-text-field
        disabled
        :model-value="user.remote ? 'Yes!' : 'Unfortunately not'"
        variant="outlined"
        label="Open for remote working"
      />
      <v-text-field
        disabled
        :model-value="user.gender"
        variant="outlined"
        label="Gender"
      />
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
</style> -->
