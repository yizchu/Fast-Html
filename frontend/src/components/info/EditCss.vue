<template>
    <div v-if="selected_element">
        <div class="shuttle-box">
            <div class="box">
                <h3>源列表</h3>
                <div v-for="(item, index) in sourceList" :key="'source-' + index" class="item">
                    <span>{{ item.label }}</span>
                    <input v-model="item.value" type="text" />
                </div>
            </div>
            <div class="shuttle-controls">
                <button @click="moveItemToTarget" :disabled="sourceList.length === 0">
                    &gt;&gt;
                </button>
                <button @click="moveItemToSource" :disabled="targetList.length === 0">
                    &lt;&lt;
                </button>
            </div>
            <div class="box">
                <h3>目标列表</h3>
                <div v-for="(item, index) in targetList" :key="'target-' + index" class="item">
                    <span>{{ item.label }}</span>
                    <input v-model="item.value" type="text" />
                </div>
            </div>
        </div>
    </div>
    <div v-if="selected_elements.length > 0">
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    export default {
        name: "EditCss",
        computed: {
            ...mapState({
                selected_element: state => state.Page.selected_element,
                selected_elements: state => state.Page.selected_elements,
                html_css_content: state => state.Page.html_css_content,
            }),
        },
        data() {
            return {
                sourceList: [],
                targetList: [],
            }
        },
        mounted() {
            if (this.selected_element) {
                const className = this.selected_element.className;
                const regex = new RegExp(`\\.${className}\\s*{[^}]*}`, 'g');
                try{
                    const match = this.html_css_content.match(regex)[0];
                    if (match){
                        const properties = match.match(/([\w-]+)\s*:\s*([^;]+);/g);
                        if (properties) {
                            properties.forEach(property => {
                                const [_, label, value] = property.match(/([\w-]+)\s*:\s*([^;]+);/);
                                this.targetList.push({ label, value });
                            });
                        }
                    }
                }catch(e){
                    this.targetList = [];
                    this.sourceList = [];
                }
            }
        },
        watch: {
            selected_element(newVal) {
                if (newVal) {
                    const className = this.selected_element.className;
                    const regex = new RegExp(`\\.${className}\\s*{[^}]*}`, 'g');
                    try{
                        const match = this.html_css_content.match(regex)[0];
                        if (match){
                            this.targetList = [];
                            this.sourceList = [];   // 需要改动
                            const properties = match.match(/([\w-]+)\s*:\s*([^;]+);/g);
                            if (properties) {
                                properties.forEach(property => {
                                    const [_, label, value] = property.match(/([\w-]+)\s*:\s*([^;]+);/);
                                    this.targetList.push({ label, value });
                                });
                            }
                        }
                    }catch(e){
                        this.targetList = [];
                        this.sourceList = [];
                    }
                }
            }
        },
        methods:{
            moveItemToTarget() {
                if (this.sourceList.length === 0) return;
                const item = this.sourceList.pop();
                this.targetList.push(item);
            },
            moveItemToSource() {
                if (this.targetList.length === 0) return;
                const item = this.targetList.pop();
                this.sourceList.push(item);
            },
        }
    }
</script>

<style>
.shuttle-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10%;
}

.shuttle-box .box {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.shuttle-box h3{
    text-align: center;
}

.shuttle-box .item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 8px 0;
}

.shuttle-box .item span{
    font-size: 0.9rem;
    color: #555;
}

.shuttle-box input{
    padding: 8px;
    width: 100%;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 0.9rem;
    color: #333;
    transition: border-color 0.2s ease-in-out;
}

.shuttle-box input:focus{
    border-color: #007bff;
    outline: none;
}

.shuttle-box .shuttle-controls {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
    align-items: center;
}

.shuttle-box button {
    width: 40px;
    height: 40px;
    background-color: #007bff;
    border: none;
    border-radius: 50%;
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
}

.shuttle-box button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}

.shuttle-box button:hover:not(:disabled) {
    background-color: #0056b3;
}
</style>