const message_empty = 'Нет непрочитанных сообщений'
const message_is_read = 'Прочитано'
const message_is_not_read = 'Не прочитано'

const get_messages_delay = 10000 // in ms

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


Vue.component('message', {
  delimiters: ["[[", "]]"],
  props: ['index','id','text', 'is_read'],

  methods: {
    markRead: async function (id) {
        await axios.post('api/mark_read?id=' + id)
        this.$parent.messages[this.index].is_read = true
    },
  },

  computed: {
    status: function () {
        return this.is_read ? message_is_read : message_is_not_read
        }
    },
  template: `
    <div class="card-body">
        <h3 class="card-title">[[ id ]]</h3>
        <h2 class="card-subtitle mb-2 text-muted">[[ status ]]</h2>
        <p class="card-text">[[ text ]]</p>
        <div class="d-grid gap-2 col-6 mx-auto">
            <button v-on:click="markRead([[ id ]])" type="button" class="btn btn-primary">прочитано</button>
        </div>
    </div>
  `,
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
        }, get_messages_delay)
  },
})
