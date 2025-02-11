import { createApp } from 'vue'
import App from './App'
import router from './router'
import ViewUiPlus from 'view-ui-plus'
import './styles/index.less'
import store from './store'

const app = createApp(App)

app.use(router)
    .use(ViewUiPlus)
    .use(store)
    .mount('#app')
