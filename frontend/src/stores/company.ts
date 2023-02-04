import { ref, computed } from "vue";
import { defineStore } from "pinia";
class Company {}
export const useCompanyStore = defineStore("company", () => {
  const company = ref<Company | null>(null);

  function getCompany(companyID: string) {
    // fetch company from backend
    company.value = new Company();
  }
  
  return { company, getCompany };
});
