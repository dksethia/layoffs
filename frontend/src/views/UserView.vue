<script setup lang="ts">
import { computed, ref } from "vue";
import { Switch } from "@headlessui/vue";
import PieChart from "../components/PieChart.vue";
import type { RoleWithCompany } from "@/types/Role";

const roles = ref<RoleWithCompany[]>([]);
// [  {
//     id: "1",
//     email: "email@yt.com",
//     name: "YouTube",
//     logoUrl: "url",
//     sustainabilityScore: 0.9,
//     description:
//       "An amazing company where you can help build the website for watching cat videos.",
//     website: "youtube.com",
//     roleName: "Software Engineer",
//     inclusivityScore: 0.5,
//     location: "US",
//     remote: true,
//   },
//   {
//     id: "2",
//     email: "email@google.com",
//     name: "Google",
//     logo: "url",
//     sustainabilityScore: 0.7,
//     description: "Come work for us, we fired all the good people.",
//     website: "google.com",
//     role_name: "Junior Software Engineer",
//     inclusivityScore: 0.8,
//     location: "UK",
//     remote: false,
//   },
// ];

// fetch("http://localhost:3000/api/roles")
//   .then((response) => response.json())
//   .then((data) => {
//     roles.value = data;
//   });

const locations = new Set<string>();
const remote = ref(true);
const dialog = ref(false);
const chosenRole = ref<RoleWithCompany | null>(null);

roles.value.forEach((role) => locations.add(role.location));

const selectedLocations = ref<Set<string>>(new Set<string>());

// role to pass to the get request
const role = ref("");

const selectedRoles = computed(() =>
  roles.value.filter((role) => {
    if (
      selectedLocations.value.size == 0 ||
      selectedLocations.value.has(role.location)
    ) {
      if (remote.value || (!remote.value && !role.remote)) {
        return role;
      }
    }
  })
);
</script>

<template>
  <v-dialog v-model="dialog">
    <div class="flex justify-center items-center">
      <div class="bg-white rounded p-5">
        <div class="text-xl font-bold">{{ chosenRole!.company.name }}</div>
        <div>{{ chosenRole!.company.description }}</div>
        <div class="font-bold">{{ chosenRole!.name }}</div>
        <div>{{ chosenRole!.remote ? "Is remote" : "Is not remote" }}</div>
      </div>
    </div>
  </v-dialog>

  <div class="flex grow justify-between">
    <div class="bg-[#1a1c23] w-96 text-white">
      <div class="px-2 text-lg font-bold">Locations</div>
      <div class="flex flex-col items-center">
        <div
          v-for="l in locations"
          class="w-full p-2 hover:bg-[#121317]"
          :class="{ 'bg-[#243]': selectedLocations.has(l) }"
          @click="
            () =>
              selectedLocations.has(l)
                ? selectedLocations.delete(l)
                : selectedLocations.add(l)
          "
        >
          {{ l }}
        </div>
      </div>
      <div class="text-white flex items-center justify-between p-2">
        Show remote locations
        <Switch
          v-model="remote"
          :class="remote ? 'bg-purple-300' : 'bg-purple-200'"
          class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
        >
          <span
            :class="remote ? 'translate-x-[25px]' : 'translate-x-1'"
            class="translate-y-[2.8px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
          />
        </Switch>
      </div>
    </div>
    <div class="flex flex-col items-center grow">
      <!-- Main part of the website -->
      <div class="w-3/5 m-2 p-4 rounded-lg">
        <label class="sr-only">Search</label>
        <input
          id="search"
          v-model="role"
          class="relative block w-full appearance-none rounded-lg border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
          placeholder="Search your dream job..."
        />
      </div>
      <div
        v-for="r in selectedRoles"
        class="w-4/5 shadow-lg flex justify-between bg-[#1a1c23] text-white m-2 p-5 rounded-lg"
        @click="
          () => {
            dialog = true;
            chosenRole = r;
          }
        "
      >
        <div class="flex flex-col justify-around">
          <div class="font-bold text-xl">{{ r.name }}</div>
          <div class="text-sm">{{ r.description }}</div>
        </div>
        <div class="flex gap-5 text-center">
          <div>
            <div>Sustainability Score:</div>
            <PieChart :p="r.company.sustainabilityScore * 100" />
          </div>
          <div>
            <div>Inclusivity Score:</div>
            <PieChart :p="r.company.inclusivityScore * 100" />
          </div>
        </div>
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
