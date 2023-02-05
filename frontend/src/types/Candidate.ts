export interface Candidate {
    id: string,
    firstName: string,
    lastName: string,
    email: string,
    formerCompany: string,
    formerRole: string,
    experience: number,
    linkedin: string,
}

export interface CandidateDB extends Candidate {
    password: string,
    profileSummary: string,
    location: string,
    remote: boolean,
    sustainable: boolean,
    gender: string,
    race: string,
    isDisabled: boolean,
}