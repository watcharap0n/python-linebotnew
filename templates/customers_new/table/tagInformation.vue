{% extends "customers_new/layout.html" %}
{% block content %}



  <div class="container-fluid" style="margin-top: 30px">

    <h1 class="h3 mb-2 text-gray-800">Boardcast</h1>

    <div class="row">
      <div class="col-xl-3 col-sm-6 mb-3">
        <div class="card text-white bg-primary o-hidden h-100">
          <div class="card-body">
            <div class="card-body-icon">
              <i class="fa fa-cog" aria-hidden="true"></i>
            </div>
            <div class="mr-5"><span id="message-count">{{ data.CON }} </span>Construction</div>
          </div>
          <a class="card-footer text-white clearfix small z-1" href="#">
            <span class="float-left">View Details</span>
            <span class="float-right">
                    <i class="fa fa-angle-right"></i>
                  </span>
          </a>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 mb-3">
        <div class="card text-white bg-warning o-hidden h-100">
          <div class="card-body">
            <div class="card-body-icon">
              <i class="fa fa-cog" aria-hidden="true"></i>
            </div>
            <div class="mr-5"><span id="message-count">{{ data.REAL }} </span>Real Estate</div>
          </div>
          <a class="card-footer text-white clearfix small z-1" href="#">
            <span class="float-left">View Details</span>
            <span class="float-right">
                    <i class="fa fa-angle-right"></i>
                  </span>
          </a>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 mb-3">
        <div class="card text-white bg-success o-hidden h-100">
          <div class="card-body">
            <div class="card-body-icon">
              <i class="fa fa-cog" aria-hidden="true"></i>
            </div>
            <div class="mr-5"><span id="order-count">{{ data.PLAN }} </span>Project Planning</div>
          </div>
          <a class="card-footer text-white clearfix small z-1" href="#">
            <span class="float-left">View Details</span>
            <span class="float-right">
                    <i class="fa fa-angle-right"></i>
                  </span>
          </a>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 mb-3">
        <div class="card text-white bg-danger o-hidden h-100">
          <div class="card-body">
            <div class="card-body-icon">
              <i class="fa fa-cog" aria-hidden="true"></i>
            </div>
            <div class="mr-5"><span id="order-count">{{ data.OTHER }} </span>OTHER</div>
          </div>
          <a class="card-footer text-white clearfix small z-1" href="#">
            <span class="float-left">View Details</span>
            <span class="float-right">
                    <i class="fa fa-angle-right"></i>
                  </span>
          </a>
        </div>
      </div>
    </div>

    <div class="card shadow mb-4">
      <div class="card-header py-3">
        <div class="row">
          <div class="col-sm-8">
            <ul class="nav nav-pills" role="tablist">
              <li class="nav-item" style="margin-left: 10px">
                <a href="/marketing_information">
                  <button
                      class="btn btn-outline-success" data-toggle="tooltip"
                      title="New Customers">
                    <i class="fa fa-user" aria-hidden="true"></i>
                    ข้อมูลลูกค้า
                    <span class="badge badge-light">{{ data.amount_information }}</span>
                  </button>
                </a>
              </li>

              <li class="nav-item" style="margin-left: 10px">
                <a href="/marketing_import">
                  <button
                      class="btn btn-outline-success" data-toggle="tooltip"
                      title="New Customers">
                    <i class="fa fa-reply" aria-hidden="true"></i>
                    นำเข้า
                    <span class="badge badge-light">{{ data.amount_import }}</span>
                  </button>
                </a>
              </li>

              <li class="nav-item" style="margin-left: 10px">
                <a href="/getDemo">
                  <button
                      class="btn btn-outline-success" data-toggle="tooltip"
                      title="New Customers">
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
              <a href="/excel_all/information" class="btn btn-outline-success btn-sm">
                <i class="fa fa-file-excel-o"></i>
                Export Excel
              </a>

              <button type="button" class="btn btn-outline-danger btn-sm" data-toggle="modal"
                      data-target="#myModal">
                <i class="fa fa-trash" aria-hidden="true"></i>
                Remove All
              </button>
              <div class="modal" id="myModal">
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
                      <a {% for d in data.information %}
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
            <div id="information" class="tab-pane active">
              <div class="footer">
                <div class="row">
                  <div class="col-sm-4">
                    <div class="dropdown btn-group dropright" style="margin-bottom: 15px">
                      <button type="button" class="btn btn-outline-secondary dropdown-toggle"
                              aria-haspopup="true" aria-expanded="false"
                              data-toggle="dropdown">
                        Tag Sort
                      </button>
                      <div class="dropdown-menu">
                        <div class="form-check">
                          <li class="dropdown-header">ประเภทธรุกิจ</li>
                          <li class="divider"></li>
                          {% for tag in data.tag %}
                            <div class="dropdown-item">
                              <input class="tag_sort"
                                     type="checkbox"
                                     name="tags"
                                     id="{{ tag }}"
                                     value="{{ tag }}"
                                  {% if tag in data %} checked {% endif %}>
                              <label for="{{ tag }}" class="getvalue"
                                     data-toggle="{{ tag }}"
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
                            </div>
                          {% endfor %}
                        </div>
                        <div class="dropdown-divider"></div>

                        <div class="row">

                          <button type="submit" name="button_event"
                                  style="margin-left: 15px"
                                  value="button_tag"
                                  class="btn btn-secondary btn-sm"
                          >
                            <i class="fas fa-tags"></i>
                            Apply
                          </button>


                          <button type="submit" name="button_event"
                                  style="margin-left: 5px"
                                  value="button_sorting"
                                  class="btn btn-secondary btn-sm"
                          >
                            <i class="fa fa-sort-amount-desc" aria-hidden="true"></i>
                            Sorting
                          </button>

                          <button type="submit" name="button_event"
                                  style="margin-left: 5px"
                                  value="button_remove_tag"
                                  class="btn btn-secondary btn-sm"
                          >
                            <i class="fa fa-eraser" aria-hidden="true"></i>
                            Clear
                          </button>

                        </div>
                      </div>
                    </div>
                    <div class="dropdown btn-group dropright" style="margin-bottom: 15px">
                      <button type="button" class="btn btn-outline-secondary dropdown-toggle"
                              aria-haspopup="true" aria-expanded="false"
                              data-toggle="dropdown">
                        <i class="fa fa-columns" aria-hidden="true"></i>
                      </button>
                      <div class="dropdown-menu">
                        <div class="form-check" id="columnshow">
                          <li class="dropdown-header">Select Column</li>
                          <li class="divider"></li>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_tag"
                                   id="col_2" checked="checked" data-column="2">
                            <label>
                              แท็ก
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_fname"
                                   id="col_3" data-column="3" checked="checked">
                            <label>
                              ชื่อ
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_product"
                                   id="col_4" data-column="4" checked="checked">
                            <label>
                              ผลิตภัณฑ์
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_other"
                                   id="col_5" data-column="5">
                            <label>
                              ผลิตภัณฑ์อื่น
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_company"
                                   id="col_6" data-column="6" checked="checked">
                            <label>
                              บริษัท
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_tel"
                                   id="col_7" data-column="7" checked="checked">
                            <label>
                              เบอร์
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_email"
                                   id="col_8" data-column="8" checked="checked">
                            <label>
                              อีเมล
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_LIFF"
                                   id="col_9" data-column="9" checked="checked">
                            <label>
                              อีเมล(ไลน์)
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_message"
                                   id="col_10" data-column="10">
                            <label>
                              ข้อความ
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_profile"
                                   id="col_11" data-column="11">
                            <label>
                              ชื่อโปรไฟล์
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_date"
                                   id="col_12" data-column="12" checked>
                            <label>
                              วัน/เวลา
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_channel"
                                   id="col_13" data-column="13" checked>
                            <label>
                              ช่องทาง
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_username"
                                   id="col_14" data-column="14">
                            <label>
                              นำเข้าโดย
                            </label>
                          </div>
                          <div class="dropdown-item">
                            <input class="check_col" type="checkbox" name="_insert"
                                   id="col_15" data-column="15">
                            <label>
                              วันเวลานำเข้า
                            </label>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="dropdown btn-group dropright" style="margin-bottom: 15px">
                      <button type="button" class="btn btn-outline-secondary dropdown-toggle"
                              aria-haspopup="true" aria-expanded="false"
                              data-toggle="dropdown">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                      </button>
                      <div class="dropdown-menu">
                        <li class="dropdown-header">การติดต่อ</li>
                        <li class="divider"></li>
                        <div class="dropdown-item">
                          <input type="checkbox"
                                 name="infoTag"
                                 id="contracted"
                                 value="contracted">
                          <label for="contracted">
                            ติดต่อแล้ว
                          </label>
                        </div>
                        <div class="dropdown-item">
                          <input type="checkbox"
                                 name="infoTag"
                                 id="nContract"
                                 value="nContract">
                          <label for="nContract">
                            ยังไม่ติดต่อ
                          </label>
                        </div>
                        <li class="dropdown-header">นำข้อมูลเข้า RE</li>
                        <li class="divider"></li>
                        <div class="dropdown-item">
                          <input type="checkbox"
                                 name="infoTag"
                                 id="importRE"
                                 value="importRE">
                          <label for="importRE">
                            ข้อมูลรอบันทึก RE
                          </label>
                        </div>
                        <div class="dropdown-item">
                          <input type="checkbox"
                                 name="infoTag"
                                 id="imported"
                                 value="imported">
                          <label for="imported">
                            บันทึกข้อมูลเข้า RE แล้ว
                          </label>
                        </div>
                        <div class="dropdown-divider"></div>
                        <div class="row">
                          <button type="submit" name="button_event"
                                  style="margin-left: 15px"
                                  value="button_infoTag"
                                  class="btn btn-secondary btn-sm"
                          >
                            <i class="fas fa-tags"></i>
                            Apply
                          </button>
                        </div>
                      </div>
                    </div>
                    <button type="submit" name="button_event" value="button_edit"
                            class="btn btn-sm">
                      <i class="fa fa-edit"></i>
                      แก้ไข
                    </button>
                  </div>
                </div>
              </div>

              <div class="table-responsive">
                <table class="table-hover stripe" style="width:100%" id="informationTable">
                  <thead>
                  <tr>
                    <th>
                      <input type="checkbox" name="select" id="select-all-information">
                    </th>
                    <th data-visible="false">Index</th>
                    <th class="_tag">แท็ก</th>
                    <th class="_fname">ชื่อ</th>
                    <th class="_product">ผลิตภัณฑ์</th>
                    <th class="_other">ผลิตภัณฑ์อื่น</th>
                    <th class="_company">บริษัท</th>
                    <th class="_tel">เบอร์</th>
                    <th class="_email">อีเมล</th>
                    <th class="_LIFF">อีเมล(ไลน์)</th>
                    <th class="_message">ข้อความ</th>
                    <th class="_profile">ชื่อโปรไฟล์</th>
                    <th class="_date">วัน/เวลา</th>
                    <th class="_channel">ช่องทาง</th>
                    <th class="_username">นำเข้าโดย</th>
                    <th class="_insert">วันเวลานำเข้า</th>
                  </tr>
                  </thead>
                  <tbody>
                  {% for info in data.lst %}
                    <tr>
                      <td class="_id">
                        <div class="form-group">
                          <input type="checkbox"
                                 name="key_information"
                                 id="{{ info.key }}"
                                 value="{{ info.key }}"
                              {% if info.key in data.lst.key %}
                                 checked {% endif %}>
                        </div>
                      </td>
                      <td>{{ info.index }}</td>
                      <td class="_tag">
                        {% set notvalue = '' %}
                        {% if notvalue not in info.Tag %}
                          <button type="button" class="btn btn-success btn-xs"
                                  data-toggle="collapse"
                                  data-target="#liff">
                            <i class="fas fa-tags"></i>
                          </button>
                        {% endif %}
                        <div id="liff" class="collapse">
                          {% for tag in info.Tag %}
                            {% if tag %}
                              <a href="{{ tag }}">
                              <span id="{{ tag }}"
                                    class="badge badge-secondary Filter_kane CC010">
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
                                {% elif tag == 'nContract' %}
                                  ยังไม่ติดต่อ
                                {% elif tag == 'contracted' %}
                                  ติดต่อแล้ว
                                {% elif tag == 'importRE' %}
                                  ข้อมูลรอบันทึก RE
                                {% elif tag == 'imported' %}
                                  ข้อมูลบันทึกเข้า RE แล้ว
                                {% endif %}
                              </span>
                              </a>
                            {% endif %}
                          {% endfor %}
                        </div>
                      </td>
                      <td class="_fname">{{ info.Name }}</td>
                      <td class="_product">{{ info.Product }}</td>
                      <td class="_other">{{ info.Other }}</td>
                      <td class="_company">{{ info.Company }}</td>
                      <td class="_tel">{{ info.Tel }}</td>
                      <td class="_email">{{ info.Email }}</td>
                      <td class="_LIFF">{{ info.EmailLiff }}</td>
                      <td class="_message">{% set notvalue = 'None' %}
                        {% if notvalue not in info.Message %}
                          <button type="button" class="btn btn-primary btn-xs"
                                  data-toggle="collapse"
                                  data-target="#message">
                            <i class="fa fa-commenting-o" aria-hidden="true"></i>
                          </button>
                        {% endif %}
                        <div id="message" class="collapse">
                          {{ info.Message }}
                        </div>
                      </td>
                      <td class="_profile">{{ info.Profile }}</td>
                      <td class="_date">{{ info.Date }} {{ info.Time }}</td>
                      <td class="_channel">{{ info.Channel }}</td>
                      <td class="_username">{{ info.Username }}</td>
                      <td class="_insert">{{ info.DateInsert }} {{ info.TimeInsert }}</td>
                    </tr>
                  {% endfor %}
                  </tbody>
                </table>


              </div>
              <br>
              <div class="footer">
                <div class="row" style="margin-left: 15px">
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



  <script>
      $(document).ready(function () {
          var table = $('#informationTable').DataTable({
              "order": [[0, false]],
              "columnDefs": [{
                  "orderable": false,
                  "targets": 0
              }]
          });

      });

      $(".check_col:not(:checked)").each(function () {
          var column = "table ." + $(this).attr("name");
          $(column).hide();
      });

      $(".check_col:checkbox").click(function () {
          var column = "table ." + $(this).attr("name");
          $(column).toggle();
      });


      {#$(".check_col").on('click', function () {#}
      {#    var column = table.column($(this).attr('data-column'));#}
      {#    column.visible(!column.visible());#}
      {#    console.log(column)#}
      {#})
      #}

      {#var check_col = $(".check_col").attr("checked", true).click(function () {#}
      {#    var showColumn = "." + $(this).attr("name");#}
      {#    $(showColumn).toggle();#}
      {#})
      #}



      {#$("other").attr("checked", false).click(function (){#}
      {#    var showColumn = "." + $(this).attr("name");#}
      {#    $(showColumn).toggle();#}
      {#})
      #}
      {#;#}


      ;


      document.getElementById('select-all-information').onclick = function () {
          var checkboxes = document.getElementsByName('key_information');
          for (var checkbox of checkboxes) {
              checkbox.checked = this.checked;
          }
      }
  </script>



{% endblock %}