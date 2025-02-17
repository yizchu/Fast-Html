<template>
    <div class="preview-pane">
        <PreviewHeader :Mode1="Mode1" :Mode2="Mode2" @updateMode1="Mode1 = $event" @updateMode2="Mode2 = $event"
            @zoomChanged="handleZoomChange" @toggleSidebar="toggleSidebar" />
        <iframe ref="iframe" :srcdoc="html_css_content"></iframe>
    </div>
    <div v-if="showSidebar" class="floating-sidebar"
        :style="{ top: panelPosition.top + 'px', left: panelPosition.left + 'px' }" @mousedown="startDrag">
        <h1> Body </h1>
        <Tree :data="treeData" class="tree" ref="tree" expand-node @on-contextmenu="handleContextMenu"
            @on-toggle-expand="handleExpand">
            <template #contextMenu>
                <DropdownItem @click="handleContextMenuCheck">查看/取消查看</DropdownItem>
                <DropdownItem @click="handleContextMode">选取/取消选取</DropdownItem>
            </template>
        </Tree>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import PreviewHeader from './PreviewHeader.vue';

export default {
    name: 'PagePreview',
    inheritAttrs: false,
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
            target: null,
            showSidebar: false,
            panelPosition: { top: 100, left: 100 },
            startDragPosition: { x: 0, y: 0 },
            isDragging: false,
            treeData: null,
            contextData: null,
            selectedTreeNode: null,
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
            this.fetchElements();
        };
    },
    beforeDestroy() {
        const iframe = this.$refs.iframe;
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        iframeDocument.removeEventListener('mouseover', this.handleHover);
        iframeDocument.removeEventListener('mouseleave', this.handleMouseLeave);
        iframeDocument.removeEventListener('click', this.handleClick);
    },
    watch: {
        Mode1(newVal) {
            if (!newVal) {
                try {
                    if (this.selected_element) {
                        this.selected_element.style.boxShadow = '';
                        this.selected_element.style.backgroundColor = '';
                    }
                } catch (e) { }
                this.updateEl(null);
                const previousHighlighted = document.querySelectorAll('.ivu-tree-title');
                previousHighlighted.forEach(node => {
                    node.classList.remove('selected');
                });
            }
        },
        Mode2(newVal) {
            if (!newVal) {
                this.selected_elements.forEach(target => {
                    target.style.boxShadow = '';
                    target.style.backgroundColor = '';
                });
                this.clearEls();
                const previousHighlighted = document.querySelectorAll('.ivu-tree-title');
                previousHighlighted.forEach(node => {
                    node.classList.remove('selected');
                });
            }
        },
        showSidebar(newVal) {
            if (!newVal) {
                if (this.target) {
                    if (this.target === this.selected_element || this.selected_elements.includes(this.target)) {
                        this.target.style.backgroundColor = '';
                    } else {
                        this.target.style.backgroundColor = '';
                        this.target.style.boxShadow = '';
                    }
                    this.target = null;
                }
            }
            else if (this.Mode1) {
                if (this.selected_element) {
                    this.treeData.some(rootNode => {
                        const node = this.dfsAddHighlight(rootNode, this.selected_element);
                        if (node) {
                            rootNode.expand = true;
                            this.addHighlightToTree(node);
                            this.selectedTreeNode = node;
                            return true;
                        }
                    });
                }
            }
            else if (this.Mode2) {
                this.selected_elements.forEach(targetNode => {
                    this.treeData.some(rootNode => {
                        const node = this.dfsAddHighlight(rootNode, targetNode);
                        if (node) {
                            rootNode.expand = true;
                            this.addHighlightToTree(node);
                            return true;
                        }
                    });
                });
            }
        }
    },
    methods: {
        ...mapMutations('Page', ['updateEl', 'addEls', 'removeEls', 'clearEls']),
        dfsAddHighlight(nowNode, targetNode) {
            if (nowNode.target === targetNode) {
                return nowNode;
            }
            const children = nowNode.children;
            for (let i = 0; i < children.length; i++) {
                const node = this.dfsAddHighlight(children[i], targetNode);
                if (node) {
                    children[i].expand = true;
                    return node;
                }
            }
        },
        handleZoomChange(newScale) {
            this.scale = newScale;
            this.applyZoomToIframe();
        },
        toggleSidebar(newState) {
            this.showSidebar = newState;
            if (newState) {
                this.fetchElements();
            }
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
            if (event.target.tagName == 'HTML') return;
            if (this.target && this.target !== event.target) {
                this.target.style.backgroundColor = '';
                if (!(this.target === this.selected_element || this.selected_elements.includes(this.target))) {
                    this.target.style.boxShadow = '';
                }
            }
            this.target = event.target;
            if (!(this.target === this.selected_element || this.selected_elements.includes(this.target))) {
                this.target.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
            }
            this.target.style.backgroundColor = 'rgba(0,0,255,0.1)';
        },
        handleMouseLeave() {
            if (!(this.Mode1 || this.Mode2)) return;
            if (!this.target) return;
            if (this.target === this.selected_element || this.selected_elements.includes(this.target)) {
                this.target.style.backgroundColor = '';
                this.target = null;
                return;
            }
            this.target.style.boxShadow = '';
            this.target.style.backgroundColor = '';
            this.target = null;
        },
        handleClick(event) {
            if (this.Mode1) {
                if (event.target === this.selected_element) {
                    this.removeHighlightFromTree(this.selectedTreeNode);
                    this.selected_element.style.boxShadow = '';
                    this.updateEl(null);
                } else {
                    if (this.selected_element) {
                        this.selected_element.style.boxShadow = '';
                        this.removeHighlightFromTree(this.selectedTreeNode);
                    }
                    this.updateEl(event.target);
                    this.treeData.some(rootNode => {
                        const node = this.dfsAddHighlight(rootNode, this.selected_element);
                        if (node) {
                            rootNode.expand = true;
                            this.addHighlightToTree(node);
                            this.selectedTreeNode = node;
                            return true;
                        }
                    });
                    this.target.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
                }
            } else if (this.Mode2) {
                if (this.selected_elements.includes(event.target)) {
                    this.treeData.some(rootNode => {
                        const node = this.dfsAddHighlight(rootNode, event.target);
                        if (node) {
                            rootNode.expand = true;
                            this.removeHighlightFromTree(node);
                            return true;
                        }
                    });
                    event.target.style.boxShadow = '';
                    this.removeEls(event.target);
                } else {
                    this.target.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
                    this.addEls(event.target);
                    this.treeData.some(rootNode => {
                        const node = this.dfsAddHighlight(rootNode, event.target);
                        if (node) {
                            rootNode.expand = true;
                            this.addHighlightToTree(node);
                            return true;
                        }
                    });
                }
            }
        },
        startDrag(event) {
            this.isDragging = true;
            this.startDragPosition.x = event.clientX - this.panelPosition.left;
            this.startDragPosition.y = event.clientY - this.panelPosition.top;

            document.addEventListener('mousemove', this.dragMove);
            document.addEventListener('mouseup', this.stopDrag);
        },
        dragMove(event) {
            if (!this.isDragging) return;
            this.panelPosition.left = event.clientX - this.startDragPosition.x;
            this.panelPosition.top = event.clientY - this.startDragPosition.y;
        },
        stopDrag() {
            this.isDragging = false;
            document.removeEventListener('mousemove', this.dragMove);
            document.removeEventListener('mouseup', this.stopDrag);
        },
        fetchElements() {
            const iframe = this.$refs.iframe;
            const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            const rootNode = {
                target: null,
                title: 'body',
                contextmenu: true,
                children: [],
            }
            const recursiveBuildTree = (parentNode, nowElement, tag) => {
                const children = nowElement.children;
                for (let i = 0; i < children.length; i++) {
                    const child = children[i];
                    const node = {
                        target: child,
                        title: (tag ? tag + '-' : '') + (i + 1) + ': '
                            + child.tagName.toLowerCase()
                            + (child.className ? ` class="${child.className}"` : ''
                                + (child.tagName.toLowerCase() === 'p' ? ` text="${child.innerText}"` : '')),
                        children: [],
                        contextmenu: true,
                        expand: false,
                    };
                    parentNode.children.push(node);
                    recursiveBuildTree(node, child, (tag ? tag + '-' : '') + (i + 1));
                }
            };
            const body = iframeDocument.querySelector('body');
            recursiveBuildTree(rootNode, body, '');
            this.treeData = rootNode.children;
        },
        handleContextMenu(node) {
            this.contextData = node;
        },
        handleContextMenuCheck() {
            if (this.target) {
                this.target.style.backgroundColor = '';
                if (!(this.target === this.selected_element || this.selected_elements.includes(this.target))) {
                    this.target.style.boxShadow = '';
                }
                if (this.target === this.contextData.target) {
                    this.target = null;
                    return;
                }
            }
            this.target = this.contextData.target;
            const iframe = this.$refs.iframe;
            const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
            const rect = this.target.getBoundingClientRect();
            const iframeRect = iframe.getBoundingClientRect();
            const scrollX = rect.left + iframe.contentWindow.scrollX - iframeRect.left - iframeRect.width / 2 + rect.width / 2;
            const scrollY = rect.top + iframe.contentWindow.scrollY - iframeRect.top - iframeRect.height / 2 + rect.height / 2;
            iframe.contentWindow.scrollTo(scrollX, scrollY);
            if (!(this.target === this.selected_element || this.selected_elements.includes(this.target))) {
                this.target.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
            }
            this.target.style.backgroundColor = 'rgba(0,0,255,0.1)';
        },
        addHighlightToTree(targetNode) {
            this.$nextTick(() => {
                try{
                    const treeNodes = this.$refs.tree.$el.querySelectorAll('.ivu-tree-title');
                    treeNodes.forEach(node => {
                        if (node.innerText === targetNode.title) {
                            node.classList.add('selected');
                        }
                    });
                } catch (e) {}
            });
        },
        removeHighlightFromTree(targetNode) {
            this.$nextTick(() => {
                try{
                    const treeNodes = this.$refs.tree.$el.querySelectorAll('.ivu-tree-title');
                    treeNodes.forEach(node => {
                        if (node.innerText === targetNode.title) {
                            node.classList.remove('selected');
                        }
                    });
                } catch (e) {}
            });
        },
        handleContextMode() {
            const node = this.contextData;
            const targetNode = node.target;
            if (this.Mode1) {
                if (targetNode === this.selected_element) {
                    this.selected_element.style.boxShadow = '';
                    this.updateEl(null);
                    this.removeHighlightFromTree(node);
                    this.selectedTreeNode = null;
                } else {
                    if (this.selected_element) {
                        this.selected_element.style.boxShadow = '';
                        this.removeHighlightFromTree(this.selectedTreeNode);
                    }
                    this.updateEl(targetNode);
                    this.selected_element.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
                    this.addHighlightToTree(node);
                    this.selectedTreeNode = node;
                }
            } else if (this.Mode2) {
                if (this.selected_elements.includes(targetNode)) {
                    targetNode.style.boxShadow = '';
                    this.removeEls(targetNode);
                    this.removeHighlightFromTree(node);
                } else {
                    targetNode.style.boxShadow = '0px 0px 5px 2px rgba(255, 0, 0, 0.7)';
                    this.addEls(targetNode);
                    this.addHighlightToTree(node);
                }
            }
        },
        handleExpand(node) {
            const children = node.children;
            for (let i = 0; i < children.length; i++) {
                const child = children[i];
                if (child.target == this.selected_element || this.selected_elements.includes(child.target)) {
                    this.addHighlightToTree(child);
                }
                this.handleExpand(child);
            }
        },
    }
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

.floating-sidebar {
    position: absolute;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 15px;
    width: 500px;
    height: 60vh;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    z-index: 1000;
}

@media (max-height: 800px) {
    h1 {
        font-size: 1.5rem;
    }
}

@media (max-height: 600px) {
    h1 {
        font-size: 1.25rem;
    }
}

@media (max-height: 400px) {
    h1 {
        font-size: 1rem;
    }
}

.floating-sidebar ul {
    list-style-type: none;
    padding: 5px;
}

.floating-sidebar li {
    padding: 5px;
    cursor: pointer;
    line-height: 1.5;
}

.floating-sidebar li:hover {
    background-color: #f8f9fa;
}

.floating-sidebar .ivu-tree-title {
    font-family: Monaco, Consolas, monospace;
    font-size: 13px;
}

.floating-sidebar .ivu-tree-arrow {
    transition: transform 0.2s;
}

.floating-sidebar .ivu-tree-selected>.ivu-tree-title {
    color: #2d8cf0;
    font-weight: bold;
}

.floating-sidebar .selected {
    box-shadow: 0px 0px 5px 2px rgba(255, 0, 0, 0.7);
    font-weight: bold;
    color: #000;
}

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}

.floating-sidebar .tree {
    max-height: 94%;
    overflow: auto;
}
</style>