<template>
    <div class="header">
        <PagesOverview />
    </div>
    <div class="pagePreview-wrapper">
        <PagePreview class="pagePreview"/>
    </div>
</template>

<script>
    import PagesOverview from './pages/PagesOverview.vue'
    import PagePreview from './preview/PagePreview.vue'


    export default {
        components: {
            PagesOverview,
            PagePreview,
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
    top:0;
    width:60%;
    left:40%;
}
</style>