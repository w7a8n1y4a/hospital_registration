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
          <v-select
              :items="helps.helps"
              item-title="display"
              item-value="item_code"
              label="Вид помощи"
              v-model="helps.item_code"
          >
          </v-select>
        </v-card-item>
        <v-card-item>
          <v-select
              :items="organizations.organizations"
              item-title="display"
              item-value="item_code"
              label="Организация"
              v-model="organizations.item_code"
          >
          </v-select>
        </v-card-item>
        <v-card-item>
          <v-textarea
              v-model="comment"
              counter
              label="Комментарий"
              maxlength="120"
              single-line
          ></v-textarea>
          <div class="bg-red text-center" v-if="comment.length === 0">
            <span>Необходимо заполнить поле</span>
          </div>
        </v-card-item>
        <v-card-item>
          <v-select
              :items="directionType.directionTypes"
              item-title="display"
              item-value="item_code"
              label="Код заболевания"
              v-model="directionType.item_code"
          >
          </v-select>
        </v-card-item>
        <v-card-item>
          <v-select
              :items="diseaseCode.diseaseCodes"
              item-title="display"
              item-value="item_code"
              label="Код заболевания"
              v-model="diseaseCode.item_code"
          >
          </v-select>
        </v-card-item>
        <v-card-actions>
          <v-btn border class="grey-darken-1"  @click="register">Регистрация</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import helps from '../jsons/kindOfHelp.json'
import organizations from '../jsons/organizations.json'
import diseaseCode from '../jsons/diseaseСode.json'
import directionType from '../jsons/directionType.json'

export default {
  name: "PatientRegister",
  data() {
    return {
      dialog: false,
      helps: {
        helps: [],
        item_code: "1",
      },
      organizations: {
        organizations: [],
        item_code: "000252b9-5f04-4f99-bf31-665e4576c38e"
      },
      directionType: {
        directionTypes: [],
        item_code: '1'
      },
      diseaseCode: {
        diseaseCodes: [],
        item_code: '1'
      },

      comment: ''
    }
  },
  created() {
    this.helps.helps = helps.items.slice(0, 100);
    this.helps.helps.forEach(item => {
      item.display = item.attributes.display;
    })

    this.organizations.organizations = organizations.items.slice(0, 100)
    this.organizations.organizations.forEach(item => {
      item.display = item.attributes.display;
    })

    this.directionType.directionTypes = directionType.items.slice(0, 100)
    this.directionType.directionTypes.forEach(item => {
      item.display = item.attributes.display;
    })

    this.diseaseCode.diseaseCodes = diseaseCode.items.slice(0, 100);
    this.diseaseCode.diseaseCodes.forEach(item => {
      item.display = item.attributes.display;
    })
  },
  methods: {
    register() {
      if (this.comment.length === 0)
        return;
    }
  }
}
</script>

<style scoped>

</style>