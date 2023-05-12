<template>
  <v-table>
    <thead>
    <tr>
      <th>
        ФИО
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
        <create-patient-dialog/>
      </th>
    </tr>
    </thead>
    <tbody>
    <tr
        v-for="item in patients"
        :key="item.id"
    >
      <td class="text-left">{{ item.fullName }}</td>
      <td class="text-left">{{ item.birthDay }}</td>
      <td class="text-left">{{ item.gender }}</td>
      <td class="text-left">{{ item.telephone }}</td>
      <td class="text-left">{{ item.snils }}</td>
      <td class="text-left" style="display: flex">
        <patient-redact
            action-type="DELETE"
            @deletePatient="deletePatient"
            :patient="item">
          >
        </patient-redact>
<!--        <patient-dialog-->
<!--            action-type="EDIT"-->
<!--            @changePatientData="changePatientData"-->
<!--            :patient="item">-->
<!--        </patient-dialog>-->
        <patient-register>

        </patient-register>
      </td>
    </tr>
    </tbody>
  </v-table>
</template>

<script>
import PatientRedact from "@/components/PatientRedact";
import CreatePatientDialog from "@/components/CreatePatientDialog";
import PatientRegister from "@/components/PatientRegister";

export default {
  name: "PatientTable",
  components: {PatientRegister, PatientRedact, CreatePatientDialog},
  data() {
    return {
      patients: [
        {
          id: 1,
          fullName: 'Кал калыч',
          birthDay: '2023-05-01',
          gender: 'Муж.',
          telephone: '234 234 234',
          snils: '1231 23123 123123'
        },
        {
          id: 2,
          fullName: 'Сем семыч',
          birthDay: '2023-05-01',
          gender: 'Жен.',
          telephone: '3 213 12',
          snils: '1231 1232 123123'
        },
        {
          id: 3,
          fullName: 'Кал калыч',
          birthDay: '2023-05-01',
          gender: 'Муж.',
          telephone: '234 234 234',
          snils: '1231 23123 123123'
        },
        {
          id: 4,
          fullName: 'Сем семыч',
          birthDay: '2023-05-01',
          gender: 'Жен.',
          telephone: '3 213 12',
          snils: '1231 1232 123123'
        },
        {
          id: 5,
          fullName: 'Кал калыч',
          birthDay: '2023-05-01',
          gender: 'Муж.',
          telephone: '234 234 234',
          snils: '1231 23123 123123'
        },
        {
          id: 6,
          fullName: 'Сем семыч',
          birthDay: '2023-05-01',
          gender: 'Жен.',
          telephone: '3 213 12',
          snils: '1231 1232 123123'
        },
      ],
    }
  },
  methods: {
    async changePatientData(value) {

    },
    async deletePatient(value) {

    }
  }
}
</script>

<style scoped>

</style>