<template>
    <Dropdown class="page">
        <Button type="primary">
            工程
            <Icon type="ios-arrow-down"></Icon>
        </Button>
        <template #list>
            <DropdownMenu>
                <DropdownItem @click="show_newpage=true">新建</DropdownItem>
                <DropdownItem @click="selectFolder">打开</DropdownItem>
                <DropdownItem @click="show_settings=true">配置</DropdownItem>
            </DropdownMenu>
        </template>
    </Dropdown>
    <newpage v-model:show_newpage="show_newpage" v-if="show_newpage" />
    <settings v-model:show_settings="show_settings" v-if="show_settings"/>
</template>

<script>
    import newpage from './newpage.vue'
    import settings from './settings.vue'
    export default {
        components: {
            newpage,
            settings,
        },
        data () {
            return {
                show_newpage: false,
                show_settings: false,
                selectedOption: null,
                directoryhandle: null,
                pageName: '',
                html_content : '',
                css_content : '',
            }
        },
        methods: {
            async selectFolder() {
                try {
                    if (!('showDirectoryPicker' in window)) {
                        throw new Error('您的浏览器不支持文件夹选择功能，请使用新版浏览器');
                    }
                    this.html_content = '';
                    this.css_content = '';
                    this.directoryhandle = await window.showDirectoryPicker({mode: 'readwrite',});
                    this.pageName = this.directoryhandle.name;
                    await this.processDirectory(this.directoryhandle);
                    this.$emit('update:pageName', this.pageName);
                    this.$page_store.commit('updateHtml', this.html_content);
                    this.$page_store.commit('updateCss', this.css_content);
                    this.$Notice.success({
                        title: 'Success!',
                        desc: `成功打开 ${this.pageName}。`,
                    });
                }catch (error) {
                    this.$Message.error(error.message);
                }
            },
            async processDirectory(handle) {
                for await (const entry of handle.values()) {
                    if (entry.kind === 'directory') {
                        await this.processDirectory(entry);
                    } else if (entry.kind === 'file') {
                        await this.processFile(entry);
                    }
                }
            },
            async processFile(fileHandle) {
                const file = await fileHandle.getFile();
                const fileName = file.name.toLowerCase();

                if (fileName.endsWith('.html')) {
                    this.html_content=await file.text();
                } else if (fileName.endsWith('.css')) {
                this.css_content = await file.text();
                }
            },
        }
    }

</script>

<style>
.page{
    transform: scale(1.2);
    transform-origin: top left;
}

</style>