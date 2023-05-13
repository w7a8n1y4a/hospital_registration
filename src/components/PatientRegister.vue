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
          Регистрация пациента {{ isLoad ? 'Загрузка...' : '' }}
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
          <div class="bg-red text-center" v-if="!validOrganization">
            <span>Не удалось найти организации</span>
          </div>
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
          <v-select
              :items="doctors"
              item-title="full_name"
              v-model="selectedDoctor"
              label="ФИО Врача"
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
              label="Тип направления"
              v-model="directionType.item_code"
          >
          </v-select>
        </v-card-item>
        <v-card-item>
          <v-select
              :items="diagnosticStatus.diagnosticStatus"
              item-title="display"
              item-value="item_code"
              label="Статус диагноза"
              v-model="diagnosticStatus.item_code"
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
          <v-btn border class="grey-darken-1" @click="register" :disabled="notValid || !validOrganization">Регистрация
          </v-btn>
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
import diagnosticStatus from '../jsons/diagnosisStatus.json'
import httpService from "@/services/HttpService";

export default {
  name: "PatientRegister",
  props: {
    userId: Number
  },
  data() {
    return {
      dialog: false,
      isLoad: false,
      errorResult: '',
      responseRegister: null,
      doctors: [
        {
          full_name: 'Родионов Артем Максович'
        },
        {
          full_name: 'Афанасьев Адриан Миронович'
        },
        {
          full_name: 'Зиновьев Иван Проклович'
        },
        {
          full_name: 'Филатов Августин Онисимович'
        }
      ],
      selectedDoctor: 'Родионов Артем Максович',
      //вид помощи
      helps: {
        helps: [],
        item_code: "10",
      },
      //организация
      organizations: {
        organizations: [],
        item_code: "5824ffaf-2daf-48c2-8cda-8f02b9bbb9c7"
      },
      //тип направления
      directionType: {
        directionTypes: [],
        item_code: '1'
      },
      //код болезни
      diseaseCode: {
        diseaseCodes: [],
        item_code: '1'
      },
      //статус диагноза
      diagnosticStatus: {
        diagnosticStatus: [],
        item_code: "1"
      },

      comment: '',
      validOrganization: true,
    }
  },
  created() {
    this.helps.helps = helps.items.slice(0, 100);
    this.helps.helps.forEach(item => {
      item.display = item.attributes.display;
    })

    this.organizations.organizations = organizations.items
    this.organizations.organizations.forEach(item => {
      item.display = item.attributes.display;
    })

    this.directionType.directionTypes = directionType.items
    this.directionType.directionTypes.forEach(item => {
      item.display = item.attributes.display;
    })

    this.diseaseCode.diseaseCodes = diseaseCode.items;
    this.diseaseCode.diseaseCodes.forEach(item => {
      item.display = item.attributes.display;
    })

    this.diagnosticStatus.diagnosticStatus = diagnosticStatus.items
    this.diagnosticStatus.diagnosticStatus.forEach(item => {
      item.display = item.attributes.display
    })
  },
  async mounted() {
    await this.updateOrganization()
  },
  methods: {
    async register() {
      this.isLoad = true
      await httpService.sendAppointment(this.userId, this.directionType.item_code, this.helps.item_code, this.organizations.item_code, this.selectedDoctor)
          .then(response => {
            alert(`code: ${response.data.code} key: ${response.data.key}`)
          })
          .catch(e => this.errorResult = e.message)

      this.isLoad = false
      this.alert = true;
    },
    async updateOrganization() {
      this.isLoad = true
      const organizationsRequest = await httpService.getOrganizations(this.helps.item_code)
      if (organizationsRequest.length === 0) {
        this.validOrganization = false
        this.isLoad = false
        return
      }

      const organizationCodes = organizationsRequest.map(item => item.code)

      this.organizations.organizations = organizations.items
      this.organizations.organizations.forEach(item => {
        item.display = item.attributes.display;
      })

      this.organizations.organizations = this.organizations.organizations.filter(o => organizationCodes.includes(o.item_code))
      this.organizations.item_code = this.organizations.organizations[0].item_code
      this.validOrganization = true;
      this.isLoad = false;
    }
  },
  computed: {
    notValid() {
      return this.comment.length === 0
    }
  },
  watch: {
    async ['helps.item_code']() {
      await this.updateOrganization()
    }
  }
}
</script>

<style scoped>

</style>