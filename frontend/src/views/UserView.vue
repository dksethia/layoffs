<script setup lang="ts">
import { ref } from "vue";

const companies = [
  {
    id: "1",
    email: "email@yt.com",
    name: "YouTube",
    logo: "url",
    sus_scote: 0.9,
    description:
      "An amazing company where you can help build the website for watching cat videos.",
    website: "youtube.com",
    role_name: "Software Engineer",
    inclusive: true,
    location: "US",
    remote: true,
  },
  {
    id: "2",
    email: "email@google.com",
    name: "Google",
    logo: "url",
    sus_scote: 0.7,
    description: "Come work for us, we fired all the good people.",
    website: "google.com",
    role_name: "Junior Software Engineer",
    inclusive: false,
    location: "UK",
    remote: false,
  },
];

let locs = new Set<string>();
let remote = false;
let inclusive = false;

companies.forEach(function (company) {
  locs.add(company.location);
  if (company.remote) {
    remote = true;
  }
  if (company.inclusive) {
    inclusive = true;
  }
});

let locations = Array.from(locs);

const role = ref("");
</script>

<template>
  <div class="flex flex-col items-center">
    <!-- Side bar -->
    <div class="w-1/2 flex justify-center items-center">
      <v-select
        id="select"
        class="w-full"
        label="Select"
        :items="locations"
        multiple
      >
      </v-select>
    </div>
    <!-- Main part of the website -->
    <div class="w-3/5 bg-slate-800 m-2 p-4 rounded-lg">
      <label for="email-address" class="sr-only">Search</label>
      <input
        v-model="role"
        id="role"
        name="role"
        class="relative block w-full appearance-none rounded-lg border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
        placeholder="Search your dream job..."
      />
    </div>
    <div v-for="c in companies" class="w-3/5">
      <div class="w-full bg-slate-800 m-2 p-4 rounded-lg">
        <div class="font-bold">{{ c.name }}</div>
        <div>{{ c.description }}</div>
      </div>
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
</style>
