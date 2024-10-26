<template>
    <v-container>
      <v-card>
        <v-card-title>{{ user.username }}</v-card-title>
        <v-card-text>
          <p>Roles: {{ user.roles.join(', ') }}</p>
          <p>Timezone: {{ user.preferences.timezone }}</p>
          <p>Is Active: {{ user.active ? 'Yes' : 'No' }}</p>
          <p>Created At: {{ new Date(user.created_ts).toLocaleString() }}</p>
          <v-btn @click="openEditModal" color="blue">Edit</v-btn>
          <v-btn @click="confirmDelete" color="red">Delete</v-btn>
        </v-card-text>
      </v-card>
      <UserModal :user="user" :showDialog="showModal" @close="closeModal" />
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  import UserModal from '../components/UserModal.vue';
  
  export default {
    components: {
      UserModal,
    },
    data() {
      return {
        user: {},
        showModal: false,
      };
    },
    mounted() {
      this.fetchUser();
    },
    methods: {
      async fetchUser() {
        const userId = this.$route.params.id;
        const response = await axios.get(`http://localhost:5000/users/${userId}`);
        this.user = response.data;
      },
      openEditModal() {
        this.showModal = true; // Abre o modal
      },
      async confirmDelete() {
        if (confirm(`Are you sure you want to delete ${this.user.username}?`)) {
          await axios.delete(`http://localhost:5000/users/${this.user._id}`);
          this.$router.push('/'); // Redireciona para a lista de usuários após a exclusão
        }
      },
      closeModal() {
        this.showModal = false; // Fecha o modal
        this.fetchUser(); // Atualiza as informações do usuário
      },
    },
  };
  </script>
  