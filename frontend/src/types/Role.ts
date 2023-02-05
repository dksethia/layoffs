import type { Company } from "./Company";

export interface Role {
  name: string;
  location: string;
  remote: boolean;
  description: string;
}

export interface RoleDB extends Role {
  role_id: string;
  companyId: string;
  list_people_interested_in_role: string[];
}

export interface RoleWithCompany extends RoleDB {
  company: Company;
}
