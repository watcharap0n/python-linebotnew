{% extends "customers_new/loginLayout.html" %}
{% block content %}


<div id="app">
    <v-app id="inspire">
        <v-container>
            <div class="d-flex flex-column justify-space-between align-center">
                <v-img
                        width="360"
                        src="/static/images/erp_RE.png"
                ></v-img>
            </div>
            <v-row justify="center">
                <v-col
                        cols="12"
                        sm="10"
                        md="8"
                        lg="6"
                >
                    <v-card>
                        <v-form
                                ref="form"
                                v-model="valid"
                                lazy-validation
                        >
                            <v-card-text>
                                <v-text-field
                                        dense
                                        outlined
                                        clearable
                                        v-model="formElement.name"
                                        :rules="validOther"
                                        label="ชื่อผู้ติดต่อ"
                                        required
                                ></v-text-field>

                                <v-text-field
                                        dense
                                        outlined
                                        clearable
                                        v-model="formElement.company"
                                        :rules="validOther"
                                        label="บริษัท"
                                        required
                                ></v-text-field>

                                <v-text-field
                                        dense
                                        outlined
                                        clearable
                                        v-model="formElement.email"
                                        :rules="validEmail"
                                        label="อีเมล"
                                        required
                                ></v-text-field>

                                <v-select
                                        dense
                                        outlined
                                        clearable
                                        v-model="formElement.other"
                                        :items="products"
                                        label="ผลิตภัณฑ์อื่นๆที่ท่านสนใจ"
                                        required
                                ></v-select>


                                <v-text-field
                                        dense
                                        outlined
                                        clearable
                                        v-model="formElement.tel"
                                        :rules="validTel"
                                        label="เบอร์ที่สะดวกให้เจ้าหน้าที่ติดต่อกลับ"
                                        type="tel"
                                        required
                                ></v-text-field>

                                <v-textarea
                                        dense
                                        outlined
                                        v-model="formElement.message"
                                        clearable
                                        autocomplete
                                        label="ข้อมูลที่ท่านต้องการทราบเพิ่มเติม"
                                ></v-textarea>
                                <v-card-actions>
                                    <v-btn block
                                            :disabled="!valid"
                                            color="success"
                                            class="mr-4"
                                            @click="validate"
                                    >
                                        ยืนยัน
                                    </v-btn>
                                    </v-btnblock>
                                </v-card-actions>
                            </v-card-text>
                        </v-form>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</div>


<script>
    new Vue({
        el: '#app',
        vuetify: new Vuetify(),
        data: () => ({
            validCheck: [v => !!v || 'กรุณาคลิกเพื่อไปต่อ'],
            validSelect: [v => !!v || 'กรุณาเลือกผลิตภัณฑ์'],
            validEmail: [
                v => !!v || 'กรุณากรอกอีเมล',
                v => /.+@.+\..+/.test(v) || 'กรุณากรอกอีเมลให้ถูกต้อง',
            ],
            validTel: [
                v => !!v || 'กรุณากรอกเบอร์โทร',
                v => (v && v.length <= 10) || 'เบอร์โทรกรอกไม่ครบ',
            ],
            validOther: [v => !!v || 'กรุณากรอกข้อมูลให้ครบถ้วน'],
            formElement: {
                name: '',
                email: '',
                other: '',
                company: '',
                tel: '',
                message: '',
            },
            valid: false,
            width: '',
            products: ['RealEstate', 'Project Planning', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP']

        }),
        created() {
            liff.init({liffId: "1655208213-bR4352Oe"}, () => {
                if (liff.isLoggedIn()) {

                } else {
                    liff.login();
                }
            }, err => console.error(err.code, error.message));
        },
        methods: {
            validate() {
                let form = this.$refs.form.validate()
                let element = this.formElement
                if (form === true) {
                    liff.getProfile()
                        .then(profile => {
                            let to_dict = {
                                'firstname': element.name,
                                'email': element.email,
                                'company': element.company,
                                'tel': element.tel,
                                'product': 'Real Estates',
                                'other': element.other,
                                'comment': element.message,
                                'userId': profile.userId,
                                'token': liff.getDecodedIDToken().email + ' ',
                                'displayName': profile.displayName,
                                'picture': profile.pictureUrl,
                                'channel': 'LINE',
                            }
                            this.sendPost(to_dict)
                        })
                } else {
                    console.log('error')
                }
            },
            sendPost(value) {
                const path = '/ajax_marketing'
                axios.post(path, value)
                    .then(() => {
                        console.log(value)
                        this.popUp()

                    })
                    .catch((error) => {
                        console.error(error)
                    })
            },
            popUp() {
                 Swal.fire("ข้อมูลบันทึกเรียบร้อย!", "เจ้าหน้าที่ได้รับข้อมูลของท่านแล้ว\nและจะดำเนินการติดต่อกลับให้เร็วที่สุด", "success").then(() => {
                    liff.closeWindow();
                })
            },

        },
        delimiters: ["[[", "]]"],
    })


</script>

{% endblock %}

