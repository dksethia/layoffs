<script setup lang="ts">
import { ref } from "vue";
const email = ref("");
const password = ref("");
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
          Company Sign in
        </h2>
      </div>
      <input type="hidden" name="remember" value="true" />
      <div class="-space-y-px rounded-md shadow-sm">
        <div>
          <input
            v-model="email"
            type="email"
            class="relative block w-full appearance-none rounded-none-md rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-300 focus:outline-none focus:ring-purple-300 sm:text-sm"
            placeholder="Email address"
          />
        </div>
        <div>
          <input
            v-model="password"
            type="password"
            class="relative block w-full appearance-none border rounded-b-md border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-purple-300 focus:outline-none focus:ring-purple-300 sm:text-sm"
            placeholder="Password"
          />
        </div>
      </div>

      <div class="flex items-center justify-between text-white gap-4">
        <div class="flex items-center">
          <input
            id="remember-me"
            name="remember-me"
            type="checkbox"
            class="h-4 w-4 rounded border-gray-300 focus:ring-purple-300"
          />
          <label for="remember-me" class="ml-2 block text-sm"
            >Remember me</label
          >
        </div>

        <div class="text-sm">
          <a href="#" class="font-medium text-purple-300 hover:text-purple-200"
            >Forgot your password?</a
          >
        </div>
      </div>

      <div>
        <button
          class="group relative flex w-full justify-center rounded-md border border-transparent bg-purple-300 py-2 px-4 text-sm font-medium hover:bg-purple-200 focus:outline-none focus:ring-2 focus:ring-purple-300 focus:ring-offset-2"
        >
          Sign In
        </button>
      </div>
    </div>
  </div>
</template>
