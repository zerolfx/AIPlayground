// included in user-related pages only

nav.toggleActive('user');

function signinValidate() {
  var usernameBox = $("#signinUsername");
  var passwordBox = $("#signinPassword");
  console.log(usernameBox.value);
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
