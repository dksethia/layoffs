import { ref, computed } from "vue";
import { defineStore } from "pinia";
import type { Company } from "@/types/Company";
import type { Role } from "@/types/Role";

export const useCompanyStore = defineStore("company", () => {
  const company = ref<Company | null>(null);

  function getCompany(companyID: string) {
    // fetch company from backend
    company.value = {
      id: "1",
      logoUrl: "logourl",
      name:"Example Company",
      email: "example@example.com",
      recruited: 10,
      sustainabilityScore: 50,
      inclusivityScore: 60,
      description: "description",
      website: "website",
    };
  }

  function getRoles() {
    // fetch jobs for company
    return [
      { id: "1", name: "Machine Learning Engineer", location: "Berlin" },
      { id: "2", name: "Product Manager", location: "Berlin" },
      { id: "3", name: "Senior Software Engineer", location: "London" },
      { id: "4", name: "Cloud Engineer", location: "Birmingham" },
      { id: "5", name: "DevOps Engineer", location: "Bristol" },
    ];
  }

  function addRole(role: Role) {
    console.log(role);
  }

  function getCandidates() {}

  return { company, getCompany, addRole, getCandidates, getRoles };
});
