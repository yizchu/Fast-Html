<template>
    <div v-if="show_settings" class="page_overlay" @click="close">
        <Card class="card" @click.stop>
            <h1>配置</h1>
            <li>Backend URL : </li>
            <div class="box">
                <input v-model="inputUrl" type="text" class="input-box"/>
                <Button type="success" ghost @click="onSave" class="action-button">
                    保存
                </Button>
                <Button type="success" ghost @click="onCancel" class="action-button">
                    撤销
                </Button>
            </div>
        </Card>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
export default {
    name: 'Settings',
    props: {
        show_settings: {
            type: Boolean,
        },
    },
    computed: {
        ...mapState({
            backend_url: state => state.Settings.backend_url,
        }),
    },
    data () {
        return {
            originUrl: '',
            inputUrl: '',
        }
    },
    created(){
        this.inputUrl = this.backend_url;
        this.originUrl = this.backend_url;
    },
    methods: {
        ...mapMutations('Settings', ['updateBackendUrl']),
        close() {
            this.$emit('update:show_settings', false);
        },
        onSave() {
            this.originUrl = this.inputUrl;
            this.updateBackendUrl(this.inputUrl);
        },
        onCancel() {
            this.inputUrl = this.originUrl;
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
    z-index: 2000;
}

.card {
    justify-content: center;
    align-items: flex-start;
    text-align: center;
    overflow: auto;
    transform: translate(-50%, -50%);
    height: 30rem;
    width: 26rem;
    transform: scale(1.5);
}

.card li {
    font-size: 16px;
    font-weight: bold;
    margin-top: 10px;
    text-align: left;
}

.card .box {
    display: flex;
    align-items: center;
    margin-top: -10px;
    margin-left:-10px;
    transform: scale(1.0);
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
</style>