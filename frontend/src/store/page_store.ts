const pageStore = {
    namespaced: true,
    state: {
        html_css_content: '',   // 预览所用
        original_content: '',   // 后端修改所用
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