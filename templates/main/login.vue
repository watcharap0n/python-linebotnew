{% extends "main/loginLayout.html" %}
{% block content %}


  <div id="app">
    <div class="jumbotron">
      <div class="container">

        <div class="row justify-content-center">
          <div class="col-xl-10 col-lg-12 col-md-9">
            <div class="card o-hidden border-0 shadow-lg my-5">
              <div class="card-body p-0">
                <!-- Nested Row within Card Body -->
                <div class="row">
                  <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                  <div class="col-lg-6">
                    <div class="p-5">
                      <div class="text-center">
                        <h1 class="h4 text-gray-900 mb-4">LINE BOT MANGO </h1>
                        <h3 class="h6 text-primary mb-4"><b> Customer {{ data.customer }}</b></h3>
                      </div>


                      <form class="user" method="POST" action="">
                        <div class="form-group">
                          <input :class="getInputClass('username')"
                                 type="text"
                                 placeholder="Email"
                                 name="username"
                              {% if request.cookies.get('user_id') %}
                                {% set reqs = request.cookies.get('user_id') %}
                                {% set txt = reqs.split() %}
                                {% if reqs %}
                                 value="{{ txt[0] }}"
                                {% endif %}
                              {% else %}
                                 value=""
                              {% endif %}
                          >
                          <div style="margin-top: 10px" class="invalid-feedback">
                            [[getErrorMessage('username')]]
                          </div>
                        </div>
                        <div class="form-group">
                          <input :class="getInputClass('password')"
                                 type="password"
                                 placeholder="Password"
                                 name="password"
                              {% if request.cookies.get('user_id') %}
                                {% set reqs = request.cookies.get('user_id') %}
                                {% set txt = reqs.split() %}
                                {% if reqs %}
                                 value="{{ txt[1] }}"
                                {% endif %}
                              {% else %}
                                 value=""
                              {% endif %}
                          >
                          <div style="margin-top: 10px" class="invalid-feedback">
                            [[getErrorMessage('password')]]
                          </div>
                        </div>
                        <div class="form-group">
                          <div class="custom-control custom-checkbox small">
                            <input type="checkbox" class="custom-control-input" name="remember" id="customCheck"
                                   value="check"
                                {% if request.cookies.get('user_id') %}
                                  {% set reqs = request.cookies.get('user_id') %}
                                  {% set txt = reqs.split() %}
                                  checked
                                {% endif %}>

                            <label class="custom-control-label" for="customCheck">Remember
                              Me</label>
                          </div>
                        </div>
                        <button class="btn btn-success btn-user btn-block" type="submit">
                          Log in
                        </button>

                      </form>
                      <br>
                      <div class="text-center">
                        <div class="small">Don't have an account? <a href="/signup">Sign Up</a></div>
                      </div>
                      <br>
                      <div class="text-center">
                        <a href="/forgot"><p class="small">Forgot Password?</p></a>
                      </div>
                      <p class="text-danger">{{ data.error }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>

    </div>
  </div>
  <script>


      var app = new Vue({
          el: "#app",
          data() {
              return {
                  formElements: {
                      username: {
                          type: 'email',
                          value: '',
                          validator: {
                              required: true,
                              pattern: 'email'
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      },
                      password: {
                          type: 'password',
                          value: '',
                          validator: {
                              required: true,
                              minLength: 1
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      }
                  },
                  formValid: false
              };
          },
          delimiters: ["[[", "]]"],
          methods: {
              onChangeForm(event) {
                  const name = event.target.name;
                  const value = event.target.value;
                  let updatedForm = {...this.formElements};
                  updatedForm[name].value = value;
                  updatedForm[name].touched = true;
                  const validatorObject = this.checkValidator(
                      value,
                      updatedForm[name].validator
                  );
                  updatedForm[name].error = {
                      status: validatorObject.status,
                      message: validatorObject.message
                  };
                  let formStatus = true;
                  for (let name in updatedForm) {
                      if (updatedForm[name].validator.required === true) {
                          formStatus = !updatedForm[name].error.status && formStatus;
                      }
                  }
                  this.formElements = updatedForm;
                  this.formValid = formStatus;
              },
              checkValidator(value, rule) {
                  let valid = true;
                  let message = '';
                  if (value.trim().length === 0 && rule.required) {
                      valid = false;
                      message = 'กรุณากรอกข้อมูล'
                  }
                  if (value.length < rule.minLength && valid) {
                      valid = false;
                      message = `น้อยกว่า ${rule.minLength} ตัวอักษร`;
                  }
                  if (rule.pattern === 'email' && valid) {
                      if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) === false) {
                          valid = false;
                          message = 'กรอกอีเมลไม่ถูกต้อง';
                      }
                  }
                  return {status: !valid, message: message}
              },
              getInputClass(name) {
                  const elementErrorStatus = this.formElements[name].error.status;
                  if (!this.formElements[name].touched) {
                      return ["form-control form-control-user"];
                  } else {
                      return elementErrorStatus && this.formElements[name].touched ? ['form-control form-control-user', 'is-invalid'] : ['form-control form-control-user', 'is-valid'];
                  }
              },
              getErrorMessage(name) {
                  return this.formElements[name].error.message;
              },
              onFormSubmit() {
                  const formData = {};
                  for (let name in this.formElements) {
                      formData[name] = this.formElements[name].value;
                  }
                  console.log(formData)
              }
          }
      });


  </script>

{% endblock %}


