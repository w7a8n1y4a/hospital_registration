<template>
  <div class="text-center">
    <v-dialog
        v-model="dialog"
        width="auto"
    >
      <template v-slot:activator="{ props }">
        <div>
          <v-btn v-bind="props" style="margin-right: 1vw;" density="compact" icon="mdi-delete"></v-btn>
        </div>
      </template>

      <v-card>
        <v-card-title>
          Удаление пациента
        </v-card-title>
        <v-textarea
            value="Вы действительно хотите удалить удалить пациента"
            counter
            disabled
            maxlength="120"
            single-line
        ></v-textarea>
        <v-card-actions>
          <v-btn border class="grey-darken-1" @click="deletePatient">Удалить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "PatientDelete",
  props: {
    id: Number
  },
  data() {
    return {
      dialog: false,
    }
  },
  methods: {
    async deletePatient() {
      await this.$emit('deletePatient', this.id)
      this.dialog = false
    }
  }
}
</script>

<style scoped>

</style>