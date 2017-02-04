Vue.component('board', {
  template: '#board-template',
  data: function() {
    return {
      submitCode: ''
    }
  },
  mounted: function() {
    $('select').material_select();
  },
  methods: {
    tabPrevent: function() {
      this.submitCode = this.submitCode + '    ';
    },
    formSubmitHelper: function() {
      var data = $(event.target).parents(".card.avatar").find("form").serialize();
      console.log(data);
    }
  }
});
