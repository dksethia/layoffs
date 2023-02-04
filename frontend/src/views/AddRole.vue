<script setup lang="ts">
import { ref } from 'vue';
import { useCompanyStore } from '@/stores/company';

const companyStore = useCompanyStore()

const name = ref("")
const link = ref("")
const location = ref("")
const remote = ref(false)
const hybrid = ref(false)
const description = ref("")

function submitForm() {
    companyStore.addRole({
        name: name.value,
        link: link.value,
        location: location.value,
        remote: remote.value,
        hybrid: hybrid.value,
        description: description.value,
    })
}
</script>

<template>
  <div>
    <div class="px-16 py-4 md:grid md:grid-cols-3 md:gap-6">
      <div class="md:col-span-1">
        <div class="px-4 py-4 sm:px-0">
          <h3 class="text-xl font-medium leading-6 text-gray-900">Add a new role</h3>
          <p class="mt-1 text-sm text-gray-600"></p>
        </div>
      </div>
      <div class="mt-5 md:col-span-2 md:mt-0">
          <div class="shadow sm:overflow-hidden sm:rounded-md">
            <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
              <div class="grid grid-cols-3 gap-6">
                <div class="col-span-6 sm:col-span-3">
                  <label for="name" class="block text-sm font-medium text-gray-700">Title</label>
                  <input type="text" name="name" id="name" autocomplete="given-name" v-model="name" class="px-3 py-2 mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
                </div>
              </div>

              <div class="col-span-3 sm:col-span-2">
                  <label for="link" class="block text-sm font-medium text-gray-700">Link</label>
                  <div class="mt-1 flex rounded-md shadow-sm">
                    <span class="inline-flex items-center rounded-l-md border border-r-0 border-gray-300 bg-gray-50 px-3 text-sm text-gray-500">http://</span>
                    <input type="text" name="link" id="link" v-model="link" class="px-3 py-2 block w-full flex-1 rounded-none rounded-r-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="" />
                  </div>
              </div>
              
              <div class="col-span-6 sm:col-span-3">
                  <label for="location" class="block text-sm font-medium text-gray-700">Location</label>
                  <select id="location" name="location" autocomplete="country-name" v-model="location" class="px-3 py-2 mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm">
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
              </div>

              <div>
                <label for="description" class="block text-sm font-medium text-gray-700">Role Description</label>
                <div class="mt-1">
                  <textarea id="description" name="description" rows="10" class="px-3 py-2 t-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
                </div>
                <p class="mt-2 text-sm text-gray-500"></p>
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 text-right sm:px-6">
              <button type="submit" @click="submitForm" class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Submit</button>
            </div>
          </div>
      </div>
    </div>
  </div>

  <div class="hidden sm:block" aria-hidden="true">
    <div class="py-5">
      <div class="border-t border-gray-200" />
    </div>
  </div>
</template>