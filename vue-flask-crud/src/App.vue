<template>
  <v-app>
    <v-container fluid>
      <router-view />
    </v-container>
  </v-app>
</template>

<style src="./assets/main.scss" lang="scss"></style>


<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
