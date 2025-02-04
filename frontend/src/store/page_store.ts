import { createStore } from 'vuex';

export default createStore({
    state: {
        html_content: '',
        css_content: '',
    },
    mutations: {
        updateHtml(state, value) {
            state.html_content = value;
        },
        updateCss(state, value) {
            state.css_content = value;
        },
    },

});