<template>
  <div class="text-center">
    <v-dialog
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" style="margin-right: 1vw;" density="compact" icon="mdi-pencil"></v-btn>
        </div>
      </template>

      <v-card>
        <v-card-title>
          Редактирование данных пациента
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
        </v-card-item>
        <v-card-item>
          <v-select
              label="Гендер"
              v-model="localData.gender"
              :items="['Муж.', 'Жен.', 'Неопределеный']"
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
          <v-btn border class="grey-darken-1" :disabled="disable" @click="changeData">Отправить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "PatientDialog",
  props: {
    actionType: String,
    patient: {
      id: Number,
      fullName: String,
      birthDay: Date,
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
    changeData() {
      if (this.localData.fullName.length === 0 || this.localData.telephone.length === 0 || this.localData.snils.length === 0) {
        return;
      }
    }
  },
  computed: {
    disable() {
      return this.localData.fullName.length === 0 || this.localData.telephone.length === 0 || this.localData.snils.length === 0;
    }
  }
}
</script>

<style scoped>

</style>