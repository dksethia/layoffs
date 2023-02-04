import type { RoleDB } from "./Role";

export interface Company {
  id: string,
  logoUrl: string,
  email: string,
  recruited: number,
  sustainabilityScore: number,
  inclusivityScore: number,
  description: string,
  website: string,
}