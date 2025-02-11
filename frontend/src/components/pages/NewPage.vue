<template>
    <div v-if="show_newpage" class="page_overlay" @click="close">
        <Spin fix v-if="loading">
            <Icon type="ios-loading" size=18 class="demo-spin-icon-load"></Icon>
            <div>Loading</div>
        </Spin>
        <Card class="card" @click.stop>
            <h1>新建工程</h1>
            <div class="newfile">
                <p>请选择.psd文件: </p>
                <Upload multiple :action="`${this.backend_url}/new-page/`" name="file"
                :format="['psd']" :before-upload="checkFileType" :on-remove="removeFile"
                class="upload-files">
                    <Button icon="ios-cloud-upload-outline">Upload files</Button>
                </Upload>
                <Button type="primary" class="submit" @click="submit">创建</Button>
            </div>
        </Card>
    </div>
</template>

<script>
import axios from 'axios';
import {mapState} from 'vuex';

export default {
    name: 'NewPage',
    props: {
        show_newpage: {
            type: Boolean,
        },
    },
    data() {
        return {
            loading: false,
        };
    },
    computed: {
        ...mapState({
            backend_url: state => state.Settings.backend_url,
        }),
    },
    methods: {
        async close() {
            this.$emit('update:show_newpage', false);
            await axios.delete(`${this.backend_url}/clear-temp/`);
        },
        async checkFileType(file) {
            const isPSD = file.name.toLowerCase().endsWith('.psd');
            if (!isPSD) {
                this.$Message.warning('请选择.psd文件');
                return false;
            }
            return true;
        },
        async removeFile(file){
            try{
                const res = await axios.delete(`${this.backend_url}/delete-temp/`, {
                    headers: {
                        'content-type': 'application/json'
                    },
                    data: {
                        page_name : file.name,
                    },
                });;
            }catch(error){
                this.$Message.error(`Error: ${error}`);
            }
        },
        async submit() {
            this.loading = true;
            try{
                const res = await axios.post(`${this.backend_url}/init-page/`);
                if (res.data.status === 'success') {
                    this.$Notice.success({
                        title: 'Success',
                        desc: `${res.data.file} 等 ${res.data.cnt} 个工程被成功创建。`
                    });
                    this.$emit('update:show_newpage', false);
                } else {
                    this.$Message.error('创建失败!');
                }
            } catch (error) {
                this.$Message.error('创建失败!');
            }finally {
                this.loading = false;
            }
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

.newfile{
    margin-top: 50px;
}

.upload-files {
    margin-top: 10px;
}

.submit {
    margin-top: 20px;
}

.demo-spin-col .circular {
        width:25px;
        height:25px;
    }
.demo-spin-icon-load{
    animation: ani-demo-spin 1s linear infinite;
}
.demo-spin-col{
    height: 100px;
    position: relative;
    border: 1px solid #eee;
    transform: scale(2);
}
</style>