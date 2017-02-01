// constants
SMALL_MAX_WIDTH = 600;
MED_MAX_WIDTH = 992;
LOGO_TITLE = 'AI Playground';

// navbar init

var nav = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: 'nav',
  data: {
    navbarActive: {
      home: false,
      problem: false,
      competition: false,
      board: false,
      search: false,
      user: false
    },
    logoTitle: LOGO_TITLE,
  },
  methods: {
    toggleActive: function (type) {
      for (var prop in this.navbarActive)
        this.navbarActive.prop = false;
      this.navbarActive[type] = true;
    }
  }
});

// side-nav ready
(function($) {
  $(function() {
    $(".button-collapse").sideNav();
  });
})(jQuery);
