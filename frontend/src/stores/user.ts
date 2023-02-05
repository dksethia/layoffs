import { ref } from "vue";
import { defineStore } from "pinia";
import type { CandidateDB } from "@/types/Candidate";
export const useUserStore = defineStore("user", () => {
  const user = ref<CandidateDB | null>(null);
  function setUser(userr:CandidateDB) {
    user.value = userr
  }
  function getUser(userID: string) {
    fetch(`/api/get_user/${userID}`).then(res=>res.json()).then(res => {
      console.log(res);
      user.value = res
    })
  }

  return { user, getUser, setUser };
});
