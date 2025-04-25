<template>
    <div class="info-container">
        <Menu mode="horizontal" @on-select="userSelection">
            <MenuItem name="edit-css">
                <Icon type="ios-create-outline" />
                <span>编辑样式</span>
            </MenuItem>
            <MenuItem name="nest">
                <Icon type="md-albums" />
                <span>设置嵌套</span>
            </MenuItem>
        </Menu>
        <div class="info-header">
            <p> tag:&nbsp;{{selected_element.tagName.toLowerCase()}}</p>
            <p class="className"> class: </p>
            <div class="box">
                <input v-model="selected_element.className" type="text" class="input-box"/>
                <Button type="success" ghost @click="onSave" class="action-button">
                    保存
                </Button>
                <Button type="success" ghost @click="onCancel" class="action-button">
                    撤销
                </Button>
            </div>
        </div>


    </div>
</template>

<script>
    import { mapState, mapMutations } from 'vuex';
    import EditCss from './EditCss.vue';

    export default{
        components: {
            EditCss,
        },
        computed: {
            ...mapState({
                selected_element: state => state.Page.selected_element,
                selected_elements: state => state.Page.selected_elements,
                original_content: state => state.Page.original_content,
            }),
        },
        data() {
            return{
                selectedMenu: 'edit-css',
                inputClassName: '',
                originClassName: '',
            }
        },
        methods: {
            ...mapMutations('Page', ['updateOriginalContent']),
            userSelection(name) {
                this.selectedMenu = name;
            },
            onSave() {
                this.originClassName = this.inputClassName;
                const updatedContent = this.selected_element.outerHTML.replace(/class="[^"]*"/, `class="${this.inputClassName}"`);
                this.updateOriginalContent(this.original_content.replace(this.selected_element.outerHTML, updatedContent));
                this.selected_element.outerHTML = updatedContent;
            },
            onCancel() {
                this.inputClassName = this.originClassName;
            },
        }
    }
</script>

<style>
.info-container{
    display: flex;
    flex-direction: column;
    margin: 0;
    height: 100%;
    width: 100%;
    overflow: auto;
}
.info-header {
    height: 10%;
    flex-direction: row;
    display: flex;
    align-items: center;
}

.info-header p {
    font-size: 1.5rem;
    margin-left: 0.75rem;
}

.info-header .box {
    display: flex-start;
    align-items: center;
    margin: 0;
    transform: scale(1.0);
}

.info-header .className{
    margin-left: 3.125rem;
}

.info-header .input-box {
    width: 9.375rem;
    height: 1.875rem;
}
</style>