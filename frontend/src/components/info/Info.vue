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
    <div v-if="selectedMenu === 'edit-css'">
        <EditCss />
    </div>
    <div v-if="selectedMenu === 'nest'">
    </div>
</template>

<script>
    import EditCss from './EditCss.vue'
    export default{
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

