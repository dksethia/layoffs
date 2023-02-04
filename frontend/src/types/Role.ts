export interface Role {
    name: string,
    link: string,
    location: string,
    remote: boolean,
    hybrid: boolean,
    description: string,
}

export interface RoleDB extends Role {
    id:string;
}