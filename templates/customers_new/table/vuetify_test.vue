{% extends "customers_new/layout.html" %}
{% block content %}
  <br><br><br>

  <div id="app">
    <v-app id="inspire" class="fixed-nav sticky-footer bg-gray-200">
      <v-container>
        <div class="text-center">
            <v-combobox
                v-model="model"
                :filter="filter"
                :hide-no-data="!searchTag"
                :items="itemsTag"
                :search-input.sync="searchTag"
                hide-selected
                label="เลือกแท็กที่ต้องการ"
                multiple
                small-chips
                solo
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
                    v-if="index < 2"
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
                  <span v-if="index === 2"
                          class="grey--text caption">(+[[ model.length - 2 ]] others)
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
      </v-container>
    </v-app>
  </div>




  <script>

      new Vue({
          el: '#app',
          vuetify: new Vuetify(),
          data: () => ({
              dialogTag: false,
              activator: null,
              attach: null,
              colorsTag: 'pink',
              editingTag: null,
              editingIndexTag: -1,
              itemsTag: [],
              searchTag: null,
              nonce: 1,
              menu: false,
              model: [],
              x: 0,
              y: 0,
          }),

          created() {
              this.getTags();
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
          },
          methods: {
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
          delimiters: ["[[", "]]"]

      })
  </script>


{% endblock %}