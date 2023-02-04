import { ref, computed } from "vue";
import { defineStore } from "pinia";
import type { Company } from "@/types/Company";
import type { Role } from "@/types/Role";

export const useCompanyStore = defineStore("company", () => {
  const company = ref<Company | null>(null);

  function getCompany(companyID: string) {
    // fetch company from backend
    company.value = {roles: [
      {id: "1", name:"Frontend Developer"},
      {id: "2", name:"Backend Developer"}
    ]};
  }

  function addRole(role: Role) {
    console.log(role)
  }

  function getCandidates() {}

  return { company, getCompany, addRole, getCandidates };
});
