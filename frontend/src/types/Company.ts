import type { RoleDB } from "./Role";

export interface Company {
  address: string,
  company_id: string,
  contact: string,
  name: string,
  email: string,
  recruited: number,
  sustainability_score: number,
  diversity_inclusive: number,
  description: string,
  website_link: string,
  logoUrl: string,
  
}