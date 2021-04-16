message_empty = 'Нет непрочитанных сообщений'

Vue.component('message', {
  delimiters: ["[[", "]]"],
  props: ['index','id','text', 'read'],

  methods: {
    markRead: async function (id) {
        await axios.get('api/mark_read?id=' + id)
        this.$parent.messages[String(this.index)].read = true
        return true
    },
  },

  computed: {
    status: function () {
        return this.read ? 'прочитано' : 'не прочитано'
        }
    },
  template: '<div class="card-body"><h3 class="card-title">[[ id ]]</h3><h2>[[ status ]]</h2><p class="card-text">[[ text ]]</p><button v-on:click="markRead([[ id ]])" type="button" class="btn btn-primary">mark read</button></div>'
})

var app = new Vue({
  el: '#messagesFromSpace',
  delimiters: ["[[", "]]"],

  methods: {
    async updateMessages() {
        resp = await axios.get('api/get_messages?last_id=' + this.last_id)
        this.messages = resp.data
    },
  },

  data() {
        return {
            messages: [],
            message_empty: message_empty}
  },

  computed: {
    last_id: function () {
        return this.messages.length > 0 ? this.messages['0'].id : 0
    }
    },

  mounted() {
        this.updateMessages()
        this.interval = setInterval(() => {
            this.updateMessages()
        },10000)
  },
  })