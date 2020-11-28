{% extends "main/loginLayout.html" %} {% block content %}
  <br>
  <div id="app">
    <div class="jumbotron">
      <div class="container">
        <div class="row justify-content-center">
          <div class="container">
            <div class="text-center">
              <h1 class="h4 text-gray-900 mb-4">LINE BOT MANGO</h1>
            </div>
          </div>
          <div class="col-lg-7">
            <div class="card shadow-lg border-0 rounded-lg">
              <div class="card-header"><h3 class="text-center font-weight-light my-4">Create Account </h3>
              </div>
              <div class="card-body">
                <form method="POST" action="/signup">
                  <div class="form-row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1" for="inputUsername">Username</label>
                        <input :class="getInputClass('userId')"
                               v-model="formElements.userId.value"
                               @keyup="onChangeForm($event)"
                               id="userId" type="text"
                               name="userId"
                               placeholder="Enter Username"/>
                        <div class="invalid-feedback">[[ getErrorMessage('userId') ]]</div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1" for="position">Position</label>
                        <input :class="getInputClass('position')"
                               v-model="formElements.position.value"
                               @keyup="onChangeForm($event)"
                               id="position" type="text"
                               name="position"
                               placeholder="Enter Position"/>
                        <div class="invalid-feedback">[[ getErrorMessage('position') ]]</div>
                      </div>
                    </div>
                  </div>
                  <div class="form-row">
                    <div class=""></div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1" for="firstname">First Name</label>
                        <input :class="getInputClass('firstname')"
                               v-model="formElements.firstname.value"
                               @keyup="onChangeForm($event)"
                               id="firstname" name="firstname"
                               type="text"
                               placeholder="Enter first name">
                        <div class="invalid-feedback">[[ getErrorMessage('firstname') ]]</div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1" for="lastname">Last Name</label>
                        <input :class="getInputClass('lastname')"
                               v-model="formElements.lastname.value"
                               @keyup="onChangeForm($event)"
                               id="lastname" name="lastname" type="text"
                               placeholder="Enter lastname"/>
                        <div class="invalid-feedback">[[ getErrorMessage('lastname') ]]</div>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="small mb-1" for="email">Email</label>
                    <input :class="getInputClass('email')"
                           v-model="formElements.email.value"
                           @keyup="onChangeForm($event)"
                           id="inputEmailAddress" type="email"
                           name="email" aria-describedby="emailHelp"
                           placeholder="Enter email address"/>
                    <div class="invalid-feedback">[[ getErrorMessage('email') ]]</div>
                  </div>
                  <div class="form-row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1"
                            for="password">Password</label>
                        <input :class="getInputClass('password')"
                               v-model="formElements.password.value"
                               @keyup="onChangeForm($event)"
                               name="password" id="inputPassword"
                               type="password" placeholder="Enter password" required/>
                        <div class="invalid-feedback">[[ getErrorMessage('password') ]]</div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label class="small mb-1"
                               for="inputPassword">Confirm Password</label>
                        <input class="form-control " name="confirmpwd" id="confirmPassword"
                               type="password" placeholder="Confirm password" required/>
                      </div>
                    </div>
                  </div>
                  <button type="submit" class="btn btn-success btn-block" :disabled="!formValid">Submit</button>
                  <br>
                  <p class="text-danger">{{ error }}</p>
                </form>
              </div>


            </div>
            <div class="card-footer text-center">
              <div class="small"><a href="/welcome">Have an account? Go to login</a></div>
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
                      userId: {
                          type: 'text',
                          value: '',
                          validator: {
                              required: true,
                              minLength: 4,
                              maxLength: 15
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      },
                      position: {
                          type: 'text',
                          value: '',
                          validator: {
                              required: true,
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      },
                      firstname: {
                          type: 'text',
                          value: '',
                          validator: {
                              required: true,
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      },
                      lastname: {
                          type: 'text',
                          value: '',
                          validator: {
                              required: true,
                          },
                          touched: false,
                          error: {status: true, message: ''}
                      },
                      email: {
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
                              minLength: 6
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
                      return ["form-control"];
                  } else {
                      return elementErrorStatus && this.formElements[name].touched ? ['form-control', 'is-invalid'] : ['form-control', 'is-valid'];
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
