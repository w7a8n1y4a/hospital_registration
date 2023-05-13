import axios from 'axios'

export class HttpService {
    baseUrl = 'https://test.pepemoss.com/api/v1/'

    async getUsers() {
        return await axios.get(this.baseUrl + 'users/all')
            .then(response => response.data)
    }

    async createUser(patient) {
        return await axios.post(this.baseUrl + 'users', patient)
    }

    async updatePatient(patient) {
        return await axios.patch(this.baseUrl + 'users', patient)
    }

    async deletePatient(patientId) {
        return await axios.delete(this.baseUrl + `users?user_id=${patientId}`)
    }

    async getOrganizations(code) {
        return await axios.get(this.baseUrl + `appointments?code=${code}`)
            .then(response => response.data)
    }
    
    sendAppointment(user_id, direction_type_code, type_of_assistance, target_organization, doctor_name) {
        return axios.post(this.baseUrl + `appointments`, {
            user_id,
            direction_type_code,
            type_of_assistance,
            target_organization,
            doctor_name
        })
    }
}

export default new HttpService()