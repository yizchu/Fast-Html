<template>
    <Button class="overview" @click="overview = true" type="primary">工程总览</Button>
    <Drawer title="工程总览" placement="left" width=40 :closable="false" v-model="overview">
        <Pages/>
        <div class="settings-wrapper">
            <div class="settings-container" @mouseenter="show = true" @mouseleave="show = false" @click="show_settings=true">
                <Icon type="ios-construct" class="settings_"/>
                <div class="path-box" v-if="show">
                    <span class="arrow"></span>
                    配置
                </div>
            </div>
        </div>
    </Drawer>
    <Settings v-model:show_settings="show_settings" v-if="show_settings" />
</template>

<script>
    import Pages from './Pages.vue';
    import Settings from './Settings.vue';

    export default{
        components: {
            Pages,
            Settings,
        },
        data() {
            return {
                overview: false,
                show:false,
                show_settings: false,
            }
        },
    }
</script>

<style>
.overview {
    transform: scale(1.2);
    transform-origin: top left;
}
.settings-wrapper {
    position: relative;
    height: 50%;    /* 根据情况调整配置图标的上下位置*/
    width:100%;
    left: 0;
}

.settings-container {
    position: absolute;
    bottom:0;
    height:0;
    padding: 10px;
    box-sizing: border-box;
    justify-content: flex-start;
    align-items: center;
}

.settings-container:hover {
    cursor: pointer;
}

.settings_ {
    font-size: 50px;
    color: #fff;
    background-color: #000;
    padding: 10px;
    border-radius: 50%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.path-box {
    position: absolute;
    left: 100%;
    margin-left: 40px;
    margin-top: -60px;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    background-color: #b512fc;
    color: white;
    padding: 10px 15px;
    font-family: monospace;
    border-radius: 8px;
    max-width: 400px;
    word-wrap: break-word;
    white-space: nowrap;
    opacity: 0.9;
    z-index: 1000;
    font-size: 20px;
}

.arrow {
    position: absolute;
    right: 100%;
    top: 50%;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-top: 8px solid;
    border-bottom: 8px solid;
    border-right: 8px solid #b512fc;
}
</style>