<template>
  <v-container>
    <v-table>
      <thead>
      <tr>
        <th>
          Фамилия
        </th>
        <th>
          Имя
        </th>
        <th>
          Отчество
        </th>
        <th>
          Дата рождения
        </th>
        <th>
          Пол
        </th>
        <th>
          Телефон
        </th>
        <th>
          Снилс
        </th>
        <th>
          <create-patient-dialog
              @createPatient="createPatient"
          />
        </th>
      </tr>
      </thead>
      <tbody>
      <tr
          v-for="item in patients"
          :key="item.id"
      >
        <td class="text-left">{{ item.first_name }}</td>
        <td class="text-left">{{ item.second_name }}</td>
        <td class="text-left">{{ item.patronymic }}</td>
        <td class="text-left">{{ item.date_of_birth }}</td>
        <td class="text-left">{{ item.gender }}</td>
        <td class="text-left">{{ item.telephone }}</td>
        <td class="text-left">{{ item.snils }}</td>
        <td class="text-left" style="display: flex">
          <patient-delete :id="item.id" @deletePatient="deletePatient"/>
          <patient-redact :patient="item" @updatePatient="updatePatient"/>
          <patient-register :userId="item.id"/>
        </td>
      </tr>
      </tbody>
    </v-table>
  </v-container>
</template>

<script>
import PatientRedact from "@/components/PatientRedact";
import CreatePatientDialog from "@/components/CreatePatientDialog";
import PatientRegister from "@/components/PatientRegister";
import PatientDelete from "@/components/PatientDelete";
import httpService from "@/services/HttpService";

export default {
  name: "PatientTable",
  components: {PatientRegister, PatientRedact, CreatePatientDialog, PatientDelete},
  data() {
    return {
      patients: [],
    }
  },
  async mounted() {
    await this.getPatients();
  },
  methods: {
    async getPatients() {
      this.patients = await httpService.getUsers()
    },
    async createPatient(patient) {
      await httpService.createUser(patient)
      await this.getPatients();
    },
    async deletePatient(id) {
      await httpService.deletePatient(id)
      await this.getPatients()
    },
    async updatePatient(patient) {
      await httpService.updatePatient(patient)
      await this.getPatients()
    }
  }
}
</script>

<style scoped>

</style>