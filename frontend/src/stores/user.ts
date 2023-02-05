import { ref } from "vue";
import { defineStore } from "pinia";
import type { CandidateDB } from "@/types/Candidate";
class User {}
export const useUserStore = defineStore("user", () => {
  const user = ref<CandidateDB | null>(null);
  function getUser(userID: string) {
    // fetch user from backend
    user.value = {
      id: "123",
      firstName: "Lorenzo",
      lastName: "Von Matterhorn",
      email: "lorenzo@hotmail.com",
      formerCompany: "Google",
      formerRole: "Software Engineer",
      experience: 27,
      linkedin: "lorenzo.linkedin.com",
      password: "ichack",
      profileSummary: "An ex CS Oxford student who got laid off from Google :(",
      location: "UK",
      remote: true,
      sustainable: true,
      gender: "male",
      race: "white",
      isDisabled: true,
  }
  }

  return { user, getUser };
});
