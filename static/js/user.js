// included in user-related pages only

nav.toggleActive('user');


function invalidateElement(element, msg) {
  element.next("label").attr('data-error', msg);
  element.removeClass("valid");
  element.addClass("invalid");
}

function passwordRepeatValidate() {
  if ($("#signupPasswordRepeat").val() != $("#signupPassword").val()) {
    invalidateElement($("#signupPasswordRepeat"), "Passwords are not identical.");
    return false;
  }
  return true;
}

function signinValidate() {
  var inputs = $("#sign-in-form").find("input");
  var data = new Array();
  for (var i = 0; i < inputs.length; ++i) {
    var input = $(inputs[i]);
    if (input.hasClass("required") && input.val() == "")
      invalidateElement(input, "Required: " + input.attr('name') + ".");
    if (input.hasClass("invalid")) return;
    data[input.attr('name')] = input.val();
  }
  console.log(data);
}

function signupValidate() {
  if (!passwordRepeatValidate()) return;
  var inputs = $("#sign-up-form").find("input");
  var data = new Array();
  for (var i = 0; i < inputs.length; ++i) {
    var input = $(inputs[i]);
    if (input.hasClass("required") && input.val() == "")
      invalidateElement(input, "Required: " + input.attr('name') + ".");
    if (input.hasClass("invalid")) return;
    data[input.attr('name')] = input.val();
  }
  console.log(data);
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
