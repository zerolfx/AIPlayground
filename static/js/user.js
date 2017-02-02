// included in user-related pages only

nav.toggleActive('user');

function clearErrorMsg() {
  $(event.target).next("label").attr('data-error', '');
  $(event.target).removeClass('invalid');
}

function invalidateElement(element, msg) {
  element.next("label").attr('data-error', msg);
  console.log(element.next("label:after").css('width'));
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

Vue.component('sign-input', {
  template: '#sign-input-template',
  props: ['placeholder', 'inputName', 'inputType', 'dataError'],
  delimiters: ['[[', ']]'],  // resolve conflicts
  methods: {
    clearErrorMessage: function() {
      console.log(this.$ref);
      $(event.target).removeClass('invalid');
    }
  }
});


Vue.component('signin', {
  template: '#sign-in-template',
  methods: {
    submit: function() {
      if (validateForm($(event.target))) {
        var data = $(event.target).serialize();
        console.log(data);
      }
    }
  }
});

Vue.component('signup', {
  template: '#sign-up-template',
  methods: {
    submit: function() {
      if (validateForm($(event.target))) {
        var data = $(event.target).serialize();
        console.log(data);
      }
    }
  }
});

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
    }
  }
});
