<script setup lang="ts">
import { ref } from "vue";
import { Switch } from "@headlessui/vue";
const name = ref("");
const email = ref("");
const password = ref("");
const linkedIn = ref("");
const formerCompany = ref("");
const formerRole = ref("");
const gender = ref("");
const location = ref("");
const race = ref("");
const remote = ref(false);
const climate = ref(false);
const isDisabled = ref(false);
const locations = ref([
  "London",
  " Manchester",
  " Birmingham",
  " West Yorkshire",
  " Glasgow",
  " Southampton/Portsmouth",
  " Liverpool",
  " Newcastle upon Tyne",
  " Nottingham",
  " Sheffield",
  " Bristol",
  " Belfast",
  " Brighton-Worthing-Littlehampton",
  " Leicester",
  " Edinburgh",
  " Bournemouth/Poole",
  " Cardiff",
]);
const races = ref(["White", "Black", "Asian", "Hispanic", "Other"]);
const companies = ref(["Apple", "Google", "Microsoft"]);
const roles = ref([
  "Senior Manager IT",
  " Product Manager",
  " Machine Learning Engineer",
  " Data Scientist",
  " Software Engineer",
  " Senior Software Engineer",
  " Software Architect",
  " Operations Engineer",
  " Cloud Engineer",
  " DevOps Engineer",
  " Game Developer",
  " Web Developer",
]);
const genders = ref(["Male", "Female", "Other"]);
</script>

<template>
  <div
    class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8 text-black"
  >
    <div class="w-full max-w-md space-y-8">
      <div>
        <h2
          class="mt-6 text-center text-3xl font-bold tracking-tight text-white"
        >
          User Sign up
        </h2>
        <h2 class="text-center text-2xl font-bold tracking-tight text-white">
          First we need a few details
        </h2>
      </div>
      <input type="hidden" name="remember" value="true" />
      <div class="-space-y-px rounded-md shadow-sm">
        <div>
          <input
            v-model="name"
            class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="Name"
          />
        </div>
        <div>
          <input
            v-model="email"
            type="email"
            class="relative block w-full appearance-none rounded-none-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="Email address"
          />
        </div>
        <div>
          <input
            v-model="password"
            type="password"
            class="relative block w-full appearance-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="Password"
          />
        </div>
        <div>
          <input
            v-model="linkedIn"
            class="relative block w-full appearance-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="LinkedIn Profile URL"
          />
        </div>
        <div>
          <select
            v-model="formerCompany"
            class="relative block w-full rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
          >
            <option value="">Please select your Former Company</option>
            <option v-for="c in companies" :value="c">{{ c }}</option>
          </select>
        </div>
        <div>
          <select
            v-model="formerRole"
            class="relative block w-full rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
          >
            <option value="">Please select your Former Role</option>
            <option v-for="r in roles" :value="r">{{ r }}</option>
          </select>
        </div>
        <div>
          <select
            v-model="race"
            class="relative block w-full rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
          >
            <option value="">Please select your Race</option>
            <option v-for="r in races" :value="r">{{ r }}</option>
          </select>
        </div>
        <div>
          <select
            v-model="gender"
            class="relative block w-full rounded-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
          >
            <option value="">Please select your Gender</option>
            <option v-for="g in genders" :value="g">{{ g }}</option>
          </select>
        </div>
        <div>
          <select
            v-model="location"
            class="relative block w-full rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
          >
            <option value="">Please select your City</option>
            <option v-for="l in locations" :value="l">{{ l }}</option>
          </select>
        </div>
        <div class="gap-4 text-white flex items-center justify-between p-2">
          Do you mind working Remotely?
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
          Do you care about the Climate?
          <Switch
            v-model="climate"
            :class="climate ? 'bg-purple-500' : 'bg-purple-300'"
            class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
          >
            <span
              :class="climate ? 'translate-x-[25px]' : 'translate-x-1'"
              class="translate-y-[2.8px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
            />
          </Switch>
        </div>
        <div class="text-white flex items-center justify-between p-2">
          Do you have a Disablilty?
          <Switch
            v-model="isDisabled"
            :class="isDisabled ? 'bg-purple-500' : 'bg-purple-300'"
            class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
          >
            <span
              :class="isDisabled ? 'translate-x-[25px]' : 'translate-x-1'"
              class="translate-y-[2.8px] pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
            />
          </Switch>
        </div>
      </div>

      <div class="flex items-center justify-between text-white">
        <div class="flex items-center">
          <input
            id="remember-me"
            name="remember-me"
            type="checkbox"
            class="h-4 w-4 rounded border-gray-300 focus:ring-purple-500"
          />
          <label for="remember-me" class="ml-2 block text-sm"
            >Remember me</label
          >
        </div>
      </div>

      <div>
        <button
          class="group relative flex w-full justify-center rounded-md border border-transparent bg-purple-500 py-2 px-4 text-sm font-medium text-white hover:bg-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
        >
          Sign Up
        </button>
      </div>
    </div>
  </div>
</template>
