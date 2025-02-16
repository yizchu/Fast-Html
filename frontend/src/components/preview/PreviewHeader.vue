<template>
    <div class="preview-header">
        <div class="button-container">
            <button @click="toggleSidebar" class="toggle-sidebar-btn">
                {{ showSidebar ? '隐藏具体' : '显示具体' }}
            </button>
            <button :disabled="Mode2" @click="toggleMode1">
                {{ Mode1 ? '退出单选' : '单选模式' }}
            </button>
            <button :disabled="Mode1" @click="toggleMode2">
                {{ Mode2 ? '退出多选' : '多选模式' }}
            </button>
            <button @click="decreaseZoom">-</button>
            <span>{{ zoomPercentage }}%</span>
            <button @click="increaseZoom">+</button>
            <Icon type="md-download" class="download" @click="handleDownload"/>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapState } from 'vuex';
    export default {
        name: 'PreviewHeader',
        props: {
            Mode1: {
                type: Boolean,
                required: true,
            },
            Mode2: {
                type: Boolean,
                required: true,
            },
        },
        data() {
            return {
                zoomPercentage: 100,
                zoomScale: 1,
                showSidebar: false,
            };
        },
        computed: {
            ...mapState({
                backend_url: state => state.Settings.backend_url,
                original_content: state => state.Page.original_content,
                page_name: state => state.Page.page_name,
            }),
        },
        methods: {
            toggleMode1() {
                const newValue = !this.Mode1;
                this.$emit('updateMode1', newValue);
            },
            toggleMode2() {
                const newValue = !this.Mode2;
                this.$emit('updateMode2', newValue);
            },
            increaseZoom() {
                if (this.zoomPercentage < 200) {
                    this.zoomPercentage += 10;
                    this.zoomScale = this.zoomPercentage / 100;
                    this.$emit('zoomChanged', this.zoomScale);
                }
            },
            decreaseZoom() {
                if (this.zoomPercentage > 50) {
                    this.zoomPercentage -= 10;
                    this.zoomScale = this.zoomPercentage / 100;
                    this.$emit('zoomChanged', this.zoomScale);
                }
            },
            toggleSidebar() {
                this.showSidebar = !this.showSidebar;
                this.$emit('toggleSidebar', this.showSidebar);
            },
            handleDownload() {
                if (this.original_content) {
                    axios.post(`${this.backend_url}/download-page/`, null, {
                        responseType: 'blob'
                    })
                    .then((response) => {
                        const blob = new Blob([response.data], { type: 'application/zip' });
                        const link = document.createElement('a');
                        const fileName = `${this.page_name || 'download'}.zip`;
                        link.href = URL.createObjectURL(blob);
                        link.download = fileName;
                        link.click();
                        URL.revokeObjectURL(link.href);
                    })
                    .catch((error) => {
                        this.$Message.error('下载失败!');
                    });
                }
            },
        },
    }
</script>

<style>
.preview-header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
}

.preview-header .button-container {
    margin-left: auto;
}

.preview-header button {
    background: #42b883;
    margin-left: 10px;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
}

.preview-header button:hover {
    background: #358a6b;
}

.preview-header button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.preview-header span {
    font-size: 18px;
    margin: 0 5px;
}

.preview-header p{
    font-size: 24px;
    font-weight: bold;
}

.preview-header .toggle-sidebar-btn {
    background-color: #f39c12;
}

.preview-header .toggle-sidebar-btn:hover {
    background-color: #e67e22;
}

.download {
    font-size: 24px;
    margin-left: 30px;
    cursor: pointer;
}
</style>