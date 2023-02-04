export interface Role {
    name: string,
    location: string,
    remote: boolean,
    description: string,
}

export interface RoleDB extends Role {
    roleId:string;
    companyId:string;
}