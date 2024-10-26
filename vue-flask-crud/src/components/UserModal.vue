<template>
  <v-dialog :value="showDialog" @input="$emit('update:showDialog', $event)" persistent max-width="600px">
    <v-card>
      <v-card-title>{{ user ? 'Edit User' : 'Create User' }}</v-card-title>
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
        <v-btn @click="close">Cancel</v-btn>
        <v-btn @click="handleSave" color="green">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
  props: ['user', 'showDialog'],
  data() {
    return {
      form: this.user ? { ...this.user } : { username: '', password: '', roles: [], preferences: { timezone: '' } },
    };
  },
  methods: {
    async handleSave() {
      console.log('Save button clicked');
      try {
        if (this.user) {
          await axios.put(`/users/${this.user._id}`, this.form);
        } else {
          await axios.post('/users', this.form);
        }
        this.$emit('close');
        this.$emit('update:showDialog', false);
      } catch (error) {
        console.error('Error saving user:', error);
      }
    },
    close() {
      this.$emit('update:showDialog', false);
      this.$emit('close');
    },
  },
};
</script>
