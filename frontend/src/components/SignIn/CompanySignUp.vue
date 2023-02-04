<script setup lang="ts">
import { ref } from "vue";
const name = ref("");
const email = ref("");
const password = ref("");
const website = ref("");
const description = ref("");
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
          Company Sign up
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
            placeholder="Company Name"
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
            v-model="website"
            class="relative block w-full appearance-none border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="Website URL"
          />
        </div>
        <div>
          <textarea
            v-model="description"
            class="relative block w-full appearance-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-500 focus:outline-none focus:ring-purple-500 sm:text-sm"
            placeholder="Description"
          />
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
