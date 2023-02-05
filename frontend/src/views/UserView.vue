<script setup lang="ts">
import { computed, ref } from "vue";
import { Switch } from "@headlessui/vue";
import PieChart from "../components/PieChart.vue";

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

let locations = new Set<string>();
let remote = ref(true);
let inclusive = ref(false);

companies.forEach(function (company) {
  locations.add(company.location);
});

let selectedLocations = ref(Array<string>());

// role to pass to the get request
const role = ref("");

const selectedCompanies = computed(() =>
  companies.filter(function (c) {
    if (
      selectedLocations.value.length == 0 ||
      selectedLocations.value.includes(c.location)
    ) {
      if (remote.value || (!remote.value && !c.remote)) {
        if (!inclusive.value || (inclusive.value && c.inclusive)) {
          return c;
        }
      }
    }
  })
);
</script>

<template>
  <div class="flex grow justify-between">
    <div class="bg-slate-900 w-96">
      <div class="flex flex-col items-center">
        <div class="p-5">Locations</div>
        <v-select
          v-model="selectedLocations"
          label="Select"
          :items="Array.from(locations)"
          multiple
          class="w-full"
        />
      </div>
      <div class="text-white flex items-center justify-between p-2">
        Show remote locations
        <Switch
          v-model="remote"
          :class="remote ? 'bg-purple-500' : 'bg-purple-300'"
          class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
        >
          <span
            :class="remote ? 'translate-x-[25px]' : 'translate-x-1'"
            class="translate-y-[2.8px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
          />
        </Switch>
      </div>
      <div class="text-white flex items-center justify-between p-2">
        Show only inclusive employers
        <Switch
          v-model="inclusive"
          :class="inclusive ? 'bg-purple-500' : 'bg-purple-300'"
          class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
        >
          <span
            :class="inclusive ? 'translate-x-[25px]' : 'translate-x-1'"
            class="translate-y-[2.8px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
          />
        </Switch>
      </div>
    </div>
    <div class="flex flex-col items-center grow">
      <!-- Main part of the website -->
      <div class="w-3/5 bg-slate-800 m-2 p-4 rounded-lg">
        <label for="email-address" class="sr-only">Search</label>
        <input
          id="search"
          v-model="role"
          class="relative block w-full appearance-none rounded-lg border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
          placeholder="Search your dream job..."
        />
      </div>
      <div
        v-for="c in selectedCompanies"
        class="w-3/5 shadow-lg flex justify-between bg-slate-900 m-2 p-5 rounded-lg"
      >
        <div class="flex flex-col justify-around">
          <div class="font-bold text-xl">{{ c.name }}</div>
          <div class="text-sm">{{ c.description }}</div>
        </div>
        <PieChart :p="c.sus_scote * 100" />
      </div>
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
#search {
  background: white !important;
}
</style>
