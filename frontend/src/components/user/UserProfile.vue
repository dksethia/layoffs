<script setup lang="ts">
import { ref } from 'vue';



const user = {
    id: "3",
    firstName: "Lorenzo",
    lastName: "Von Matterhorn",
    email: "lorenzo@hotmail.com",
    formerCompany: "Google",
    formerRole: "Owner",
    experience: 27,
    linkedin: "lorenzo.linkedin.com",
    password: "ichack",
    profileSummary: "An ex CS Oxford student who got laid off from Google :(",
    location: "UK",
    remote: true,
    sustainable: true,
    gender: "male",
    race: "white",
    isDisabled: true,
}


// // Fetching the data in real time
// const user = ref(null)
// fetch("http://localhost:3000/api/user")
//     .then((response) => response.json())
//     .then((data) => {
//         user.value = data;
//     });

</script>
<template>
    <v-avatar image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"></v-avatar>
    <div>
        <div>{{ user.firstName }}</div>
        <div>{{ user.lastName }}</div>   
    </div>
    <div>{{ user.email }}</div><div>{{ user.linkedin }}</div>
    <div>Previous company:{{ user.formerCompany }} </div>
    <div>Most recent role: {{ user.formerRole }}</div>
    <div>Lives in: {{ user.location }}</div> 
    <div>Open for remote working: {{ (user.remote) ? "Yes!" : "Unfortunately not" }}</div>
</template>