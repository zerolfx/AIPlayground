Vue.component('sign-input', {
  template: '#sign-input-template',
  props: ['placeholder', 'inputName', 'inputType', 'dataError'],
  data: function() {
    return {
      name: this.inputName,
      errorMessage: this.dataError,
    }
  },
  delimiters: ['[[', ']]'],  // resolve conflicts
  methods: {
    clearErrorMessage: function() {
      $(event.target).removeClass('invalid');
    },
    setError: function(name, msg) {
      if (this.name == name) {
        this.errorMessage = msg;
        var el = $(this.$el).children("input");
        el.removeClass("valid");
        el.addClass("invalid");
      }
    }
  }
});


var signinForm = {
  template: '#sign-in-template',
  methods: {
    sendErrorMessage: function(name, msg) {
      for (var i = 0; i < this.$children.length; ++i)
        this.$children[i].setError(name, msg);
    },
    submit: function() {
      var data = $(event.target).serialize();
      console.log(data);
    }
  }
};

var signupForm = {
  template: '#sign-up-template',
  methods: {
    sendErrorMessage: function(name, msg) {
      for (var i = 0; i < this.$children.length; ++i)
        this.$children[i].setError(name, msg);
    },
    submit: function() {
      var data = $(event.target).serialize();
    }
  }
};

var signContainer = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#sign-container',
  data: {
    signInActive: true,
    signUpActive: false,
  },
  components: {
    signin: signinForm,
    signup: signupForm
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
