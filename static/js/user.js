// included in user-related pages only

nav.toggleActive('user');

var sign = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#sign-container',
  data: {
    url: 'haha',
    signInActive: true,
    signUpActive: false
  },
  methods: {
    click: function() {
      console.log("hello");
    }
  }
})
