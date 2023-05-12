<template>
  <div class="text-center">
    <v-dialog
        ref="dialog"
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" density="compact" icon="mdi-plus"></v-btn>
        </div>
      </template>
      <v-card style="width: 50vw">
        <v-card-item>
          <div style="display: flex">
            <v-text-field label="Фамилия" v-model="localData.first_name"></v-text-field>
            <v-text-field label="Имя" v-model="localData.second_name"></v-text-field>
            <v-text-field label="Отчество" v-model="localData.patronymic"></v-text-field>
          </div>
          <div class="bg-red text-center"
               v-if="localData.first_name.length === 0 || localData.second_name.length === 0 || localData.patronymic.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-text-field
              type="date"
              label="Дата рождения"
              v-model="localData.date_of_birth"
          >
          </v-text-field>
        </v-card-item>
        <v-card-item>
          <v-select
              label="Гендер"
              v-model="localData.gender"
              :items="['Муж.', 'Жен.', 'Неопределенный']"
          ></v-select>
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
import httpService from "@/services/HttpService";

export default {
  name: "CreatePatientDialog",
  data() {
    return {
      dialog: false,
      localData: {
        id: 0,
        first_name: '',
        second_name: '',
        patronymic: '',
        date_of_birth: '',
        gender: '',
        telephone: '',
        snils: ''
      }
    }
  },
  methods: {
    async createPatient() {
      if (this.notValid) return

      await httpService.createUser(this.localData);

      await this.$emit('getPatients')
      
      this.dialog = false;
    }
  },
  computed: {
    notValid() {
      return this.localData.first_name.length === 0
          ||
          this.localData.second_name === 0
          ||
          this.localData.patronymic.length === 0
          ||
          this.localData.date_of_birth.length === 0
          ||
          this.localData.telephone.length === 0
          ||
          this.localData.snils.length === 0;
    }
  }
}
</script>

<style scoped>

</style>