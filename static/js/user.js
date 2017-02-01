// included in user-related pages only

nav.toggleActive('user');

function signinValidate() {
  var usernameBox = document.getElementById("signinUsername");
  var passwordBox = document.getElementById("signinPassword");
  console.log("hello");
}

var signContainer = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#sign-container',
  data: {
    signInActive: true,
    signUpActive: false
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
    }
  }
});
