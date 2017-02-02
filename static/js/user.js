// included in user-related pages only

nav.toggleActive('user');

function clearErrorMsg() {
  $(event.target).next("label").attr('data-error', '');
  $(event.target).removeClass('invalid');
}

function invalidateElement(element, msg) {
  element.next("label").attr('data-error', msg);
  console.log(element.next("label:after"));
  element.removeClass("valid");
  element.addClass("invalid");
}

function validateForm(form) {
  var inputs = form.find("input");
  var valid = true;
  for (var i = 0; i < inputs.length; ++i) {
    var input = $(inputs[i]);
    if (input.hasClass("required") && input.val() == "") {
      invalidateElement(input, "Required: " + input.attr('name') + ".");
      valid = false;
    }
    if (input.hasClass("invalid")) valid = false;
  }
  return valid;
}

function passwordRepeatValidate() {
  if ($("#signupPasswordRepeat").val() != $("#signupPassword").val()) {
    invalidateElement($("#signupPasswordRepeat"), "Passwords are not identical.");
    return false;
  }
  return true;
}

function signinValidate() {
  if (validateForm($("#sign-in-form"))) {
    var data = $("#sign-in-form").serialize();
    console.log(data);
  }
}

function signupValidate() {
  if (!passwordRepeatValidate()) return;
  if (validateForm($("#sign-up-form"))) {
    var data = $("#sign-up-form").serialize();
    console.log(data);
  }
}

var signContainer = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#sign-container',
  data: {
    signInActive: true,
    signUpActive: false,
  },
  methods: {
    toggle: function(type) {
      if (type == 'in') {
        this.signInActive = true;
        this.signUpActive = false;
      } else {
        this.signInActive = false;
        this.signUpActive = true;
      }
    },
    signIn: function() {
      signinValidate();
    },
    signUp: function() {
      signupValidate();
    },
    passwordRepeatValidate: function() {
      passwordRepeatValidate();
    }
  }
});
