<template>
    <div class="preview-pane">
        <PreviewHeader
            :Mode1="Mode1" :Mode2="Mode2"
            @updateMode1="Mode1 = $event" @updateMode2="Mode2 = $event"
            @zoomChanged="handleZoomChange"
        />
        <iframe ref="iframe" :srcdoc="html_css_content"></iframe>
    </div>
</template>

<script>
    import { mapState, mapMutations } from 'vuex';
    import PreviewHeader from './PreviewHeader.vue';

    export default {
      name: 'PagePreview',
        components: {
            PreviewHeader,
        },
        computed: {
            ...mapState({
                html_css_content: state => state.Page.html_css_content,
                selected_element: state => state.Page.selected_element,
                selected_elements: state => state.Page.selected_elements,
            }),
        },
        data() {
            return {
                Mode1: false,
                Mode2: false,
                scale: 1,
            }
        },
        mounted() {
            const iframe = this.$refs.iframe;
            iframe.onload = () => {
                const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
                const body = iframeDocument.querySelector('body');
                if (body) {
                    body.style.cursor = 'default';
                }
                iframeDocument.addEventListener('mouseover', this.handleHover);
                iframeDocument.addEventListener('mouseleave', this.handleMouseLeave);
                iframeDocument.addEventListener('click', this.handleClick);
            };
        },
        watch: {
            Mode1(newVal) {
                if (!newVal) {
                    try{
                        this.selected_element.style.border = '';
                    }catch(e){}
                    this.updateEl(null);
                }
            },
            Mode2(newVal) {
                if (!newVal) {
                    this.selected_elements.forEach(target =>{
                        target.style.border = '';
                    });
                    this.clearEls();
                }
            },
        },
        methods: {
            ...mapMutations('Page', ['updateHtmlCss', 'updateEl', 'addEls', 'removeEls', 'clearEls']),
            handleZoomChange(newScale) {
                this.scale = newScale;
                this.applyZoomToIframe();
            },
            applyZoomToIframe() {
                const iframe = this.$refs.iframe;
                const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
                const body = iframeDocument.querySelector('body');
                if (body) {
                    body.style.transform = `scale(${this.scale})`;
                    body.style.transformOrigin = 'top left';
                    body.style.width = '100%';
                    body.style.height = 'auto';
                }
            },
            handleHover(event) {
                if (!(this.Mode1 || this.Mode2)) return;
                if (this.target){
                    this.target.style.backgroundColor = '';
                    if (!(this.target === this.selected_element || this.selected_elements.includes(this.target))){
                    this.target.style.border = '';
                    }
                }
                this.target = event.target;
                this.target.style.border = '0.5px dashed red';
                this.target.style.backgroundColor = 'rgba(0,0,255,0.1)';
            },
            handleMouseLeave() {
                if (!(this.Mode1 || this.Mode2)) return;
                if (!this.target) return;
                if (this.target === this.selected_element || this.selected_elements.includes(this.target))
                    return;
                this.target.style.border = '';
                this.target.style.backgroundColor = '';
                this.target = null;
            },
            handleClick(event) {
                if (this.Mode1){
                    if (event.target === this.selected_element){
                        this.selected_element.style.border = '';
                        this.updateEl(null);
                    }
                    else{
                        try{
                            this.selected_element.style.border = '';
                        }catch(e){}
                        this.updateEl(event.target);
                        this.selected_element.style.border = '0.5px dashed red';
                    }
                }
                else if (this.Mode2){
                    if (this.selected_elements.includes(event.target)){
                        event.target.style.border = '';
                        this.removeEls(event.target);
                    }
                    else{
                        event.target.style.border = '0.5px dashed red';
                        this.addEls(event.target);
                    }
                }
            },
        },
    }
</script>

<style>
.preview-pane {
    height: 100vh;
    border: 1px solid #ccc;
    padding: 20px;
    overflow: hidden;
    position: relative;
    justify-content: flex-end;
}

.preview-pane iframe {
    width: 100%;
    height: 95%;
    overflow: auto;
    box-sizing: border-box;
    border: 1px solid #ccc;
}
</style>