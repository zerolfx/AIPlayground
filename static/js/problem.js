var feed = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#feed-problem',
  data: {
  },
  methods: {
    search: function() {
      // TODO: search options
      console.log(event.target);
    },
    gotoProblem: function() {
      window.location.href = '/problem/1';
    }
  }
});

Vue.component('description', {
  template: '#problem-description-template',
});

Vue.component('board', {
  template: '#board-template',
});

Vue.component('ranklist', {
  template: '#problem-ranklist-template',
});

Vue.component('management', {
  template: '#problem-manage-template',
});

var show = new Vue({
  delimiters: ['[[', ']]'],  // resolve conflicts
  el: '#show-problem',
  data: {
    showComponent: 'description',
  },
  methods: {
    toggle: function(tab) {
      this.showComponent = tab;
      $(event.target).addClass("active");
      $(event.target).siblings().removeClass("active");
    }
  }
});
