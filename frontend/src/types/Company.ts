import type { RoleDB } from "./Role";

export interface Company {
  id: string,
  name: string,
  email: string,
  recruited: number,
  sustainabilityScore: number,
  inclusivityScore: number,
  description: string,
  website: string,
  logoUrl: string,
}