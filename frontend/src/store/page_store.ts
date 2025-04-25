const pageStore = {
    namespaced: true,
    state: {
        html_css_content: '',   // 当前
        original_content: '',   // 历史，撤销用，换成栈结构更好
        page_name: '',
        selected_element: null,
        selected_elements: [],
    },
    mutations: {
        updatePageName(state: any, value: string) {
            state.page_name = value;
        },
        updateHtmlCss(state: any, value: string) {
            state.html_css_content = value;
        },
        updateOriginalContent(state: any, value: string) {
            state.original_content = value;
        },
        updateEl(state: any, value: any) {
            state.selected_element = value;
        },
        addEls(state: any, value: any) {
            state.selected_elements.push(value);
        },
        removeEls(state: any, value: any) {
            state.selected_elements = state.selected_elements.filter((element: any) => element !== value);
        },
        clearEls(state: any) {
            state.selected_elements = [];
        }
    },
};

export default pageStore;