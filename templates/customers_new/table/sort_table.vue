{% extends "customers_new/layout.html" %}
{% block content %}

  <br><br><br>
  <div id="app">
    <v-app id="inspire" class="fixed-nav sticky-footer bg-gray-200">
      <v-card
          elevation="5"
          shaped
          class="mx-auto my-12"
          max-width="800"
      >
        <v-card-title>กรุณาเลือกวันเดือนปีหรือผลิตภัณฑ์ และช่องทางที่ท่านต้องการ</v-card-title>
        <v-card-text>

          <v-row>
            <v-col cols="6">
              <div class="text-center">
                <v-dialog
                    v-model="dialogCustoms"
                    width="500"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                        color="pink lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                    >
                      <v-icon>
                        mdi-calendar-multiselect
                      </v-icon>
                    </v-btn>
                  </template>

                  <v-card>
                    <v-card-title class="headline grey lighten-2">
                      Days/Product/Channel/Tags
                    </v-card-title>

                    <v-card-text>

                      <v-row>
                        <v-col cols="12">
                          <v-menu
                              ref="menu"
                              v-model="menu"
                              :close-on-content-click="false"
                              :return-value.sync="dates"
                              transition="scale-transition"
                              offset-y
                              min-width="290px"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-combobox
                                  v-model="dates"
                                  multiple
                                  chips
                                  small-chips
                                  label="เลือกในแต่ละวัน"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                              ></v-combobox>
                            </template>
                            <v-date-picker
                                v-model="dates"
                                multiple
                                no-title
                                scrollable
                            >
                              <v-spacer></v-spacer>
                              <v-btn
                                  text
                                  color="primary"
                                  @click="menu = false"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menu.save(dates)"
                              >
                                OK
                              </v-btn>
                            </v-date-picker>
                          </v-menu>
                        </v-col>
                      </v-row>
                      <div>
                        <v-combobox
                            prepend-icon="mdi-tag"
                            v-model="tagsSelect"
                            :items="filter_tags"
                            label="เลือกแท็ก"
                            multiple
                            chips
                            small-chips
                        ></v-combobox>
                      </div>
                      <v-row style="margin-top: 8px">
                        <v-col cols="6">
                          <v-select
                              v-model="formProduct"
                              :items="filter_products"
                              label="ผลิตภัณฑ์"
                              menu-props="auto"
                              outlined
                              dense
                              clearable
                          >
                          </v-select>
                        </v-col>
                        <v-col cols="6">
                          <v-select
                              v-model="formChannel"
                              :items="filter_channels"
                              label="ช่องทาง"
                              menu-props="auto"
                              outlined
                              dense
                              clearable
                          >
                          </v-select>
                        </v-col>
                      </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="primary"
                          text
                          @click="dialogCustoms = false"
                      >
                        ยกเลิก
                      </v-btn>
                      <v-btn
                          color="primary"
                          text
                          @click="sortDate"
                      >
                        ตกลง
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </v-col>


            <v-col cols="6">
              <div class="text-center">
                <v-dialog
                    v-model="dialogMonth"
                    width="500"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                        color="pink lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                    >
                      <v-icon>
                        mdi-calendar-month
                      </v-icon>
                    </v-btn>
                  </template>

                  <v-card>
                    <v-card-title class="headline grey lighten-2">
                      Month
                    </v-card-title>

                    <v-card-text>
                      <v-row>
                        <v-col cols="12">
                          <v-menu
                              ref="menuMonth"
                              v-model="menuMonth"
                              :close-on-content-click="false"
                              :return-value.sync="month"
                              transition="scale-transition"
                              offset-y
                              max-width="290px"
                              min-width="290px"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-combobox
                                  v-model="month"
                                  multiple
                                  chips
                                  small-chips
                                  label="Multiple picker in menu"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                              ></v-combobox>
                            </template>
                            <v-date-picker
                                v-model="month"
                                type="month"
                                no-title
                                scrollable
                                multiple
                            >
                              <v-spacer></v-spacer>
                              <v-btn
                                  text
                                  color="primary"
                                  @click="menuMonth = false"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menuMonth.save(month)"
                              >
                                OK
                              </v-btn>
                            </v-date-picker>
                          </v-menu>
                        </v-col>

                      </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="primary"
                          text
                          @click="dialogMonth = false"
                      >
                        ยกเลิก
                      </v-btn>
                      <v-btn
                          color="primary"
                          text
                          @click="sortMonth"
                      >
                        ตกลง
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </v-col>
          </v-row>

        </v-card-text>
        <v-card-actions>

        </v-card-actions>
      </v-card>


      <v-container>
        <v-data-table
            :loading="!spinChart"
            :headers="headers"
            :items="transaction"
            sort-by="calories"
            class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar>
              <v-tabs
                  dark
                  background-color="success">
                <v-tab>
                  <v-badge
                      color="blue"
                      :content="transaction.length">
                    ข้อมูลลูกค้า
                  </v-badge>
                </v-tab>


                <v-spacer></v-spacer>
              </v-tabs>
            </v-toolbar>
            <v-toolbar
                flat
            >
              <v-toolbar-title>Dynamic Table</v-toolbar-title>
              <v-divider
                  class="mx-4"
                  inset
                  vertical
              ></v-divider>
              <v-spacer></v-spacer>
              <v-dialog
                  v-model="dialog"
                  max-width="800px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      disabled
                      color="success"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
                  >
                    เพิ่มข้อมูล
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="headline">[[formTitle]]</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-account"
                              v-model="editedItem.fname"
                              label="ชื่อ"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-post-outline"
                              v-model="editedItem.product"
                              label="ผลิตภัณฑ์"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-office-building"
                              v-model="editedItem.company"
                              label="บริษัท"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-email"
                              v-model="editedItem.email"
                              label="อีเมล"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-card-account-phone"
                              v-model="editedItem.tel"
                              label="เบอร์"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              prepend-inner-icon="mdi-access-point-check"
                              v-model="editedItem.channel"
                              label="ช่องทาง"
                              outlined
                              dense
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="close"
                    >
                      Cancel
                    </v-btn>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="save"
                    >
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                    <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.channel="{ item }">
            <v-chip
                class="ma-2"
                color="green"
                text-color="white"
                v-if="item.channel === 'LINE'"
            >
              [[item.channel]]
            </v-chip>
            <v-chip
                class="ma-2"
                color="primary"
                text-color="white"
                v-else-if="item.channel === 'GetDemo'"
            >
              [[item.channel]]
            </v-chip>
            <v-chip
                class="ma-2"
                color="secondary"
                text-color="white"
                v-else-if="item.channel === 'Contact'"
            >
              [[item.channel]]
            </v-chip>
            <v-chip
                class="ma-2"
                color="orange"
                text-color="white"
                v-else
            >
              [[item.channel]]
            </v-chip>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon
                disabled
                small
                class="mr-2"
                @click="editItem(item)"
                disable
            >
              mdi-pencil
            </v-icon>
            <v-icon
                disabled
                small
                @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </template>

        </v-data-table>
      </v-container>
    </v-app>
  </div>


  <script>
      new Vue({
          el: '#app',
          vuetify: new Vuetify(),
          data: () => ({
              spinChart: true,
              dialog: false,
              dialogDelete: false,
              editedIndex: -1,
              menu: false,
              dates: [],
              month: [],
              menuMonth: false,
              dialogCustoms: false,
              dialogMonth: false,
              showTable: false,
              filter_products: [],
              filter_channels: [],
              filter_tags: [],
              formProduct: '',
              formChannel: '',
              tagsSelect: [],
              transaction: [],
              headers: [
                  {text: 'Actions', value: 'actions', sortable: false},
                  {text: 'แท็ก', value: 'tag'},
                  {text: 'ชื่อ', value: 'name'},
                  {text: 'ผลิตภัณฑ์', value: 'product'},
                  {text: 'บริษัท', value: 'company'},
                  {text: 'อีเมล', value: 'email'},
                  {text: 'เบอร์', value: 'tel'},
                  {text: 'ช่องทาง', value: 'channel'},
                  {text: 'วันเวลา', value: 'datetime'},
              ],
              editedItem: {
                  id: '',
                  name: '',
                  product: '',
                  company: '',
                  email: '',
                  tel: '',
                  channel: '',
              },
              defaultItem: {
                  id: '',
                  name: '',
                  product: '',
                  company: '',
                  email: '',
                  tel: '',
                  channel: '',
              },
          }),
          created() {
              this.createTable()
              this.getTableStart()
          },
          computed: {
              formTitle() {
                  return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
              },
          },
          watch: {
              dialog(val) {
                  val || this.close()
              },
              dialogDelete(val) {
                  val || this.closeDelete()
              },
              transaction: 'showData',
          },
          methods: {
              createTable() {
                  const path = '/json_datetime'
                  axios.get(path)
                      .then((res) => {
                          this.filter_products = res.data.products
                          this.filter_channels = res.data.channels
                          this.filter_tags = res.data.tags
                      })
                      .catch((err) => {
                          console.error(err)
                      })
              },
              showData() {
                  if (this.transaction) {
                      this.spinChart = true
                  }
              },
              sortDate() {
                  let _json = {
                      'dates': this.dates,
                      'product': this.formProduct,
                      'channel': this.formChannel,
                      'tag': this.tagsSelect
                  }
                  this.postSorting(_json)
                  this.dialogCustoms = false
              },
              sortMonth() {
                  _json = {'months': this.month}
                  this.postMonth(_json)
                  this.dialogMonth = false
              },
              postSorting(data) {
                  const path = '/return_sort_table'
                  axios.post(path, data)
                      .then(() => {
                          this.getTable()
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error)
                      })
              },
              postMonth(data) {
                  const path = '/data_month';
                  axios.post(path, data)
                      .then(() => {
                          this.getMonths()
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              getTable() {
                  this.spinChart = false
                  const path = '/return_sort_table'
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((err) => {
                          console.error(err)
                      })
              },
              getTableStart() {
                  this.spinChart = false
                  const path = '/json_datetime';
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              getMonths() {
                  this.spinChart = false
                  const path = '/data_month';
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              editItem(item) {
                  this.editedIndex = this.transaction.indexOf(item)
                  this.editedItem = Object.assign({}, item)
                  this.dialog = true
              },

              deleteItem(item) {
                  this.editedIndex = this.transaction.indexOf(item)
                  this.editedItem = Object.assign({}, item)
                  this.dialogDelete = true
              },

              deleteItemConfirm() {
                  this.transaction.splice(this.editedIndex, 1)
                  this.closeDelete()
              },

              close() {
                  this.dialog = false
                  this.$nextTick(() => {
                      this.editedItem = Object.assign({}, this.defaultItem)
                      this.editedIndex = -1
                  })
              },

              closeDelete() {
                  this.dialogDelete = false
                  this.$nextTick(() => {
                      this.editedItem = Object.assign({}, this.defaultItem)
                      this.editedIndex = -1
                  })
              },

              save() {
                  if (this.editedIndex > -1) {
                      Object.assign(this.transaction[this.editedIndex], this.editedItem)
                  } else {
                      this.transaction.push(this.editedItem)
                  }
                  this.close()
              },
          },
          delimiters: ["[[", "]]"],
      })
  </script>


  <style>
      #spinner {
          position: fixed;
          top: 50%;
          left: 50%;
          color: darkblue;
      }

      #spinChar {
          color: darkblue;
      }


      .custom-loader {
          animation: loader 1s infinite;
          display: flex;
      }

      @-moz-keyframes loader {
          from {
              transform: rotate(0);
          }
          to {
              transform: rotate(360deg);
          }
      }

      @-webkit-keyframes loader {
          from {
              transform: rotate(0);
          }
          to {
              transform: rotate(360deg);
          }
      }

      @-o-keyframes loader {
          from {
              transform: rotate(0);
          }
          to {
              transform: rotate(360deg);
          }
      }

      @keyframes loader {
          from {
              transform: rotate(0);
          }
          to {
              transform: rotate(360deg);
          }
      }


  </style>

{% endblock %}