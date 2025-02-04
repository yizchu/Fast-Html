<template>
    <Button class="overview" @click="overview = true" type="primary">工程总览</Button>
    <Drawer title="工程总览" placement="left" width=20 :closable="false" v-model="overview">
        <pages @update:pageName="updatePageName"/>
        <li class="info">工程名称</li>
        <p class="value">{{ pageName }}</p>
    </Drawer>
</template>

<script>
    import pages from './pages.vue'
    export default{
        components: {
            pages,
        },
        data() {
            return {
                overview: false,
                pageName: '',
            }
        },
        methods: {
            updatePageName(newPageName) {
                this.pageName = newPageName;
            },
        }
    }
</script>

<style>
.overview {
    transform: scale(1.2);
    transform-origin: top left;
}

.info {
    margin-top: 40px;
    font-size: 24px;
    font-weight: bold;
}

.value{
    font-size: 24px;
    margin-top: 10px;
    text-align: center;
}
</style>