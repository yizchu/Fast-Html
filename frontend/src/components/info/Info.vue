<template>
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
    <div v-if="selectedMenu === 'edit-css'" class="edit-css-container">
        <EditCss />
    </div>
    <div v-if="selectedMenu === 'nest'">
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import EditCss from './EditCss.vue';

    export default{
        components: {
            EditCss,
        },
        computed: {
            ...mapState({
                selected_element: state => state.Page.selected_element,
                selected_elements: state => state.Page.selected_elements,
            }),
        },
        data() {
            return{
                selectedMenu: 'edit-css',
            }
        },
        methods: {
            userSelection(name) {
                this.selectedMenu = name;
            }
        }
    }
</script>

<style>
.edit-css-container {
  padding: 20px;
  background-color: #f0f2f5;
  flex-grow: 1;
  overflow: auto;
}

.EditCss {
    padding: 20px;
    background-color: #f0f2f5;
    height: 100%;
    overflow: auto;
}
</style>