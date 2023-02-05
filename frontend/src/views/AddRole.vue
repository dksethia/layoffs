<script setup lang="ts">
import { ref } from "vue";
import { useCompanyStore } from "@/stores/company";
import { Switch } from "@headlessui/vue";
const locations = [
  "London",
  "Manchester",
  "Birmingham",
  "West Yorkshire",
  "Glasgow",
  "Southampton/Portsmouth",
  "Liverpool",
  "Newcastle upon Tyne",
  "Nottingham",
  "Sheffield",
  "Bristol",
  "Belfast",
  "Brighton-Worthing-Littlehampton",
  "Leicester",
  "Edinburgh",
  "Bournemouth/Poole",
  "Cardiff",
];

const companyStore = useCompanyStore();

const name = ref("");
const link = ref("");
const location = ref("");
const remote = ref(false);
const hybrid = ref(false);
const description = ref("");

function submitForm() {
  companyStore.addRole({
    companyId: "117",
    name: name.value,
    location: location.value,
    remote: remote.value,
    description: description.value,
  });
}
</script>

<template>
  <div class="text-black">
    <div class="px-16 py-4 md:grid md:grid-cols-3 md:gap-6">
      <div class="md:col-span-1">
        <div class="pr-4 py-4 sm:px-0">
          <h3 class="text-2xl text-white font-bold leading-6 text-gray-900">
            Add a new role
          </h3>
          <p class="mt-1 text-sm text-gray-600"></p>
        </div>
      </div>
      <div class="mt-5 md:col-span-2 md:mt-0">
        <div class="sm:overflow-hidden sm:rounded-md">
          <div class="space-y-6 px-4 py-5 sm:p-6">
            <div class="grid grid-cols-3 gap-6">
              <div class="col-span-6 sm:col-span-3">
                <input
                  placeholder="Title"
                  type="text"
                  name="name"
                  v-model="name"
                  class="px-3 py-2 mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-purple-300 focus:ring-purple-300 sm:text-sm"
                />
              </div>
            </div>

            <div class="col-span-3 sm:col-span-2">
              <div class="mt-1 flex rounded-md shadow-sm">
                <input
                  type="text"
                  name="link"
                  id="link"
                  v-model="link"
                  class="rounded px-3 py-2 block w-full flex-1 rounded-none rounded-r-md border-gray-300 focus:border-purple-300 focus:ring-purple-300 sm:text-sm"
                  placeholder="Link"
                />
              </div>
            </div>

            <div class="col-span-6 sm:col-span-3">
              <select
                name="location"
                v-model="location"
                class="text-black px-3 py-2 mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-purple-300 focus:outline-none focus:ring-purple-300 sm:text-sm"
              >
                <option value="">Please select a Location</option>
                <option v-for="l in locations">{{ l }}</option>
              </select>
            </div>

            <div class="text-white flex items-center justify-between">
              Remote
              <Switch
                v-model="remote"
                :class="remote ? 'bg-purple-300' : 'bg-purple-200'"
                class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
              >
                <span
                  :class="remote ? 'translate-x-[26px]' : 'translate-x-1'"
                  class="translate-y-[4px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
                />
              </Switch>
            </div>
            <div class="text-white flex items-center justify-between">
              Hybrid
              <Switch
                v-model="hybrid"
                :class="hybrid ? 'bg-purple-300' : 'bg-purple-200'"
                class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
              >
                <span
                  :class="hybrid ? 'translate-x-[26px]' : 'translate-x-1'"
                  class="translate-y-[4px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
                />
              </Switch>
            </div>
            <div>
              <div class="mt-1">
                <textarea
                  placeholder="Role Description"
                  name="description"
                  rows="10"
                  v-model="description"
                  class="px-3 py-2 t-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-purple-300 focus:ring-purple-300 sm:text-sm"
                />
              </div>
              <p class="mt-2 text-sm text-gray-500"></p>
            </div>
          </div>
          <div class="px-4 py-3 text-right sm:px-6">
            <button
              @click="submitForm"
              class="rounded-md bg-purple-300 py-2 px-4 text-sm font-medium text-black shadow-sm hover:bg-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-300 focus:ring-offset-2"
            >
              Create Role
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
