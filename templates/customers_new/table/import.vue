{% extends "customers_new/layout.html" %}
{% block content %}

<br><br><br>
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
                    <span class="badge badge-light">{{ data.information }}</span>
                  </button>
                </a>
              </li>

              <li class="nav-item" style="margin-left: 10px">
                <a href="/marketing_import">
                  <button
                      class="btn btn-outline-success active">
                    <i class="fa fa-reply" aria-hidden="true"></i>
                    นำเข้า
                    <span class="badge badge-light">{{ data.amount }}</span>
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
                    <span class="badge badge-light">{{ data.getDemo }}</span>
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
              <a href="/excel_all/import" class="btn btn-outline-success btn-sm">
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
                      <a {% for d in data.imports %}
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
            <div id="import" class="tab-pane active">
              <div class="footer">
                <div class="dropdown btn-group dropright" style="margin-bottom: 15px">
                  <button type="button" class="btn btn-outline-secondary dropdown-toggle"
                          data-toggle="dropdown">
                    Tag Sort
                  </button>
                  <div class="dropdown-menu">
                    <li class="dropdown-header">ประเภทธรุกิจ</li>
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
                            class="btn btn-secondary btn-sm"
                    >
                      <i class="fas fa-tags"></i>
                      Apply
                    </button>
                    <button type="submit" name="button_event"
                            style="margin-left: 10px"
                            value="button_sorting"
                            class="btn btn-secondary btn-sm"
                    >
                      <i class="fa fa-sort-amount-desc" aria-hidden="true"></i>
                      Sorting
                    </button>
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
                        <input class="tag_sort" type="checkbox" name="_tag"
                               id="_tag" checked="checked">
                        <label>
                          แท็ก
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_fname"
                               id="fname" checked="checked">
                        <label>
                          ชื่อ
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_product"
                               id="product" checked="checked">
                        <label>
                          ผลิตภัณฑ์
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_other"
                               id="other">
                        <label>
                          ผลิตภัณฑ์อื่น
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_company"
                               id="company" checked="checked">
                        <label>
                          บริษัท
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_tel"
                               id="tel" checked="checked">
                        <label>
                          เบอร์
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_email"
                               id="email" checked="checked">
                        <label>
                          อีเมล
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_LIFF"
                               id="LIFF" checked="checked">
                        <label>
                          อีเมล(ไลน์)
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_message"
                               id="LIFF" checked="checked">
                        <label>
                          ข้อความ
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_profile"
                               id="profile">
                        <label>
                          ชื่อโปรไฟล์
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_date"
                               id="date" checked>
                        <label>
                          วัน/เวลา
                        </label>
                      </div>
                      <div class="dropdown-item">
                        <input class="tag_sort" type="checkbox" name="_channel"
                               id="channel" checked="checked">
                        <label>
                          ช่องทาง
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
                <button type="submit" name="button_event" value="button_edit"
                        class="btn btn-sm">
                  <i class="fa fa-edit"></i>
                  แก้ไข
                </button>
              </div>


              <div class="table-responsive">
                <table class="table-hover stripe" style="width:100%" id="importTable">
                  <thead>
                  <tr>
                    <th>
                      <input type="checkbox" name="select" id="select-all-import">
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
                  </tr>
                  </thead>
                  <tbody>
                  {% for import in data.imports[::-1] %}
                    <tr>
                      <td>
                        <div class="form-group">
                          <input type="checkbox"
                                 name="key_import"
                                 id="{{ import.key }}"
                                 value="{{ import.key }}"
                              {% if import.key in data.imports.key %} checked {% endif %}>
                        </div>
                      </td>
                      <td>{{ import.index }}</td>
                      <td class="_tag">
                        {% set notvalue = '' %}
                        {% if notvalue not in import.tag %}
                          <button type="button" class="btn btn-dark btn-xs"
                                  data-toggle="collapse"
                                  data-target="#liff">
                            <i class="fas fa-tags"></i>
                          </button>
                        {% endif %}
                        <div id="liff" class="collapse">
                          {% for tag in import.tag %}
                            {% if tag %}
                              <a href="tagImport/{{ tag }}">
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
                                                                  {% endif %}
                                                                </span>
                              </a>
                            {% endif %}
                          {% endfor %}
                        </div>
                      </td>
                      <td class="_fname">{{ import.event.firstname }}</td>
                      <td class="_product">{{ import.event.product }}</td>
                      <td class="_other">{{ import.event.other }}</td>
                      <td class="_company">{{ import.event.company }}</td>
                      <td class="_tel">{{ import.event.tel }}</td>
                      <td class="_email">{{ import.event.email }}</td>
                      <td class="_LIFF">{{ import.event.token }}</td>
                      <td class="_message">
                        {% if import.event.comment %}
                          <button type="button" class="btn btn-primary btn-xs"
                                  data-toggle="collapse"
                                  data-target="#message">
                            <i class="fa fa-commenting-o" aria-hidden="true"></i>
                          </button>
                        {% endif %}
                        <div id="message" class="collapse">
                          {% if import.event.comment %}
                            {{ import.event.comment }}
                          {% endif %}
                        </div>
                      </td>
                      <td class="_profile">{{ import.event.displayName }}</td>
                      <td class="_date">{{ import.day }}/{{ import.month }}/{{ import.year }}
                        {{ import.hour }}:{{ import.min }}:{{ import.sec }}</td>
                      <td class="_channel">{{ import.event.channel }}</td>
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


  <script>
      $(document).ready(function () {
          var dataTable = $('#importTable').DataTable({
              "order": [[0, false]],
              "columnDefs": [{
                  "orderable": false,
                  "targets": 0
              }]
          });


          $(".tag_sort:not(:checked)").each(function () {
              var column = "table ." + $(this).attr("name");
              $(column).hide();
          });

          $(".tag_sort:checkbox").click(function () {
              var column = "table ." + $(this).attr("name");
              $(column).toggle();
          });

          var pusher = new Pusher('a0e97466cb155b48d6b7', {
              cluster: 'us2',
          });

          var customerChannel = pusher.subscribe('customer');
          customerChannel.bind('add', function (data) {
              dataTable.row.add([
                  data.key,
                  data.index,
                  data.tag,
                  data.name,
                  data.product,
                  data.other,
                  data.company,
                  data.tel,
                  data.email,
                  data.emailLIFF,
                  data.comment,
                  data.displayName,
                  data.dtg,
                  data.channel
              ]).draw(false);
          });
          console.log(customerChannel)
      });

      document.getElementById('select-all-import').onclick = function () {
          var checkboxes = document.getElementsByName('key_import');
          for (var checkbox of checkboxes) {
              checkbox.checked = this.checked;
          }
      }

  </script>


{% endblock %}