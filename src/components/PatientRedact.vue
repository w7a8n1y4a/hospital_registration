<template>
  <div class="text-center">
    <v-dialog
        ref="dialog"
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" style="margin-right: 1vw;" density="compact" icon="mdi-pencil"></v-btn>
        </div>
      </template>

      <v-card style="width: 50vw">
        <v-card-title>
          Редактирование данных пациента
        </v-card-title>
        <v-card-item>
          <div style="display: flex">
            <v-text-field label="Фамилия" v-model="localData.first_name"></v-text-field>
            <v-text-field label="Имя" v-model="localData.second_name"></v-text-field>
            <v-text-field label="Отчество" v-model="localData.patronymic"></v-text-field>
          </div>
          <div class="bg-red text-center" v-if="localData.first_name.length === 0 || localData.second_name === 0 || localData.patronymic.length === 0">
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
          <v-btn border class="grey-darken-1" :disabled="notValid" @click="changeData">Отправить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "PatientDialog",
  props: {
    patient: {
      id: Number,
      first_name: String,
      second_name: String,
      patronymic: String,
      date_of_birth: String,
      gender: String,
      telephone: String,
      snils: String
    }
  },
  mounted() {
    this.localData = {
      ...this.patient
    }
  },
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
        snils: '',
      }
    }
  },
  methods: {
    async changeData() {
      if (this.notValid) {
        return;
      }
      await this.$emit('updatePatient')
      this.dialog = false
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
  },
  watch: {
    ['localData.birthDay']() {
      console.log(this.localData.birthDay)
    }
  }
}
</script>

<style scoped>

</style>