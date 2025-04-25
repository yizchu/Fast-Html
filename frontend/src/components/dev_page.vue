<template>
    <div class="header">
        <PagesOverview />
    </div>
    <div class="info-wrapper">
        <Info v-if="selected_element || selected_elements.length > 0" class="info"/>
        <p v-if="!selected_element && selected_elements.length===0">
            请选取至少一个元素
        </p>
    </div>
    <div class="pagePreview-wrapper">
        <PagePreview class="pagePreview"/>
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import PagesOverview from './pages/PagesOverview.vue'
    import PagePreview from './preview/PagePreview.vue'
    import Info from './info/Info.vue'


    export default {
        components: {
            PagesOverview,
            PagePreview,
            Info,
        },
        computed: {
            ...mapState({
                selected_element: state => state.Page.selected_element,
                selected_elements: state => state.Page.selected_elements,
            }),
        },
    }
</script>

<style>
.header {
    display: flex;
    align-items: center;
}
.header p {
    font-size: 24px;
    margin-left: 100px;
}

.pagePreview-wrapper {
    position: absolute;
    top: 0;
    width: 60%;
    left: 40%;
}

.info-wrapper {
    position: absolute;
    display: flex;
    top: 0;
    left: 6.5%;
    width: 33.5%;
    height: 60%;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    align-items: center;
    justify-content: center;
}

.info-wrapper p {
    font-size: 24px;
}
</style>