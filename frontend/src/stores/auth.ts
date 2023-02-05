import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import { useUserStore } from "./user";
import { useCompanyStore } from "./company";

interface LocalAccount {
  type: "user" | "company";
  ID: string;
}

export const useAuthStore = defineStore("auth", () => {
  const userType = useStorage<string | null>("accountType", null);
  function initAuth() {
    if (!userType.value) {
      return;
    }
    const userObj = JSON.parse(userType.value);
    if (userObj.type == "user") {
      useUserStore().getUser(userObj.ID);
    } else if (userObj.type == "company") {
      useCompanyStore().getCompany();
    }
  }

  function updateUser(account: LocalAccount) {
    userType.value = JSON.stringify(account);
  }

  function isUser() {
    if (!userType) {
      return false;
    }
    const userObj = JSON.parse(userType.value!);
    return userObj.type == 'user';
  }

  function signIn(email:string, password:string, type:string) {
    fetch(`/api/login/${email};${password}`).then(res => res.json()).then(res => {
      if (type == 'user') {
        useUserStore().setUser(res)
        userType.value = JSON.stringify({type, ID: res.id})

      } else {
        // company signin
      }
      }
      )
  }

  function signOut() {
    userType.value = null;
  }

  return { initAuth, userType, updateUser, signOut, isUser, signIn };
});
