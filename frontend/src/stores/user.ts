import { ref, computed } from "vue";
import { defineStore } from "pinia";
class User {}
export const useUserStore = defineStore("user", () => {
  const user = ref<User | null>(null);
  function getUser(userID: string) {
    // fetch user from backend
    user.value = new User();
  }
  return { user, getUser };
});
