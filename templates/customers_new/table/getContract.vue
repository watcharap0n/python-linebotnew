{% extends "customers_new/layout.html" %}
{% block content %}


  <div id="app">
    <div class="container-fluid" style="margin-top: 30px">

      <div class="card shadow mb-4">
        <div class="card-header py-3">
          <div class="row">
            <div class="col-sm-8">
              <ul class="nav nav-pills" role="tablist">
                <li class="nav-item" style="margin-left: 10px">
                  <a href="/information_v2">
                    <button
                        class="btn btn-outline-success">
                      <i class="fa fa-users"></i>
                      ข้อมูลลูกค้า
                      <span class="badge badge-light">{{ data.amount_information }}</span>
                    </button>
                  </a>
                </li>

                <li class="nav-item" style="margin-left: 10px">
                  <a href="/marketing_import">
                    <button
                        class="btn btn-outline-success">
                      <i class="fa fa-reply"></i>
                      นำเข้า
                      <span class="badge badge-light">{{ data.amount_import }}</span>
                    </button>
                  </a>
                </li>

                <li class="nav-item" style="margin-left: 10px">
                  <a href="/getDemo">
                    <button
                        class="btn btn-outline-success">
                      <i class="fa fa-globe" aria-hidden="true"></i>
                      นัดDemo
                      <span class="badge badge-light">{{ data.amount_getDemo }}</span>
                    </button>
                  </a>
                </li>

                <li class="nav-item" style="margin-left: 10px">
                  <a href="/getContract">
                    <button
                        class="btn btn-outline-success">
                      <i class="fa fa-globe" aria-hidden="true"></i>
                      ติดต่อเรา
                      <span class="badge badge-light">{{ data.amount_getContract }}</span>
                    </button>
                  </a>
                </li>
              </ul>
            </div>

            <div class="col-sm-4" style="text-align: end">
              <div class="align-content-end">
                <a href="/excel_all/getDemo" class="btn btn-outline-success btn-sm">
                  <i class="fa fa-file-excel-o"></i>
                  Export Excel
                </a>

                <button type="button" class="btn btn-outline-danger btn-sm" data-toggle="modal"
                        data-target="#myModal">
                  <i class="fa fa-trash" aria-hidden="true"></i>
                  Remove All
                </button>
                <div class="modal fade" id="myModal">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h4 class="modal-title">Confirm Delete</h4>
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                      </div>
                      <div class="modal-body">
                        Delete all transaction... <br>
                        Are you sure ?
                      </div>
                      <div class="modal-footer">
                        <a {% for d in data.getContract %}
                          href="/delete/{{ d.key }}"
                        {% endfor %} class="btn btn-danger btn">Remove All</a>
                        <button type="button" class="btn btn-danger btn" data-dismiss="modal">Close
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <form action="" method="POST">
          <div class="card-body">
            <div class="tab-content">
              <div id="getDemo" class="tab-pane active">
                <div class="footer">
                  <div class="dropdown btn-group dropright" style="margin-bottom: 15px">
                    <button type="button" class="btn btn-outline-secondary dropdown-toggle"
                            data-toggle="dropdown">
                      Tag Sort
                    </button>
                    <div class="dropdown-menu">
                      <li class="dropdown-header">Select Tag</li>
                      <li class="divider"></li>
                      {% for tag in data.tag %}
                        <a class="dropdown-item">
                          <input class="tag_sort"
                                 type="checkbox"
                                 name="tags"
                                 id="{{ tag }}"
                                 value="{{ tag }}"
                              {% if tag in data %} checked {% endif %}>
                          <label for="{{ tag }}" class="getvalue" data-toggle="{{ tag }}"
                                 title="">
                            {% if tag == '' %}
                              ล้างแท็ก
                            {% endif %}
                            {% if tag == 'CB010' %}
                              รับเหมาสาธารณูปโภค
                            {% endif %}
                            {% if tag == 'CC010' %}
                              รับเหมาก่อสร้างระบบวางท่อ
                            {% endif %}
                            {% if tag == 'CG010' %}
                              งานระบบประกอบอาคาร
                            {% endif %}
                            {% if tag == 'CI010' %}
                              รับเหมาก่อสร้างพลังงานทดแทน
                            {% endif %}
                            {% if tag == 'CJ010' %}
                              รับเหมาก่อสร้างงานอาคาร
                            {% endif %}
                            {% if tag == 'CM010' %}
                              ออกแบบตกแต่ง
                            {% endif %}
                            {% if tag == 'CF010' %}
                              รับเหมาขุดเจาะ
                            {% endif %}
                            {% if tag == 'CP010' %}
                              งานอลูมิเนียม
                            {% endif %}
                            {% if tag == 'CE010' %}
                              ผลิตและติดตั้ง
                            {% endif %}
                            {% if tag == 'CH010' %}
                              งานบริการ
                            {% endif %}
                            {% if tag == 'CK010' %}
                              รับสร้างบ้าน
                            {% endif %}
                            {% if tag == 'CN010' %}
                              ไม่แน่ใจ
                            {% endif %}
                            {% if tag == 'CD010' %}
                              ขาย
                            {% endif %}
                            {% if tag == 'RC010' %}
                              อสังหาฯ
                            {% endif %}
                            {% if tag == 'RA010' %}
                              แนวราบ
                            {% endif %}
                            {% if tag == 'RB010' %}
                              แนวสูง
                            {% endif %}
                          </label>
                        </a>
                      {% endfor %}
                      <div class="dropdown-divider"></div>
                      <button type="submit" name="button_event" style="margin-left: 10px"
                              value="button_tag"
                              class="btn btn-secondary btn-sm">
                        <i class="fas fa-tags"></i>
                        Apply
                      </button>
                    </div>
                  </div>
                </div>


                <div class="table-responsive">
                  <table class="table-hover stripe" style="width:100%" id="getdemoTable">
                    <thead>
                    <tr>
                      <th>
                        <input type="checkbox" name="select" id="select-all-demo">
                      </th>
                      <th>แท็ก</th>
                      <th>ชื่อ</th>
                      <th>ผลิตภัณฑ์</th>
                      <th>บริษัท</th>
                      <th>เบอร์</th>
                      <th>อีเมล</th>
                      <th>ข้อความ</th>
                      <th>วัน/เวลา</th>
                      <th>ช่องทาง</th>
                    </tr>
                    </thead>
                    <tbody>
                    {% for demo in data.getContract[::-1] %}
                      <tr>
                        <td>
                          <div class="form-group">
                            <input type="checkbox"
                                   name="key_getContract"
                                   id="{{ demo.key }}"
                                   value="{{ demo.key }}"
                                {% if demo.key in data.getContract.key %}
                                   checked {% endif %}>
                          </div>
                        </td>
                        <td>
                          {% if 'google' in demo.Company %}
                            <span id="" class="badge badge-secondary Filter_kane CC010">
                                <i class="fas fa-tags"></i>
                                spam
                            </span>
                          {% endif %}
                          {% set notvalue = '' %}
                          {% if notvalue not in demo.tag %}
                            <button type="button" class="btn btn-dark btn-xs"
                                    data-toggle="collapse"
                                    data-target="#liff">
                              <i class="fas fa-tags"></i>
                            </button>
                          {% endif %}
                          <div id="liff" class="collapse">
                            {% for tag in demo.tag %}
                              {% if tag %}

                                <span id="{{ tag }}"
                                      class="badge badge-secondary">
                                        <i class="fas fa-tags"></i>
                                  {% if tag == 'CB010' %}
                                    รับเหมาสาธารณูปโภค
                                  {% elif tag == 'CC010' %}
                                    รับเหมาก่อสร้างระบบวางท่อ
                                  {% elif tag == 'CG010' %}
                                    งานระบบประกอบอาคาร
                                  {% elif tag == 'CI010' %}
                                    รับเหมาก่อสร้างพลังงานทดแทน
                                  {% elif tag == 'CJ010' %}
                                    รับเหมาก่อสร้างงานอาคาร
                                  {% elif tag == 'CM010' %}
                                    ออกแบบ ตกแต่ง
                                  {% elif tag == 'CF010' %}
                                    รับเหมาขุดเจาะ
                                  {% elif tag == 'CP010' %}
                                    งานอลูมิเนียม
                                  {% elif tag == 'CE010' %}
                                    ผลิตและติดตั้ง
                                  {% elif tag == 'CH010' %}
                                    งานบริการ
                                  {% elif tag == 'CK010' %}
                                    รับสร้างบ้าน
                                  {% elif tag == 'CN010' %}
                                    ไม่แน่ใจ
                                  {% elif tag == 'CD010' %}
                                    ขาย
                                  {% elif tag == 'RC010' %}
                                    อสังหาฯ
                                  {% elif tag == 'RA010' %}
                                    แนวราบ
                                  {% elif tag == 'RB010' %}
                                    แนวสูง
                                  {% endif %}
                                </span>

                              {% endif %}
                            {% endfor %}
                          </div>
                        </td>
                        <td>{{ demo.Name }}</td>
                        <td>
                          {% if '-- Products --' in demo.Product %}
                          {% else %}
                          {{ demo.Product }}
                          {% endif %}
                        </td>
                        <td>{{ demo.Company }}</td>
                        <td>{{ demo.tel }}</td>
                        <td>{{ demo.Email }}</td>
                        <td>
                          {% set notvalue = 'None' %}
                          {% if demo.Message %}
                            <button type="button" class="btn btn-primary btn-xs"
                                    data-toggle="collapse"
                                    data-target="#message">
                              <i class="fa fa-commenting-o" aria-hidden="true"></i>
                            </button>
                          {% endif %}
                          <div id="message" class="collapse">
                            {{ demo.Message }}
                          </div>
                        </td>
                        <td>{{ demo.date_time }}</td>
                        <td>{{ demo.Channel }}</td>

                      </tr>
                    {% endfor %}
                    </tbody>
                  </table>


                </div>
                <br>
                <div class="footer">
                  <div class="row" style="margin-left: 15px">
                    <div style="margin-right: 12px">
                      <button type="submit" name="button_event" value="button_insert"
                              class="btn btn-success btn-sm">
                        <i class="fa fa-check-square-o"></i>
                        Insert Index
                      </button>
                    </div>
                    <div style="margin-right: 12px">
                      <button type="submit" name="button_event" value="button_excel"
                              class="btn btn-warning btn-sm">
                        <i class="fa fa-check-square-o"></i>
                        Excel Index
                      </button>
                    </div>
                    <div style="margin-right: 12px">
                      <button type="submit" name="button_event" value="button_delete"
                              class="btn btn-danger btn-sm">
                        <i class="fa fa-check-square-o"></i>
                        Delete Index
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>

    </div>
  </div>


  <script>

      var app = new Vue({
          el: "#app",
          data: {
              message: "Intents New Customer",
              dataset: [],
              textSearch: "",
              editintent: "",
              intname: "",
              inttype: "",
              last_id: 0,
          },
          delimiters: ["[[", "]]"],
          mounted() {
          }
      });


      $(document).ready(function () {
          $('#getdemoTable').DataTable({
              "order": [[0, false]],
              "columnDefs": [{
                  "orderable": false,
                  "targets": 0
              }]
          });
      });

      document.getElementById('select-all-demo').onclick = function () {
          var checkboxes = document.getElementsByName('key_getContract');
          for (var checkbox of checkboxes) {
              checkbox.checked = this.checked;
          }
      }
  </script>



{% endblock %}