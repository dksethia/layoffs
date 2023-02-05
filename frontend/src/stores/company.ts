import { ref, computed } from "vue";
import { defineStore } from "pinia";
import type { Company } from "@/types/Company";
import type { Role } from "@/types/Role";
import RoleCardVue from "@/components/company/RoleCard.vue";

export const useCompanyStore = defineStore("company", () => {
  let companyId = ''

  function getCompany() {
    // fetch company from backend
    // const response = fetch(`/api/get_company/${}`)
    fetch(`/api/user_query/developer`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data.response[0].company.company_id)
      companyId = data.response[0].company.company_id
    });
  }

  const roles = ref<Role[]>([])

  function getRoles() {
    // fetch jobs for company
    fetch(`/api/get_roles/${companyId}`)
    .then((response) => response.json())
    .then((data) => {
      const items = data.items;
      items.forEach((item: { name: string; location: string; remote: boolean; description: string; }) => 
        roles.value.push(item)
      );
    
    return roles.value
  });


    // return [
    //   { id: "1", name: "Machine Learning Engineer", location: "Berlin" },
    //   { id: "2", name: "Product Manager", location: "Berlin" },
    //   { id: "3", name: "Senior Software Engineer", location: "London" },
    //   { id: "4", name: "Cloud Engineer", location: "Birmingham" },
    //   { id: "5", name: "DevOps Engineer", location: "Bristol" },
    // ];
  }

  function getRole(id: string) {
    return {  list_people_interested_in_role: [`${id}`]}
  }

  function addRole(role: Role) {
    console.log(role);
  }

  function getCandidates(roleId: string) {
    return [
      {id: "1", firstName: "David", lastName: "Blaine", email: "dks20@ic.ac.uk", formerCompany: "Google", formerRole:"Backend Developer", experience: 3, linkedin: "https://www.google.com"},
    ]
  }

  return { companyId, getCompany, addRole, getCandidates, getRoles, getRole };
});
