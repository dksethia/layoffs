<script setup lang="ts">
import { ref } from "vue";
import UserSignUp from "./SignIn/UserSignUp.vue";
import CompanySignUp from "./SignIn/CompanySignUp.vue";
import UserSignIn from "./SignIn/UserSignIn.vue";
import CompanySignIn from "./SignIn/CompanySignIn.vue";
const accountType = ref<null | string>(null);
const newUser = ref<boolean>(false);
</script>

<template>
  <div
    class="text-white flex flex-col grow bg-[#121317] grow min-h-screen justify-around items-center"
  >
    <div
      v-if="!accountType"
      class="flex flex-col justify-center items-center gap-16"
    >
      <div class="text-5xl">Welcome to BackToBusiness.</div>
      <div class="text-3xl">I am</div>
      <div class="flex justify-around w-screen text-3xl">
        <div
          class="flex flex-col justify-center items-center hover:text-gray-500"
          @click="accountType = 'user'"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-24 h-24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
            />
          </svg>
          <div>Looking for a job</div>
        </div>
        <div
          @click="accountType = 'company'"
          class="flex flex-col justify-center items-center hover:text-gray-500"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-24 h-24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008z"
            />
          </svg>
          <div>Hiring</div>
        </div>
      </div>
    </div>
    <div v-else>
      <UserSignUp v-if="accountType == 'user' && newUser" />
      <CompanySignUp v-else-if="accountType == 'company' && newUser" />
      <UserSignIn v-else-if="accountType == 'user' && !newUser" />
      <CompanySignIn v-else-if="accountType == 'company' && !newUser" />
      <button
        @click="accountType = null"
        class="text-purple-300 hover:text-purple-200"
      >
        Go Back
      </button>
    </div>
    <div
      v-if="accountType"
      class="hover:text-gray-500 my-5"
      @click="newUser = !newUser"
    >
      {{
        newUser
          ? "Already have an account? Login now!"
          : "New to BackToBusiness? Sign up now!"
      }}
    </div>
  </div>
</template>

<style>
input,
textarea,
select {
  background-color: white !important;
}
</style>
