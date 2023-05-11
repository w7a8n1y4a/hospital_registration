<template>
  <v-app>
    <v-app-bar title="wsdl-app" app/>
    <patient-table></patient-table>
  </v-app>
</template>

<script>
import PatientTable from "@/components/PatientTable";

export default {
  name: 'App',
  components: {PatientTable},
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
