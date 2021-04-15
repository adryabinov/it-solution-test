function noDelaySetInterval(func, interval) {
      func();
      return setInterval(func, interval);
      };

Vue.component('message', {
  delimiters: ["[[", "]]"],
  props: ['id','text', 'read'],
  methods: {
    markRead: async function (id) {
        await axios.get('api/mark_read?id=' + id)
        this.read = true
        return true
    },
  },
  template: '<div class="card-body"><h3 class="card-title">[[ id ]]</h3><h2>[[ read ]]</h2><p class="card-text">[[ text ]]</p><button v-on:click="markRead([[ id ]])" type="button" class="btn btn-primary">mark read</button></div>'
})

var app = new Vue({
  el: '#messagesFromSpace',
  delimiters: ["[[", "]]"],
  methods: {
    async updateMessages() {
        resp = await axios.get('api/get_messages?last_id=' + last_id)
        this.messages = resp.data
    },
  },
  data(){
        return {
            messages: []}
  },
  mounted() {
        this.updateMessages();
        this.interval = setInterval(() => {
            this.updateMessages()
        },10000);
  },
  });