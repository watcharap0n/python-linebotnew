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
                        color="red lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                    >
                      Days/Products/Channels
                    </v-btn>
                  </template>

                  <v-card>
                    <v-card-title class="headline grey lighten-2">
                      Days/Products/Channels
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
                                  label="Multiple picker in menu"
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
                      <v-row>
                        <v-col cols="6">
                          <v-select
                              v-model="formProduct"
                              :items="products"
                              label="Product"
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
                              :items="channels"
                              label="Channel"
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
                        color="red lighten-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                    >
                      Month
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


      <div>
        <v-data-table
            :loading="!spinChart"
            :headers="headers"
            :items="transaction"
            sort-by="calories"
            class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar
                flat
            >
              <v-toolbar-title>My CRUD</v-toolbar-title>
              <v-divider
                  class="mx-4"
                  inset
                  vertical
              ></v-divider>
              <v-spacer></v-spacer>
              <v-dialog
                  v-model="dialog"
                  max-width="500px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      color="primary"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
                  >
                    New Item
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="headline">{{ formTitle }}</span>
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
                              v-model="editedItem.name"
                              label="Dessert name"
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              v-model="editedItem.calories"
                              label="Calories"
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              v-model="editedItem.fat"
                              label="Fat (g)"
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              v-model="editedItem.carbs"
                              label="Carbs (g)"
                          ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                          <v-text-field
                              v-model="editedItem.protein"
                              label="Protein (g)"
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
          <template v-slot:item.actions="{ item }">
            <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
                small
                @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </template>

        </v-data-table>
      </div>
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
              products: [],
              channels: [],
              formProduct: '',
              formChannel: '',
              transaction: [],
              headers: [
                  {text: 'Actions', value: 'actions', sortable: false},
                  {text: 'ชื่อ', value: 'fname'},
                  {text: 'ผลิตภัณฑ์', value: 'product'},
                  {text: 'บริษัท', value: 'company'},
                  {text: 'อีเมล', value: 'email'},
                  {text: 'เบอร์', value: 'tel'},
                  {text: 'วันเวลา', value: 'datetime'},
              ],
              editedItem: {
                  name: '',
                  calories: 0,
                  fat: 0,
                  carbs: 0,
                  protein: 0,
              },
              defaultItem: {
                  name: '',
                  calories: 0,
                  fat: 0,
                  carbs: 0,
                  protein: 0,
              },
          }),
          created() {
              this.createTable()
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
                          this.products = res.data.products
                          this.channels = res.data.channels
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
                  let _json = {'dates': this.dates, 'product': this.formProduct, 'channel': this.formChannel}
                  this.postSorting(_json)
                  this.dialogCustoms = false
              },
              sortMonth() {
                  _json = {'month': this.month}
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
              getTable() {
                  this.spinChart = false
                  const path = '/return_sort_table'
                  axios.get(path)
                      .then((res) => {
                          let transaction = this.transaction = res.data.ms
                          console.log(transaction)
                      })
                      .catch((err) => {
                          console.error(err)
                      })
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