<template>
  <div class="text-center">
    <v-dialog
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" density="compact" icon="mdi-plus"></v-btn>
        </div>
      </template>
      <v-card>
        <v-card-title>
          Создать пользователя
        </v-card-title>
        <v-card-item>
          <v-text-field label="ФИО" v-model="localData.fullName"></v-text-field>
          <v-select
              label="Гендер"
              v-model="localData.gender"
              :items="['Муж.', 'Жен.', 'Неопределеный']"
          ></v-select>
          <v-text-field label="Телефон" v-model="localData.telephone"></v-text-field>
          <v-text-field label="Снилс" v-model="localData.snils"></v-text-field>
        </v-card-item>
        <v-card-actions>
          <v-btn @click="createPatient">Создать пациента</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "CreatePatientDialog",
  data() {
    return {
      dialog: false,
      localData: {
        id: '',
        fullName: '',
        birthDay: '',
        gender: '',
        telephone: '',
        snils: ''
      }
    }
  },
  methods: {
    createPatient() {
      
    }
  } 
}
</script>

<style scoped>

</style>