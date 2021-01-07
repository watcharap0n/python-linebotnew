{% extends "customers_new/layout.html" %}
{% block content %}

  <br><br><br>
  <div id="app" style="font-family: 'Roboto', sans-serif; margin-left: 20px;">
    <v-app id="inspire" class="fixed-nav sticky-footer bg-gray-200">
      <v-row>
        <v-col cols="5">
          <v-card
              :loading="!spinChart"
              class="rounded-xl"
          >
            <v-card-text>
              <i class="fa fa-bar-chart"></i> Revenue Chart
              <hr>
              <div class="row">
                <div class="col-sm-7 text-center my-auto">
                  <canvas ref="myChart" height="180px"></canvas>
                </div>
                <div class="col-sm-5 text-center my-auto" v-for="d in dataSetData">
                  <v-row>
                    <v-col cols="6">
                      <div>
                        <p style="margin-bottom: -13px; font-size: 14px"><i class="fas fa-stop"
                                                                            style="color: #FF648D"></i>&nbsp;Construction
                        </p>
                        <hr>
                        <p style="margin-top: -13px; font-size: 14px">Product [[d.con]]</p>
                      </div>
                    </v-col>
                    <v-col cols="6">
                      <div>
                        <p style="margin-bottom: -13px; font-size: 14px"><i class="fas fa-stop"
                                                                            style="color: #7364FD"></i>&nbsp;RealEstate
                        </p>
                        <hr>
                        <p style="margin-top: -13px; font-size: 14px">Product [[d.real]]</p>
                      </div>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="6">
                      <div>
                        <p style="margin-bottom: -13px; font-size: 14px"><i class="fas fa-stop"
                                                                            style="color: #F9F33B"></i>&nbsp;Planning
                        </p>
                        <hr>
                        <p style="margin-top: -13px; font-size: 14px">Product [[d.planing]]</p>
                      </div>
                    </v-col>
                    <v-col cols="6">
                      <div>
                        <p style="margin-bottom: -13px; font-size: 14px"><i class="fas fa-stop"
                                                                            style="color: #3BF955"></i>&nbsp;Other
                        </p>
                        <hr>
                        <p style="margin-top: -13px; font-size: 14px">Product [[d.other]]</p>
                      </div>
                    </v-col>
                  </v-row>
                </div>
              </div>
              <br>
            </v-card-text>
          </v-card>

          <br>
          <v-card class="overflow-hidden rounded-xl" elevation="3">
            <v-app-bar
                color="white"
                scroll-target="#scrolling-techniques-7"
            >
              <v-toolbar-title>
                <v-row>
                  <v-col cols="6">
                    <div class="text-center">
                      <v-dialog
                          v-model="sortingDialog"
                          width="500"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                              :loading="!spinDateTime"
                              color="red lighten-2"
                              dark
                              v-bind="attrs"
                              v-on="on"
                          >
                            <v-icon left>
                              mdi-sort-calendar-ascending
                            </v-icon>
                            Sorting
                          </v-btn>
                        </template>

                        <v-card>
                          <v-card-title class="headline grey lighten-2">
                            Select Your BY
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
                                    v-model="selectProduct.product"
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
                                    v-model="selectProduct.channel"
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
                                @click="sortingDialog = false"
                            >
                              Cancel
                            </v-btn>
                            <v-btn
                                color="primary"
                                text
                                @click="sortDate"
                            >
                              Submit
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </div>
                  </v-col>

                  <v-col cols="6">
                    <div class="text-center">
                      <v-dialog
                          v-model="monthDialog"
                          width="500"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                              :loading="!spinDateTime"
                              color="red lighten-2"
                              dark
                              v-bind="attrs"
                              v-on="on"
                          >
                            <v-icon left>
                              mdi-calendar-month
                            </v-icon>
                            Y/M
                          </v-btn>
                        </template>

                        <v-card>
                          <v-card-title class="headline grey lighten-2">
                            Select Month
                          </v-card-title>
                          <v-card-text>
                            <v-row>
                              <v-col cols="12">
                                <v-menu
                                    ref="menuMonth"
                                    v-model="menuMonth"
                                    :close-on-content-click="false"
                                    :return-value.sync="date"
                                    transition="scale-transition"
                                    offset-y
                                    max-width="290px"
                                    min-width="290px"
                                >
                                  <template v-slot:activator="{ on, attrs }">
                                    <v-combobox
                                        v-model="date"
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
                                      v-model="date"
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
                                        @click="$refs.menuMonth.save(date)"
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
                                @click="monthDialog = false"
                            >
                              Cancel
                            </v-btn>
                            <v-btn
                                color="primary"
                                text
                                @click="sortMonth"
                            >
                              Submit
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </div>
                  </v-col>
                </v-row>
              </v-toolbar-title>

              <v-spacer></v-spacer>
              <v-chip
                  class="ma-2"
                  color="green"
                  text-color="white"
                  @click="clickChannel('LINE')"
              >
                <v-avatar
                    left
                    class="green darken-4"
                >
                  [[amount_line]]
                </v-avatar>
                LINE
              </v-chip>

              <v-chip
                  class="ma-2"
                  color="green"
                  text-color="white"
                  @click="clickChannel('GetDemo')"
              >
                <v-avatar
                    left
                    class="green darken-4"
                >
                  [[amount_get_demo]]
                </v-avatar>
                GetDemo
              </v-chip>

              <v-chip
                  class="ma-2"
                  color="green"
                  text-color="white"
                  @click="clickChannel('event Impact')"
              >
                <v-avatar
                    left
                    class="green darken-4"
                >
                  [[amount_other]]
                </v-avatar>
                Other
              </v-chip>
              <v-chip
                  class="ma-2"
                  color="indigo"
                  text-color="white"
                  @click="getDateTime($event)"
              >
                <v-avatar left>
                  <v-icon>mdi-account-circle</v-icon>
                </v-avatar>
                [[ms.length]]
              </v-chip>
            </v-app-bar>
            <v-sheet
                id="scrolling-techniques-7"
                class="overflow-y-auto"
                elevation="3"
                max-height="350px"
                elevate-on-scroll
                style="height: 1500px;"
            >
              <v-container>
                <div v-if="!spinDateTime" style="margin-left: 300px; margin-top: 150px">
                  <i id="spinChar" class="fas fa-spinner fa-spin fa-2x"></i>
                </div>
                <v-expansion-panels popout v-else>
                  <v-expansion-panel
                      v-for="(m,i) in ms"
                      :key="i"
                  >
                    <v-expansion-panel-header>
                      <v-row>
                        <v-col style="margin-top: 10px"
                               cols="3"
                               sm="3"
                               md="3"
                        >
                          <v-menu
                              bottom
                              right
                              transition="scale-transition"
                              origin="top left"
                          >
                            <template v-slot:activator="{ on }">
                              <v-chip
                                  pill
                                  v-on="on"
                              >
                                <v-avatar left>
                                  <v-img :src="m.img"></v-img>
                                </v-avatar>
                                [[m.company]]
                              </v-chip>
                            </template>
                            <v-card width="300">
                              <v-list dark>
                                <v-list-item>
                                  <v-list-item-avatar>
                                    <v-img :src="m.img"></v-img>
                                  </v-list-item-avatar>
                                  <v-list-item-content>
                                    <v-list-item-title>[[m.fname]]
                                    </v-list-item-title>
                                    <v-list-item-subtitle>[[m.company]]
                                    </v-list-item-subtitle>
                                  </v-list-item-content>
                                  <v-list-item-action>
                                    <v-btn
                                        icon
                                        @click="menu = false"
                                    >
                                      <v-icon>mdi-close-circle</v-icon>
                                    </v-btn>
                                  </v-list-item-action>
                                </v-list-item>
                              </v-list>
                              <v-list>
                                <v-list-item @click="() => {}">
                                  <v-list-item-action>
                                    <v-icon>mdi-briefcase</v-icon>
                                  </v-list-item-action>
                                  <v-list-item-subtitle>[[m.email]]
                                  </v-list-item-subtitle>
                                </v-list-item>
                              </v-list>
                            </v-card>
                          </v-menu>
                        </v-col>

                        <v-col cols="3">
                          <v-chip
                              class="ma-2"
                              color="primary lighten-1"
                              text-color="white"
                          >
                            [[m.product]]
                          </v-chip>
                        </v-col>
                        <v-col
                            cols="3"
                            sm="3"
                            md="3"
                        >
                          <v-chip
                              class="ma-2"
                              color="green lighten-1"
                              text-color="white"
                          >
                            [[m.channel]]
                          </v-chip>
                        </v-col>
                        <v-col
                            cols="3"
                            sm="3"
                            md="3"
                        >
                          <v-chip
                              style="margin-top: 10px"
                              color="red lighten-4"
                              class="ml-0 mr-2 black--text"
                              label
                              small
                          >
                            [[m.year]]/[[m.month]]/[[m.day]]
                          </v-chip>
                        </v-col>
                      </v-row>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <p>ชื่อ [[m.fname]]</p>
                      <p v-if="m.message">ข้อความ [[m.message]]</p>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-container>
            </v-sheet>
          </v-card>
        </v-col>
        <v-col cols="7">
          <div class="container-fluid">
            <v-data-table
                v-model="selected"
                :single-select="singleSelect"
                show-select
                height="550"
                :search="search"
                :headers="showHeaders"
                :items="transaction"
                :loading="!spinTable"
                loading-text="Loading... Please wait"
                class="elevation-5 rounded-xl">


              <template v-slot:item.tag="{ item }">
                <div v-if='item.tag'>
                  <v-btn @click="onShowTag"
                         x-small
                         text-color="white"
                  >
                    <v-icon>
                      mdi-label-multiple
                    </v-icon>
                  </v-btn>
                </div>
                <div v-for="tag in item.tag" v-if="showTag === true">
                  <div v-if="tag">
                    <v-chip
                        class="ma-2"
                        color="pink"
                        label
                        small
                        close
                        @click:close="chipRemove(item.tag, item.id)"
                        text-color="white"
                    >
                      <v-icon>
                        mdi-label
                      </v-icon>
                      [[tag]]
                    </v-chip>
                  </div>
                  <div v-else></div>
                </div>
                <div v-else></div>
              </template>

              <template v-slot:item.actions="{ item }">
                <v-icon
                    small
                    class="mr-2"
                    @click="editItem(item)"
                    color="green"
                >
                  mdi-pencil
                </v-icon>
                <v-icon
                    small
                    color="red"
                    @click="deleteItem(item)"
                >
                  mdi-delete
                </v-icon>
              </template>

              <template v-slot:item.channel="{item}">
                <v-chip v-if="item.channel === 'LINE'"
                        color="green"
                        class="text-white"
                >
                  [[item.channel]]
                </v-chip>
                <v-chip v-else-if="item.channel === 'GetDemo'"
                        color="#FF648D"
                        class="text-white"
                >
                  [[item.channel]]
                </v-chip>
                <v-chip v-else
                        color="#F7F77D"
                        class="text-black"
                >
                  [[item.channel]]
                </v-chip>
              </template>

              <template v-slot:item.message="{item}">
                <v-list-group
                    color="#7A8FC0"
                    v-if="item.message"
                    :value="false"
                    prepend-icon="mdi-message"
                >
                  <v-list-item-content>
                    [[item.message]]
                  </v-list-item-content>
                </v-list-group>
                <div v-else></div>
              </template>

              <template v-slot:item.product="{item}">
                <div style="color: #6183D4;">[[item.product]]</div>
              </template>

               <template v-slot:item.datetime="{item}">
                <div style="color: #E9643C;">[[item.datetime]]</div>
              </template>

              <template v-slot:top>
                <v-toolbar flat>
                  <v-tabs
                      dark
                      style="background: linear-gradient(to right , #7C4DFF, #304FFE, #448AFF);">
                    <v-tab>
                      <v-badge
                          color="#FF648D"
                          :content="amountInfo">
                        ข้อมูลลูกค้า
                      </v-badge>
                    </v-tab>

                    <v-tab>
                      <a href="/marketing_import">
                        <v-badge
                            color="#FF648D"
                            :content="amountImport"
                            class="text-white"
                        >
                          นำเข้า
                        </v-badge>
                      </a>
                    </v-tab>

                    <v-tab>
                      <a href="/getDemo">
                        <v-badge
                            class="text-white"
                            :content="amountDemo"
                            color="#FF648D"
                        >
                          นัดDemo
                        </v-badge>
                      </a>
                    </v-tab>
                    <v-tab>
                      <a href="#">
                        <v-badge
                            class="text-white"
                            :content="amountContact"
                            color="#FF648D"
                        >
                          ติดต่อเรา
                        </v-badge>
                      </a>
                    </v-tab>
                    <v-spacer></v-spacer>
                    <div>
                      <v-select v-model="selectedHeaders"
                                style="margin-top: 15px;"
                                :items="headers"
                                dense
                                label="Select Columns"
                                multiple outlined return-object>
                        <template v-slot:selection="{ item, index }">
                          <v-chip v-if="index < 2" small>
                            <span>[[ item.text ]]</span>
                          </v-chip>
                          <span v-if="index === 2"
                                class="white--text caption">(+[[ selectedHeaders.length - 2 ]] others)</span>
                        </template>
                      </v-select>
                    </div>
                  </v-tabs>
                </v-toolbar>

                <v-toolbar flat>
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-dialog
                          v-model="dialogExcel"
                          persistent
                          max-width="290"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                              style="margin-left: 10px"
                              elevation="3"
                              :loading="!spinTable"
                              :disabled="!spinTable"
                              medium
                              small
                              v-bind="attrs"
                              v-on="on"
                              color="#FF648D"
                              @click="excelIndex(selected)"
                              class="text-white"
                          >
                            <i class="fa fa-file-excel-o" aria-hidden="true"></i>
                          </v-btn>
                        </template>
                        <v-card>
                          <v-card-title class="headline">
                            ดาวโหลดไฟล์ Excel
                          </v-card-title>
                          <v-card-text v-for="(i, x) in selected" :key="x">
                            ลำดับ : [[x + 1]] ชื่อ : [[i.name]]
                          </v-card-text>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="red"
                                text
                                @click="dialogExcel = false"
                            >
                              ยกเลิก
                            </v-btn>
                            <form method="post">
                              <v-btn
                                  color="green darken-1"
                                  text
                                  type="submit"
                                  :disabled="!exD"
                                  @click="dialogExcel = false"
                              >
                                ตกลง
                              </v-btn>
                            </form>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </template>
                  </v-tooltip>


                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                          style="margin-left: 10px"
                          elevation="3"
                          :loading="!spinTable"
                          :disabled="!spinTable"
                          medium
                          small
                          v-bind="attrs"
                          v-on="on"
                          color="#FF648D"
                          class="text-white"
                          @click="sortIndex(selected)"
                      ><i class="fas fa-user-tag"></i>
                      </v-btn>
                    </template>
                    <span>ติดแท็ก</span>
                    <template v-slot:loader>
                      <span class="custom-loader">
                        <v-icon light>mdi-cached</v-icon>
                      </span>
                    </template>
                  </v-tooltip>

                  <v-dialog
                      v-model="dialogCustoms"
                      width="500"
                      persistent
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
                                ref="tableMenu"
                                v-model="tableMenu"
                                :close-on-content-click="false"
                                :return-value.sync="table_dates"
                                transition="scale-transition"
                                offset-y
                                min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-combobox
                                    v-model="table_dates"
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
                                  v-model="table_dates"
                                  multiple
                                  no-title
                                  scrollable
                              >
                                <v-spacer></v-spacer>
                                <v-btn
                                    text
                                    color="primary"
                                    @click="tableMenu = false"
                                >
                                  Cancel
                                </v-btn>
                                <v-btn
                                    text
                                    color="primary"
                                    @click="$refs.tableMenu.save(table_dates)"
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
                      [[formProduct]]
                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="red"
                            text
                            @click="dialogCustoms = false"
                        >
                          ยกเลิก
                        </v-btn>
                        <v-btn
                            color="primary"
                            text
                            @click="tableSortDate"
                        >
                          ตกลง
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>


                  <v-dialog
                      v-model="dialogMonth"
                      width="500"
                      persistent
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
                                ref="tableMenuMonth"
                                v-model="tableMenuMonth"
                                :close-on-content-click="false"
                                :return-value.sync="table_month"
                                transition="scale-transition"
                                offset-y
                                max-width="290px"
                                min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-combobox
                                    v-model="table_month"
                                    multiple
                                    chips
                                    small-chips
                                    label="เลือกเดือน"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                ></v-combobox>
                              </template>
                              <v-date-picker
                                  v-model="table_month"
                                  type="month"
                                  no-title
                                  scrollable
                                  multiple
                              >
                                <v-spacer></v-spacer>
                                <v-btn
                                    text
                                    color="primary"
                                    @click="tableMenuMonth = false"
                                >
                                  Cancel
                                </v-btn>
                                <v-btn
                                    text
                                    color="primary"
                                    @click="$refs.tableMenuMonth.save(table_month)"
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
                            color="red"
                            text
                            @click="dialogMonth = false"
                        >
                          ยกเลิก
                        </v-btn>
                        <v-btn
                            color="primary"
                            text
                            @click="tableSortMonth"
                        >
                          ตกลง
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>


                  <v-col cols="2" style="margin-top: 30px">
                    <v-select
                        :loading="!spinTable"
                        :items="productMango"
                        label="Product"
                        v-model="search"
                        menu-props="auto"
                        outlined
                        dense
                        clearable
                    >
                    </v-select>
                  </v-col>
                  {#
{#          <v-switch#}
                  {#              #}
                  {# v-model="singleSelect" #}
                  {# label="Single select" #}
                  {# class="pa-3" #}
                  {#></v-switch>
{#          #}
                  <v-spacer></v-spacer>
                  <div class="small" style="margin-left: 10px; margin-top: 23px; margin-right: 20px">
                    <v-combobox
                        :loading="!spinTable"
                        v-model="model"
                        :filter="filter"
                        :hide-no-data="!searchTag"
                        :items="itemsTag"
                        :search-input.sync="searchTag"
                        hide-selected
                        label="แท็ก"
                        multiple
                        dense
                        small-chips

                    >
                      <template v-slot:no-data>
                        <v-list-item>
                          <v-icon color="green">mdi-arrow-right-thick</v-icon>
                          <span class="subheading">สร้าง</span>&nbsp;&nbsp;
                          <v-chip
                              style="color: white"
                              color="pink lighten-2"
                              label
                              small
                          >
                            [[ searchTag ]]
                          </v-chip>
                        </v-list-item>
                      </template>
                      <template v-slot:selection="{ attrs, item, parent, selected, index}">
                        <v-chip
                            v-if="index < 1"
                            v-if="item === Object(item)"
                            v-bind="attrs"
                            color="pink lighten-2"
                            :input-value="selected"
                            label
                            small
                            close
                            close-icon="mdi-delete"
                            @click:close="parent.selectItem(item)"
                        >
                      <span class="pr-2" style="color: white">
                        [[ item.text ]]
                      </span>
                        </v-chip>
                        <span v-if="index === 1"
                              class="grey--text caption">(+[[ model.length - 1 ]] แท็กอื่นๆ)
                    </span>
                      </template>

                      <template v-slot:item="{ index, item }">
                        <v-text-field
                            v-if="editingTag === item"
                            v-model="editingTag.text"
                            autofocus
                            flat
                            background-color="transparent"
                            hide-details
                            solo
                            @keyup.enter="edit(index, item)"
                        ></v-text-field>
                        <v-chip
                            v-else
                            color="pink lighten-2"
                            dark
                            label
                            small
                        >
                          [[ item.text ]]
                        </v-chip>
                        <v-spacer></v-spacer>
                        <v-list-item-action @click.stop>
                          <v-row>
                            <v-col>
                              <v-btn
                                  icon
                                  @click.stop.prevent="edit(index, item)"
                              >
                                <v-icon color="teal">[[ editingTag !== item ? 'mdi-pencil' : 'mdi-check' ]]</v-icon>
                              </v-btn>
                            </v-col>
                            <v-col>
                              <v-btn
                                  icon
                                  @click.stop.prevent="toRemove(index, item)"
                              >
                                <v-icon color="red">mdi-delete</v-icon>
                              </v-btn>
                            </v-col>
                          </v-row>
                        </v-list-item-action>
                      </template>
                    </v-combobox>

                  </div>
                  <div class="small">
                    <v-text-field
                        :loading="!spinTable"
                        v-model="search"
                        label="ค้นหา"
                        single-line
                        hide-details
                    ></v-text-field>
                  </div>
                  <v-dialog
                      v-model="dialog"
                      max-width="1000px"
                  >

                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                          :loading="!spinTable"
                          color="#FF648D"
                          style=" margin-left: 10px"
                          dark
                          small
                          elevation="3"
                          v-bind="attrs"
                          v-on="on"
                      >
                        <i class="fa fa-plus" aria-hidden="true"></i>เพิ่มข้อมูล
                      </v-btn>
                    </template>


                    <v-card>
                      <v-card-title>
                        <span class="headline">[[ formTitle ]]</span>
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
                                  v-model="editedItem.name"
                                  label="Name"
                                  outlined
                                  dense
                              ></v-text-field>

                            </v-col>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                              <v-select
                                  prepend-inner-icon="mdi-post-outline"
                                  v-model="editedItem.product"
                                  :items="productMango"
                                  label="Product"
                                  outlined
                                  dense
                              ></v-select>
                            </v-col>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                              <v-select
                                  prepend-inner-icon="mdi-post"
                                  v-model="editedItem.other"
                                  :items="productOther"
                                  label="Product"
                                  outlined
                                  dense
                              ></v-select>
                            </v-col>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                              <v-text-field
                                  prepend-inner-icon="mdi-office-building"
                                  v-model="editedItem.company"
                                  label="Company"
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
                                  label="Tel"
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
                                  label="Email"
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
                                  prepend-inner-icon="mdi-android-messages"
                                  v-model="editedItem.message"
                                  label="Message"
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
                                  label="Channel"
                                  outlined
                                  dense
                              ></v-text-field>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                              <v-autocomplete
                                  prepend-inner-icon="mdi-tag"
                                  v-model="editedItem.tag"
                                  :items="itemsTag"
                                  outlined
                                  dense
                                  chips
                                  small-chips
                                  label="Tags"
                                  multiple
                              ></v-autocomplete>
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
                      <v-card-title class="headline">Are you sure you want to delete this item?
                      </v-card-title>
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
              <template v-slot:no-data>
                <v-btn
                    color="primary"
                    @click="getTableStart"
                >
                  Reset
                </v-btn>
              </template>
            </v-data-table>
          </div>
        </v-col>
      </v-row>
    </v-app>
  </div>


  <script>
      new Vue({
          el: '#app',
          vuetify: new Vuetify(),
          data: () => ({
              dateValid: false,
              productMango: [],
              productOther: ['RealEstate', 'Construction', 'BI Dashboard', 'Project Planning', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP'],
              showSelect: [],
              singleSelect: false,
              selected: [],
              loading: false,
              dialog: false,
              dialogExcel: false,
              dialogDelete: false,
              spinTable: true,
              spinChart: true,
              showTag: false,
              search: '',
              searchProduct: '',
              transaction: [],
              tags: [],
              amountInfo: '',
              amountDemo: '',
              amountImport: '',
              amountContact: '',
              filter_products: [],
              filter_channels: [],
              filter_tags: [],
              editedIndex: -1,
              dates: [],
              date: [],
              products: [],
              channels: [],
              ms: [],
              spinDateTime: true,
              menu: false,
              menuMonth: false,
              sortingDialog: false,
              monthDialog: false,
              amount_line: '',
              amount_get_demo: '',
              amount_other: '',
              amount_contact: '',
              dialogTag: false,
              activator: null,
              attach: null,
              colorsTag: 'pink',
              editingTag: null,
              editingIndexTag: -1,
              itemsTag: [],
              searchTag: null,
              nonce: 1,
              model: [],
              x: 0,
              y: 0,
              tableMenu: false,
              table_dates: [],
              table_month: [],
              tableMenuMonth: false,
              dialogCustoms: false,
              dialogMonth: false,
              showTable: false,
              formProduct: '',
              formChannel: '',
              tagsSelect: [],
              selectProduct: [
                  {
                      product: '',
                      channel: '',
                  }
              ],
              editedItem: {
                  id: '',
                  name: '',
                  tag: [],
                  product: '',
                  email: '',
                  emailliff: '',
                  company: '',
                  tel: '',
                  profile: '',
                  username: '',
                  time: '',
                  date: '',
                  position: '',
                  tax: '',
                  authorized: '',
                  date_insert: '',
                  time_insert: '',
                  channel: '',
                  message: '',
              },
              defaultItem: {
                  id: '',
                  name: '',
                  tag: [],
                  product: '',
                  email: '',
                  emailLiff: '',
                  company: '',
                  tel: '',
                  profile: '',
                  username: '',
                  time: '',
                  date: '',
                  position: '',
                  tax: '',
                  authorized: '',
                  date_insert: '',
                  time_insert: '',
                  channel: '',
                  message: '',
              },
              exD: false,
              dataSetData: [],
              amountCon: '',
              amountReal: '',
              amountPlan: '',
              amountOther: '',
              headers: [],
              selectedHeaders: []
          }),
          computed: {
              formTitle() {
                  return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
              },
              showHeaders() {
                  return this.headers.filter(s => this.selectedHeaders.includes(s));
              },
              headersMap() {
                  return [
                      {text: 'Edit/Delete', value: 'actions', sortable: false},
                      {text: 'แท็ก', value: 'tag'},
                      {text: 'ชื่อ', value: 'name'},
                      {text: 'ผลิตภัณฑ์', value: 'product'},
                      {text: 'อื่นๆ', value: 'other'},
                      {text: 'บริษัท', value: 'company'},
                      {text: 'เบอร์', value: 'tel'},
                      {text: 'อีเมล', value: 'email'},
                      {text: 'อีเมล(ไลน์)', value: 'emailliff'},
                      {text: 'ข้อความ', value: 'message'},
                      {text: 'โปรไฟล์', value: 'profile'},
                      {text: 'วันเวลา', value: 'datetime'},
                      {text: 'ช่องทาง', value: 'channel'},
                      {text: 'คนนำเข้า', value: 'username'},
                      {text: 'วันเวลานำ', value: 'datetime_insert'},
                  ]
              },
              headersDefault() {
                  return [
                      {text: 'Edit/Delete', value: 'actions', sortable: false},
                      {text: 'แท็ก', value: 'tag'},
                      {text: 'ชื่อ', value: 'name'},
                      {text: 'ผลิตภัณฑ์', value: 'product'},
                      {text: 'อื่นๆ', value: 'other'},
                      {text: 'บริษัท', value: 'company'},
                      {text: 'เบอร์', value: 'tel'},
                      {text: 'อีเมล', value: 'email'},
                  ]
              }
          },
          watch: {
              model(val, prev) {
                  if (val.length === prev.length) return
                  this.model = val.map(v => {
                      if (typeof v === 'string') {
                          v = {
                              text: v,
                              color: this.colorsTag
                          }
                          this.addTag(v)
                          this.nonce++
                      }
                      return v
                  })
              },
              dialog(val) {
                  val || this.close()
              },
              dialogDelete(val) {
                  val || this.closeDelete()
              },
              transaction: 'showData',
              dataSetData: 'showChart',
              ms: 'showDateTime'
          },
          created() {
              this.filterTable()
              this.getTableStart();
              this.getTags();
              this.createInformation()
              this.getDateTime()
              this.headers = Object.values(this.headersMap);
              this.selectedHeaders = this.headers;
          },
          mounted: async function () {
              this.dataSetData = await this.getListData();
              console.log("mounted Chart", this.dataSetData);
              this.getDataSet();
              this.buildChart(this.dataSetData);
          },
          methods: {

              getDataSet: function () {
                  console.log("get data sets");
                  console.log(this.dataSetData);
                  this.dataSetData.forEach(data => {
                  })
                  this.amountCon = this.dataSetData.map(function (chartData) {
                      return chartData.con;
                  });
                  this.amountReal = this.dataSetData.map(function (chartData) {
                      return chartData.real;
                  });
                  this.amountPlan = this.dataSetData.map(function (chartData) {
                      return chartData.planing;
                  });
                  this.amountOther = this.dataSetData.map(function (chartData) {
                      return chartData.other;
                  });
              },
              getListData: async function () {
                  this.spinChart = false
                  const {data} = await axios.get(
                      "/json_information"
                  );
                  return data.amountProduct;
              },
              buildChart() {
                  new Chart(this.$refs.myChart, {
                      type: "doughnut",
                      data: {
                          labels: ['Construction', 'RealEstate', 'Planning', 'Other'],
                          datasets: [
                              {
                                  label: 'Product',
                                  data: [this.amountCon, this.amountReal, this.amountPlan, this.amountOther],
                                  backgroundColor: [
                                      'rgba(255,100,141,1)',
                                      '#7364FD',
                                      '#F9F33B',
                                      '#3BF955',
                                  ],
                                  borderColor: [
                                      'rgba(255,100,141,1)',
                                      '#7364FD',
                                      '#F9F33B',
                                      '#3BF955',
                                  ],
                                  borderWidth: 1
                              }
                          ]
                      },
                      options: {}
                  });
              },
              filterTable() {
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
              getTableStart() {
                  this.spinTable = false
                  const path = '/json_datetime';
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              createInformation() {
                  this.spinTable = false
                  const path = '/json_information';
                  axios.get(path)
                      .then((res) => {
                          this.tags = res.data.tags
                          this.amountInfo = res.data.amount_info
                          this.amountImport = res.data.amount_import
                          this.amountDemo = res.data.amount_demo
                          this.amountContact = res.data.amount_contact
                          this.productMango = res.data.products
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              tableSortDate() {
                  if (this.table_dates.length === 0 && this.formProduct === '' && this.formChannel === '') {
                      console.log('error')
                  } else {
                      console.log('ff')
                      let _json = {
                          'dates': this.table_dates,
                          'product': this.formProduct,
                          'channel': this.formChannel,
                          'tag': this.tagsSelect
                      }
                      this.tablePostSorting(_json)
                      this.dialogCustoms = false
                  }
              },
              tableSortMonth() {
                  if (this.table_month.length === 0) {
                      log.error('error')
                  } else {
                      _json = {'months': this.table_month}
                      this.tablePostMonth(_json)
                      this.dialogMonth = false
                  }
              },
              tablePostSorting(data) {
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
              tablePostMonth(data) {
                  const path = '/data_month';
                  axios.post(path, data)
                      .then(() => {
                          this.tableGetMonths()
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              tableGetMonths() {
                  this.spinTable = false
                  const path = '/data_month';
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              getTable() {
                  this.spinTable = false
                  const path = '/return_sort_table'
                  axios.get(path)
                      .then((res) => {
                          this.transaction = res.data.ms
                      })
                      .catch((err) => {
                          console.error(err)
                      })
              },
              onShowTag() {
                  this.showTag = !this.showTag
              },
              chipRemove(remove, id) {
                  let chip = remove.splice(remove.indexOf(remove), 1)
                  this.updateChip(chip, id)
              },
              excelIndex(selected) {
                  if (selected.length === 0) {
                      this.exD = false
                  } else {
                      this.exD = true
                      console.log(selected)
                      key = []
                      selected.forEach((data) => {
                          key.push(data.id)
                      })
                      this.ExcelPush(key)
                      console.log(key)
                  }

              },
              sortIndex(selected) {
                  user = []
                  model = []
                  console.log(this.model)
                  console.log(selected)
                  this.selected.forEach((data) => {
                      user.push(data.id)
                  })
                  this.model.forEach((data) => {
                      model.push(data.text)
                  })
                  group = {'tags': model, 'key': user}
                  console.log(group)
                  this.SortPush(group)
              },
              showData() { // condition
                  if (this.transaction) {
                      this.spinTable = true
                  }
              },
              showChart() {
                  if (this.dataSetData) {
                      this.spinChart = true
                  }
              },
              LoadDataInfo() { //
                  this.spinTable = false;
                  this.getTableStart()
                  console.log(this.spinTable)
              },
              editItem(item) {
                  this.editedIndex = this.transaction.indexOf(item)
                  this.editedItem = Object.assign({}, item)
                  this.dialog = true
                  console.log(this.editedItem)
              },

              deleteItem(item) {
                  this.editedIndex = this.transaction.indexOf(item)
                  this.editedItem = Object.assign({}, item)
                  this.dialogDelete = true
              },

              deleteItemConfirm() {
                  this.transaction.splice(this.editedIndex, 1)
                  this.removeData(this.editedItem.id)
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
                      let payload = Object.assign(this.transaction[this.editedIndex], this.editedItem)
                      this.updateData(payload, payload.id);
                  } else {
                      this.addData(this.editedItem)
                      console.log(this.editedItem)
                  }
                  this.close()
              },
              async ExcelPush(id) {
                  const path = `/excel_information`;
                  await axios.post(path, id)
                      .then(() => {
                          console.log('success');
                          this.getExcel();
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              getExcel() {
                  const path = `/static/excel/testVue.xlsx`;
                  axios.get(path)
                      .then(() => {
                          console.log('success');
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              SortPush(group) {
                  const path = `/tag_information`;
                  axios.post(path, group)
                      .then(() => {
                          this.getTableStart();
                          this.showLog = 'Sorting!';
                          this.showMessage = true;
                      })
                      .catch((error) => {
                          console.error(error);
                          this.getTableStart();
                      });
              },

              updateChip(chip, id) {
                  const path = `/json_chip/${id}`;
                  axios.post(path, chip)
                      .then(() => {
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error);
                      })
              },

              updateData(payload, id) {
                  const path = `/update_information/${id}`;
                  axios.post(path, payload)
                      .then(() => {
                          this.showLog = 'Data updated!';
                          this.showMessage = true;
                      })
                      .catch((error) => {
                          console.error(error);
                          this.getTableStart();
                      });
              },
              removeData(id) {
                  const path = `/delete_information/${id}`;
                  axios.post(path)
                      .then(() => {
                          console.log(path)
                      })
                      .catch((error) => {
                          // eslint-disable-next-line
                          console.error(error);

                      });
              },
              addData(payload) {
                  const path = '/json_information'
                  axios.post(path, payload)
                      .then(() => {
                          console.log(payload)
                          this.getTableStart();
                          this.showMessage = true;
                      })
                      .catch((error) => {
                          console.log(error)
                          this.getTableStart();
                      });
              },
              sortProduct(value) {
                  this.search = value
              },
              showDateTime() {
                  if (this.ms) {
                      this.spinDateTime = true
                  }
              },
              clickChannel(value) {
                  let data = {
                      'channel': value
                  }
                  this.postDateTime(data)
              },
              sortMonth() {
                  let data = {
                      'months': this.date
                  }
                  this.postMonth(data)
                  console.log(data)
                  this.monthDialog = false
              },
              sortDate() {
                  let data = {
                      'product': this.selectProduct.product,
                      'dates': this.dates,
                      'channel': this.selectProduct.channel
                  }
                  console.log('data', data)
                  this.postDateTime(data)
                  this.sortingDialog = false
              },
              getDateTime() {
                  this.spinDateTime = false
                  const path = '/json_datetime';
                  axios.get(path)
                      .then((res) => {
                          this.ms = res.data.ms
                          this.amount_line = res.data.amount_channel.line
                          this.amount_get_demo = res.data.amount_channel.get_demo
                          this.amount_other = res.data.amount_channel.other
                          this.products = res.data.products
                          this.channels = res.data.channels
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              postDateTime(data) {
                  const path = '/json_datetime';
                  axios.post(path, data)
                      .then(() => {
                          console.log('success')
                          this.getSortDate()
                      })
                      .catch((error) => {
                          // eslint-disable-next-line
                          console.error(error);
                      });
              },
              getSortDate() {
                  this.spinDateTime = false
                  const path = '/return_sort'
                  axios.get(path)
                      .then((res) => {
                          this.amount_line = res.data.amount_channel.line
                          this.amount_get_demo = res.data.amount_channel.get_demo
                          this.amount_other = res.data.amount_channel.other
                          this.ms = res.data.ms
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
              getMonths() {
                  this.spinDateTime = false
                  const path = '/data_month';
                  axios.get(path)
                      .then((res) => {
                          this.amount_line = res.data.amount_channel.line
                          this.amount_get_demo = res.data.amount_channel.get_demo
                          this.amount_other = res.data.amount_channel.other
                          let ms = this.ms = res.data.ms
                          console.log('months', ms)
                      })
                      .catch((error) => {
                          console.error(error);
                      });
              },
              edit(index, item) {
                  if (!this.editingTag) {
                      this.editingTag = item
                      this.editingIndexTag = index

                  } else {
                      this.setTag(item.id, this.editingTag)
                      this.editingTag = null
                      this.editingIndexTag = -1
                  }
              },
              toRemove(index, item) {
                  this.itemsTag.splice(this.itemsTag.indexOf(item), 1)
                  this.removeTag({'index': item.id})
              },
              addTag(item) {
                  const path = '/add_tags'
                  axios.post(path, item)
                      .then(() => {
                          this.getTags()
                          console.log('success')
                      })
                      .catch((err) => {
                          console.error(err)
                      })
              },
              setTag(index, item) {
                  const path = `/tags/${index}`;
                  axios.post(path, item)
                      .then(() => {
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error)
                      })
              },
              removeTag(index) {
                  const path = `/tags`;
                  axios.post(path, index)
                      .then(() => {
                          this.getTags()
                          console.log('success')
                      })
                      .catch((error) => {
                          console.error(error)
                      })
              },
              filter(item, queryText, itemText) {
                  const hasValue = val => val != null ? val : ''
                  const text = hasValue(itemText)
                  const query = hasValue(queryText)
                  return text.toString()
                      .toLowerCase()
                      .indexOf(query.toString().toLowerCase()) > -1
              },
              getTags() {
                  const path = '/tags';
                  axios.get(path)
                      .then((res) => {
                          let tags = this.itemsTag = res.data.val_tags;
                          console.log(tags)
                      })
                      .catch((error) => {
                          console.error(error);
                      });
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