{% extends "customers_new/layout.html" %}
{% block content %}
    <br>
    <br>
    <div class="row" style="margin-top: 30px">
        <div class="col-lg-8 offset-lg-2">
            <form method="POST" action="">
                <div class="card">
                    <div class="card-header">
                        <i class="fa fa-edit">
                            แก้ไขข้อมูลลูกค้า <strong style="color: #25D366;" id="fname"> {{ data.user.Name }} </strong>
                        </i>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="name">ชื่อ</label>
                                    <input type="text" class="form-control" id="name" placeholder="Enter Name"
                                           name="name" onchange="myFuc()"
                                           value="{{ data.user.Name }}">
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="company">บริษัท</label>
                                    <input type="text" class="form-control" id="student_id" placeholder="Enter Company"
                                           name="company"
                                           value="{{ data.user.Company }}">
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="tel">เบอร์</label>
                            <input type="tel" class="form-control" id="tel" placeholder="Enter Tel"
                                   name="tel"
                                   value="{{ data.user.Tel }}">
                        </div>
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="email">อีเมล</label>
                                    <input type="email" class="form-control" id="email" placeholder="Enter Email"
                                           name="email"
                                           value="{{ data.user.Email }}">
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="token">อีเมลไลน์</label>
                                    <input type="email" class="form-control" id="token" placeholder="Enter Email LINE"
                                           name="token"
                                           value="{{ data.user.EmailLiff }}">
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="form-group">
                                    <label for="displayName">ชื่อโปรไฟล์</label>
                                    <input type="text" class="form-control" id="displayName"
                                           placeholder="Enter displayName"
                                           name="displayName"
                                           value="{{ data.user.Profile }}">
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label for="channel">ช่องทาง</label>
                                    <input type="text" class="form-control" id="channel" placeholder="Enter Channel"
                                           name="channel"
                                           value="{{ data.user.Channel }}">
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="message">ข้อความ</label>
                            <input type="text" class="form-control" id="message" placeholder="Enter Message"
                                   name="message"
                                   value="{{ data.user.Message }}">
                        </div>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="product">ผลิตภัณฑ์</label><br>
                                    <select name="product" id="product" class="form-control form-control-sm">
                                        <option value="">Please, select</option>
                                        {% for user in data.product %}
                                            <option value="{{ user }}" {% if user == data.user.Product %}
                                                    selected {% endif %}>
                                                {{ user }}
                                            </option>
                                        {% endfor %}
                                    </select>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="other">ผลิตภัณฑ์อื่น</label><br>
                                    <select name="other" id="other" class="form-control form-control-sm">
                                        <option value="">Please, select</option>
                                        {% for user in data.other %}
                                            <option value="{{ user }}" {% if user == data.user.Other %}
                                                    selected {% endif %}>
                                                {{ user }}
                                            </option>
                                        {% endfor %}
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <button type="button" class="btn btn-success btn-xs"
                                    data-toggle="collapse"
                                    data-target="#liff">
                                <i class="fas fa-tags"></i>
                            </button>
                            <div id="liff" class="collapse fade" style="margin-top: 15px">
                                {% for tag in data.tag %}
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="{{ tag }}"
                                                {% if tag in data.user.Tag %} checked {% endif %}
                                               id="{{ tag }}"
                                               name="tag">
                                        <label class="form-check-label" for="{{ tag }}">
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
                        </div>

                        <div class="row">
                            <div class="col">
                                <div class="form-group">
                                    <label for="channel">ทุนจดทะเบียน</label>
                                    <input type="text" class="form-control" id="channel" placeholder="Enter Authorized"
                                           name="authorized"
                                           value="{{ data.user.Authorized }}">
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label for="channel">เลขผู้เสียภาษี</label>
                                    <input type="text" class="form-control" id="channel" placeholder="Enter Tax"
                                           name="tax"
                                           value="{{ data.user.Tax }}">
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label for="channel">ตำแหน่ง</label>
                                    <input type="text" class="form-control" id="channel" placeholder="Enter Position"
                                           name="position"
                                           value="{{ data.user.Position }}">
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="card-footer">
                        <button type="submit"
                                class="btn btn-outline-success btn-sm">
                            <i class="fa fa-check" aria-hidden="true"></i>
                            ตกลง
                        </button>

                        <a class="text-light" href="/marketing_information">
                            <button type="button" class="btn btn-outline-danger btn-sm">
                                <i class="fa fa-arrow-left" aria-hidden="true"></i>
                                ย้อนกลับ
                            </button>
                        </a>

                    </div>
                </div>
            </form>
        </div>

    </div>

    <script>
        function myFuc() {
            let paraName = document.getElementById("name").value;
            document.getElementById("fname").innerHTML = paraName;
        }
    </script>
{% endblock %}