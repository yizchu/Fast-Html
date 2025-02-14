const settingStore = {
    namespaced: true,
    state: {
        backend_url: localStorage.getItem('backend_url') || 'http://localhost:8000',
    },
    mutations: {
        updateBackendUrl(state: any, value: string) {
            state.backend_url = value;
            localStorage.setItem('backend_url', value);
        },
    },
};

export default settingStore;