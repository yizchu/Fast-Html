<template>
    <Spin fix v-if="loading">
        <Icon type="ios-loading" size=18 class="demo-spin-icon-load"></Icon>
        <div>Loading</div>
    </Spin>
    <Button class="new-page" @click="show_newpage = true" type="primary">还没有工程? 去创建 =></Button>
    <li class="info">打开工程</li>
    <div class="dropdown-container">
        <select :key="key" name="pages" v-model="selectedPage" @change="onPageSelect">
        <option value=""> --请选择一个工程-- </option>
        <option v-for="page in pages" :key="page" :value="page">
            {{ page }}
        </option>
        </select>
    </div>
    <li class="info">网页标题</li>
    <div class="box">
        <input v-model="inputTitle" :disabled="!isEditable" type="text" class="input-box"/>
        <Button type="success" ghost @click="onEdit" :disabled="isEditable || selectedPage===''" class="action-button">
            修改
        </Button>
        <Button type="success" ghost @click="onSave" :disabled="!canSaveCancel" class="action-button">
            保存
        </Button>
        <Button type="success" ghost @click="onCancel" :disabled="!canSaveCancel" class="action-button">
            取消
        </Button>
    </div>
    <NewPage v-model:show_newpage="show_newpage" v-if="show_newpage" />
</template>

<script>
    import { mapState, mapMutations } from 'vuex';
    import axios from 'axios';

    import NewPage from './NewPage.vue'

    export default {
        name: 'Pages',
        computed: {
            ...mapState({
                backend_url: state => state.Settings.backend_url,
                html_css_content: state => state.Page.html_css_content,
                original_content: state => state.Page.original_content,
            }),
        },
        components: {
            NewPage,
        },
        data () {
            return {
                show_newpage: false,
                pages: [],
                selectedPage: '',
                originTitle: '',
                inputTitle: '',
                isEditable: false,
                canSaveCancel: false,
                loading: false,
                key: 0,
            }
        },
        mounted() {
            this.fetchPages();
        },watch: {
            show_newpage(newVal, oldVal) {
                if (oldVal === true && newVal === false) {
                    this.fetchPages();
                }
            }
        },
        methods: {
            ...mapMutations('Page', ['updatePageName', 'updateHtmlCss', 'updateOriginalContent', 'updateEl', 'clearEls']),
            async fetchPages() {
                try {
                    const response = await axios.get(`${this.backend_url}/get-page/`);
                    this.pages = response.data;
                    this.key += 1;
                } catch (error) {
                    console.error('Error fetching projects:', error);
                }
            },
            async onPageSelect() {
                if (this.selectedPage) {
                    this.loading = true;
                    this.updateEl(null);
                    this.clearEls();
                    try {
                        const response = await axios.post(`${this.backend_url}/open-page/`, {page_name: this.selectedPage}, {
                            headers: {
                                'content-type': 'application/json'
                            },
                        });
                        this.updatePageName(this.selectedPage);
                        this.updateHtmlCss(response.data.html_css_content);
                        this.updateOriginalContent(response.data.original_content);
                        this.inputTitle = this.original_content.match(/<title>(.*?)<\/title>/)[1];
                        this.$Notice.success({
                            title: 'Success',
                            desc: `成功打开 ${this.selectedPage}。`,
                            duration: 1,
                        });
                    } catch (error) {
                        console.error('Error selecting project:', error);
                    }
                    this.loading = false;
                }
            },
            async onEdit() {
                this.isEditable = true;
                this.canSaveCancel = true;
                this.originTitle = this.inputTitle;
            },
            async onSave() {
                this.updateOriginalContent(
                    this.original_content.replace(/<title>.*<\/title>/, `<title>${this.inputTitle}</title>`));
                try{
                    await axios.post(`${this.backend_url}/update-page/`, {html_css_content: this.original_content}, {
                        headers: {
                            'content-type': 'application/json'
                        }
                    });
                }catch (error) {
                    console.error('Error updating project:', error);
                }
                this.resetButtons();
            },
            async onCancel() {
                this.inputTitle = this.originTitle;
                this.resetButtons();
            },
            async resetButtons() {
                this.isEditable = false;
                this.canSaveCancel = false;
            },
    }
}
</script>

<style>
.page{
    transform: scale(1.5);
    transform-origin: top left;
}

.info {
    margin-top: 40px;
    font-size: 24px;
    font-weight: bold;
}

.new-page {
    transform: scale(1.5);
    transform-origin: top left;
}

.dropdown-container {
  width: 300px;
  margin-top:10px;
}

select {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.box {
  display: flex;
  align-items: center;
  padding: 10px;
  width: 100%;
  margin-left:23%;
  transform: scale(1.5);
}

.input-box {
  margin-right: 10px;
}

.action-button {
  margin-left: 5px;
}

.action-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.demo-spin-col .circular {
        width:25px;
        height:25px;
}

.demo-spin-icon-load{
    animation: ani-demo-spin 1s linear infinite;
}

.demo-spin-col{
    height: 100px;
    position: relative;
    border: 1px solid #eee;
    transform: scale(2);
}

</style>