<template>
    <v-container>
      <v-btn @click="openCreateModal" color="primary">Create User</v-btn>
      <v-data-table :headers="headers" :items="users" class="mt-5">
        <template v-slot:[`item.username`]="{ item }">
          <router-link :to="`/users/${item._id}`">{{ item.username }}</router-link>
        </template>
        <template v-slot:[`item.actions`]="{ item }">
          <v-btn @click="openEditModal(item)" color="blue">Edit</v-btn>
          <v-btn @click="confirmDelete(item)" color="red">Delete</v-btn>
        </template>
      </v-data-table>
  
      <v-dialog v-model="showModal" persistent max-width="600px">
        <v-card>
          <v-card-title>{{ selectedUser ? 'Edit User' : 'Create User' }}</v-card-title>
          <v-card-text>
            <v-text-field v-model="form.username" label="Username" required />
            <v-text-field v-model="form.password" label="Password" type="password" required />
            <v-select
              v-model="form.roles"
              :items="['admin', 'manager']"
              label="Roles"
              multiple
              required
            />
            <v-text-field v-model="form.preferences.timezone" label="Timezone" required />
          </v-card-text>
          <v-card-actions>
            <v-btn @click="closeModal">Cancel</v-btn>
            <v-btn @click="handleSave" color="green">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        users: [],
        selectedUser: null,
        showModal: false,
        form: {
          username: '',
          password: '',
          roles: [],
          preferences: { timezone: '' },
        },
        headers: [
          { text: 'Username', value: 'username' },
          { text: 'Roles', value: 'roles' },
          { text: 'Timezone', value: 'preferences.timezone' },
          { text: 'Is Active?', value: 'active' },
          { text: 'Created at', value: 'created_ts' },
          { text: 'Actions', value: 'actions', sortable: false },
        ],
      };
    },
    mounted() {
      this.fetchUsers();
    },
    methods: {
      async fetchUsers() {
        const response = await axios.get('http://localhost:5000/users');
        this.users = response.data;
      },
      openCreateModal() {
        this.selectedUser = null;
        this.form = { username: '', password: '', roles: [], preferences: { timezone: '' } }; 
        this.showModal = true;
      },
      openEditModal(user) {
        this.selectedUser = user; 
        this.form = { ...user }; 
        this.showModal = true;
      },
      async handleSave() {
        try {
          if (this.selectedUser) {
            await axios.put(`http://localhost:5000/users/${this.selectedUser._id}`, this.form);
        } else {
            await axios.post('http://localhost:5000/users', this.form);
        }
          this.closeModal();
        } catch (error) {
          console.error('Error saving user:', error);
        }
      },
      closeModal() {
        this.showModal = false;
        this.fetchUsers();
      },
      async confirmDelete(user) {
        if (confirm(`Are you sure you want to delete ${user.username}?`)) {
          await axios.delete(`http://localhost:5000/users/${user._id}`);
          this.fetchUsers();
        }
      },
    },
  };
  </script>
  