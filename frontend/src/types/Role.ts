import type { Company } from "./Company";

export interface Role {
  name: string;
  location: string;
  remote: boolean;
  description: string;
  interestedPeople: string[];
}

export interface RoleDB extends Role {
  roleId: string;
  companyId: string;
}

export interface RoleWithCompany extends RoleDB {
  company: Company;
}
