<script setup lang="ts">
import { computed, ref } from "vue";
import { Switch } from "@headlessui/vue";
import PieChart from "../components/PieChart.vue";
import type { RoleWithCompany } from "@/types/Role";
import { stringifyExpression } from "@vue/compiler-core";
import { useAuthStore } from "@/stores/auth";
import { useUserStore } from "@/stores/user";
import Heart from "../assets/Heart.vue"
import HeartEmpty from "../assets/HeartEmpty.vue"

const user = useUserStore().user;

const userId = user!.id;

// role to pass to the get request
const role = ref(user!.formerRole);
const roles = ref<RoleWithCompany[]>([])
const locations = new Set<string>();

function fetchRoles() {
  roles.value = []
  fetch(`/api/user_query/${role}`)
    .then((response) => response.json())
    .then((data) => {
      const response = data.response
      response.forEach((obj: { role: any; company: any; }) => {
        const role = obj.role;
        role.company = obj.company;
        role.company.diversity_inclusive = Math.round(Math.random() * 100)
        console.log(role);
        roles.value.push(role);
        locations.add(role.location)
      })
    });
}

fetchRoles()

  
// [
//   {
//     company: {
//       id: "1234",
//       name: "YouTube",
//       email: "email@yt.com",
//       recruited: 90,
//       sustainability_score: 0.9,
//       diversity_inclusive: 0.5,
//       description:
//         "An amazing company where you can help build the website for watching cat videos.",
//       website: "youtube.com",
//       logoUrl: "url",
//     },
//     role_id: "1234",
//     companyId: "1234",
//     name: "Software Engineer",
//     location: "US",
//     remote: true,
//     description:
//       "Role description description description description description description description description",
//       list_people_interested_in_role: ["123", "456"],
//   },
// ]);



const remote = ref(true);
const dialog = ref(false);
const chosenRole = ref<RoleWithCompany | null>(null);

const selectedLocations = ref<Set<string>>(new Set<string>());

const selectedRoles = computed(() => 
  roles.value.filter((role) => {
    if (
      selectedLocations.value.size == 0 ||
      selectedLocations.value.has(role.location)
    ) {
      if (remote.value || (!remote.value && !role.remote)) {
        console.log("something")
        return role;
      }
    }
  })
);

// add the user to interested users for a role

function addIntrested(rId: string, uId: string) {
    // PUT userId to the list of interested people
  const requestOptions = {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ roleId: rId, userId: uId })
  };
  fetch("https://reqres.in/api/articles/1", requestOptions)
    .then(response => response.json())
    .then(data => (
        roles.value.forEach((role) => {
            if (role.role_id == rId) role.  list_people_interested_in_role = data
        })
    ));
}


const liked = ref(new Set())



</script>

<template>
  <v-dialog v-model="dialog">
    <div class="flex justify-center items-center">
      <div class="bg-white rounded p-10 w-3/5 ">
        <div class="flex flex-row mb-5">
          <div class="flex flex-row w-11/12">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 fill-purple-300">
              <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 00.75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 00-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0112 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 01-.673-.38m0 0A2.18 2.18 0 013 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 013.413-.387m7.5 0V5.25A2.25 2.25 0 0013.5 3h-3a2.25 2.25 0 00-2.25 2.25v.894m7.5 0a48.667 48.667 0 00-7.5 0M12 12.75h.008v.008H12v-.008z" />
            </svg>
            <div class="flex text-xl uppercase font-bold ml-5 ">{{ chosenRole!.company.name }}</div>
          </div>
        <button class="flex w-1/12" @click="dialog = false">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 stroke-purple-300">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        </div>
        <div>{{ chosenRole!.company.description }}</div>
        <div class="flex flex-column my-5">
          <div class="font-bold w-9/12">Role: {{ chosenRole!.name }}</div>
          <div class="flex w-3/12 text-gray-500">{{ chosenRole!.remote ? "Available remote" : "Not available remote" }}</div>
        </div>
        <div>{{ chosenRole!.description }}</div>
      </div>
    </div>
  </v-dialog>

  <div class="flex grow justify-between">
    <div class="bg-[#1a1c23] min-w-fit text-white">
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
          {{ l.split(";")[0] }}
        </div>
      </div>
      <div class="text-white flex items-center justify-between p-2 gap-8">
        Show remote locations
        <Switch
          @keyup.enter="remote = !remote"
          v-model="remote"
          :class="remote ? 'bg-purple-300' : 'bg-purple-200'"
          class="relative inline-flex h-8 w-14 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out mr-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
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
      <div class="flex justify-center w-3/5 m-2 p-4 rounded-lg">
        <label class="sr-only">Search</label>
        <input
          id="search"
          v-model="role"
          class="min-w-fit w-80 relative block appearance-none rounded-lg border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
          placeholder="Search your dream job..."
          @keyup.enter="() => fetchRoles()"
        />
      </div>
      <div
        v-for="r in selectedRoles"
        class="w-9/10 flex justify-between text-white my-2 p-5"
      >
        <div class="flex items-center px-5 pl-10 ">
            <label title="Let the company know that you're interested in this position!">
            <HeartEmpty 
                v-if="!liked.has(r.role_id)" @click="
                () => {
                    liked.add(r.role_id);
                }
                "/>
            <Heart v-if="liked.has(r.role_id)" @click="
                () => {
                    liked.delete(r.role_id);
                }
                "
            />
            </label>
        </div>
        <div 
            class="rounded-lg shadow-lg justify-around bg-[#1a1c23] mr-4 p-4 cursor-pointer h-60 overflow-hidden w-4/12"
            @click="
            () => {
                dialog = true;
                chosenRole = r;
            }
            "
        >
          <div class="font-bold my-2 text-xl">{{ r.name }}</div>
          <div class="text-sm">{{ r.description }}</div>
        </div>
        <div
          class="rounded-lg shadow-lg justify-around bg-[#1a1c23] p-4 h-60 overflow-hidden w-4/12"
        >
          <div class="font-bold my-2 text-xl">{{ r.company.name }}</div>
          <div class="text-sm">{{ r.company.description }}</div>
        </div>
        <div class="flex justify-around gap-5 pt-10 text-center bg-[#1a1c23] p-4 rounded-lg mr-12 h-60 overflow-hidden">
          <div>
            <div>Sustainability Score:</div>
            <PieChart :p="Math.round(r.company.sustainability_score * 10)" />
          </div>
          <div>
            <div>Inclusivity Score:</div>
            <PieChart :p="r.company.diversity_inclusive" />
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
