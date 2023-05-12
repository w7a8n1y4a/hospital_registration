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
      <v-card style="width: 50vw">
        <v-card-title>
          Создать пользователя
        </v-card-title>
        <v-card-item>
          <v-text-field label="ФИО" v-model="localData.fullName"></v-text-field>
          <div class="bg-red text-center" v-if="localData.fullName.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-text-field
              type="date"
              label="Дата рождения"
              v-model="localData.birthDay"
          >
          </v-text-field>
          <div class="bg-red text-center" v-if="!localData.birthDay">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-select
              label="Гендер"
              v-model="localData.gender"
              :items="['Муж.', 'Жен.', 'Неопределеный']"
          ></v-select>
          <div class="bg-red text-center" v-if="localData.gender.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-text-field label="Телефон" v-model="localData.telephone"></v-text-field>
          <div class="bg-red text-center" v-if="localData.telephone.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-text-field label="Снилс" v-model="localData.snils"></v-text-field>
          <div class="bg-red text-center" v-if="localData.snils.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-actions>
          <v-btn border @click="createPatient" :disabled="NotValid">Создать пациента</v-btn>
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
        birthDay: '2000-01-01',
        gender: '',
        telephone: '',
        snils: ''
      }
    }
  },
  methods: {
    createPatient() {

    }
  },
  computed: {
    NotValid() {
      return this.localData.fullName.length === 0 || !this.localData.birthDay || this.localData.gender === 0 || this.localData.telephone === 0 || this.localData.snils === 0
    }
  }
}
</script>

<style scoped>

</style>