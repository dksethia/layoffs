<script setup lang="ts">
import { ref } from "vue";

const user = {
  id: "3",
  firstName: "Lorenzo",
  lastName: "Von Matterhorn",
  email: "lorenzo@hotmail.com",
  formerCompany: "Google",
  formerRole: "Software Engineer",
  experience: 27,
  linkedin: "https://www.lorenzo.linkedin.com",
  password: "ichack",
  profileSummary: "An ex CS Oxford student who got laid off from Google :(",
  location: "UK",
  remote: true,
  sustainable: true,
  gender: "male",
  race: "white",
  isDisabled: true,
};
</script>
<template>
  <div class="flex justify-center p-5 gap-5 mx-20">
    <div class="flex flex-col bg-[#1a1c23] p-8 rounded-[40px] shadow-lg">
      <div class="flex justify-center">
        <v-avatar
          size="20em"
          image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
        />
      </div>
      <div>{{ user.firstName.toUpperCase() }}</div>
      <div class="text-2xl font-bold">{{ user.lastName.toUpperCase() }}</div>
      <div class="text-2xl text-[#fff5]">{{ user.gender }}</div>
      <div class="mt-5">
        {{ user.profileSummary }}
      </div>
      <div class="flex justify-around mt-5">
        <a
          :href="user.linkedin"
          target="_blank"
          class="bg-purple-300 hover:bg-purple-200 text-black p-3 rounded"
          >Linked in</a
        >
        <a
          :href="`mailto:${user.email}`"
          class="bg-purple-300 hover:bg-purple-200 text-black p-3 rounded"
          >Email</a
        >
      </div>
    </div>
    <div class="w-1/2 flex flex-col gap-5 justify-between">
      <div class="bg-[#1a1c23] p-8 rounded-[40px] shadow-lg">
        <div class="text-2xl font-bold">Experience</div>
        <div class="my-3">
          <div class="font-bold">Former Company:</div>
          <div>{{ user.formerCompany }}</div>
        </div>
        <div class="mt-3">
          <div class="font-bold">Former Role:</div>
          <div>{{ user.formerRole }}</div>
        </div>
      </div>
      <div class="bg-[#1a1c23] p-8 rounded-[40px] shadow-lg">
        <div class="text-2xl font-bold">Preferences</div>
        <div class="my-3">
          <div class="font-bold">Location:</div>
          <div>{{ user.location }}</div>
        </div>
        <div class="my-3">
          <div class="font-bold">Open for remote working:</div>
          <div>{{ user.remote ? "Yes!" : "Unfortunately not" }}</div>
        </div>
        <div class="my-3">
          <div class="font-bold">Former Company:</div>
          <div>{{ user.formerCompany }}</div>
        </div>
        <div class="mt-3">
          <div class="font-bold">Former Role:</div>
          <div>{{ user.formerRole }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
:deep(input) {
  background: none !important;
}
</style>
