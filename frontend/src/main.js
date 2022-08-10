import {createApp} from 'vue'
import App from './App.vue'
import {Table,Button,Row,Col} from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import io from 'socket.io-client';
const app = createApp(App);
app.config.globalProperties.$socket=io('http://localhost:4000')
app.use(Table)
app.use(Button)
app.use(Row)
app.use(Col)
app.use()
app.mount("#app");