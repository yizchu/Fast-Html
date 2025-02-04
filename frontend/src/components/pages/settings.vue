<template>
    <div v-if="show_settings" class="page_overlay" @click="close">
        <Card class="card" @click.stop>
            <h1>配置</h1>
            <template>
                <Switch v-model="theme" @on-change="change" />
            </template>
        </Card>
    </div>
</template>

<script>
export default {
    name: 'settings',
    props: {
        show_settings: {
            type: Boolean,
        },
        theme:{
            type: String,
            default: 'light',
        }
    },
    methods: {
        close() {
            this.$emit('update:show_settings', false);
        },
        change(value) {
            this.$emit('update:theme', value ? 'dark' : 'light');
        },
    },
}
</script>

<style>
.page_overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.card {
    justify-content: center;
    align-items: flex-start;
    text-align: center;
    transform: translate(-50%, -50%);
    height: 30rem;
    width: 26rem;
    transform: scale(1.5);
}

</style>