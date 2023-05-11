<template>
  <div class="text-center">
    <v-dialog
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" style="margin-right: 1vw;" density="compact" icon="mdi-account"></v-btn>
        </div>
      </template>

      <v-card>
        <v-card-title>
          Регистрация пациента
        </v-card-title>
        <v-card-item>

        </v-card-item>
        <v-card-actions>
          <v-btn @click="register">Регистрация</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "PatientRegister",
  data() {
    return {
      dialog: false,
      kindOfHelp: [],
      organizations: [],
      doctorName: '',
      comment: '',
      id: undefined,
      diseaseCode: undefined
    }
  },
  methods: {
    register() {
      
    }
  }
}
</script>

<style scoped>

</style>