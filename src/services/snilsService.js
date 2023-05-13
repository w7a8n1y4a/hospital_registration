class SnilsService {
    zeros(str, lng) {
        let factlength = str.length;
        if (factlength < lng) {
            for (var i = 0; i < (lng - factlength); i++) {
                str = '0' + str;
            }
        }
        return str;
    }

    snils() {
        let rand1 = this.zeros(String(Math.floor((Math.random() * 998) + 2)), 3);
        let rand2 = this.zeros(String(Math.floor((Math.random() * 999) + 1)), 3);
        let rand3 = this.zeros(String(Math.floor((Math.random() * 999) + 1)), 3);
        let rezult = rand1 + rand2 + rand3;
        let kontr = String(9 * rezult[0] + 8 * rezult[1] + 7 * rezult[2] +
            6 * rezult[3] + 5 * rezult[4] + 4 * rezult[5] +
            3 * rezult[6] + 2 * rezult[7] + 1 * rezult[8]);
        if (kontr < 100) {

        } else if (kontr > 101) {
            kontr = String(kontr % 101);
            kontr = this.zeros(kontr, 2);
            if (kontr > 99) {
                kontr = '00';
            }
        } else {
            kontr = '00';
        }
        rezult = rezult + kontr;
        return rezult;
    }
}

export default new SnilsService()