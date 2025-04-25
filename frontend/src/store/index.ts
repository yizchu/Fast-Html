import { createStore } from 'vuex'
import pageStore from './page_store'
import settingStore from './settings_store'

const store = createStore({
    modules: {
        Page: pageStore,
        Settings: settingStore,
    }
})

export default store