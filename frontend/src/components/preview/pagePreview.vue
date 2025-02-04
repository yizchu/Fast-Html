<template>
      <div class="preview-pane">
        <div class="preview-header">
          <h3>实时预览</h3>
          <button @click="inspectMode = !inspectMode">
            {{ inspectMode ? '退出检查模式' : '进入检查模式' }}
          </button>
        </div>
        <div
          class="preview-content"
          ref="previewContainer"
          @mouseover="handleHover"
          @click="handleClick"
          v-html="compiledHtml"
        ></div>
      </div>

      <div v-if="selectedElement" class="inspector-pane">
        <div class="element-info">
          <h3>元素属性</h3>
          <div class="info-section">
            <h4>HTML结构</h4>
            <pre><code>{{ selectedElement.outerHTML }}</code></pre>
          </div>

          <div class="info-section">
            <h4>样式</h4>
            <div v-for="(value, key) in selectedElement.computedStyle" :key="key">
              {{ key }}: {{ value }}
            </div>
          </div>

          <div class="info-section">
            <h4>盒子模型</h4>
            <div>Width: {{ selectedElement.rect.width }}px</div>
            <div>Height: {{ selectedElement.rect.height }}px</div>
            <div>Position: ({{ selectedElement.rect.x }}, {{ selectedElement.rect.y }})</div>
          </div>
        </div>
      </div>
  </template>

<script>
    import { mapState } from 'vuex';
    import page_store from '@/store/page_store';
    export default {
        store: page_store,
        data() {
            return {
                inspectMode: false,
                selectedElement: null,
                hoveredElement: null,
                htmlCode: '<div class="demo"><h1>Hello World</h1><p>这是一个示例</p></div>',
            }
        },
        computed: {

            compiledHtml() {
                return this.htmlCode;
            }
        },
        watch: {
            inspectMode(newVal) {
                if (!newVal) {
                    this.clearHighlights()
                }
            }
        },
        methods: {
        handleHover(event) {
            if (!this.inspectMode) return
            const target = event.target
            if (target === this.$refs.previewContainer) return

            this.clearHighlights()
            this.highlightElement(target)
        },

        handleClick(event) {
            if (!this.inspectMode) return

            const target = event.target
            if (target === this.$refs.previewContainer) return

            this.selectedElement = {
            element: target,
            outerHTML: target.outerHTML,
            computedStyle: this.getFilteredStyles(target),
            rect: target.getBoundingClientRect()
            }

            event.stopPropagation()
        },

        highlightElement(element) {
            element.style.setProperty('outline', '2px solid #42b883', 'important')
            element.style.setProperty('outline-offset', '2px', 'important')
            element.style.setProperty('cursor', 'pointer', 'important')
            element.style.setProperty('position', 'relative', 'important')
            element.style.setProperty('z-index', '9999', 'important')
        },

        clearHighlights() {
            const elements = this.$refs.previewContainer.getElementsByTagName('*')
            Array.from(elements).forEach(el => {
            el.style.removeProperty('outline')
            el.style.removeProperty('outline-offset')
            el.style.removeProperty('cursor')
            el.style.removeProperty('position')
            el.style.removeProperty('z-index')
            })
        },

        getFilteredStyles(element) {
            const styles = window.getComputedStyle(element)
            const filtered = {}

            // 过滤出常用样式属性
            const allowedProperties = [
            'font-size', 'color', 'margin', 'padding',
            'width', 'height', 'display', 'position'
            ]

            allowedProperties.forEach(prop => {
            filtered[prop] = styles.getPropertyValue(prop)
            })

            return filtered
        }
        }
    }
</script>

<style scoped>
  .preview-pane {
    border: 1px solid #ccc;
    padding: 20px;
  }

  .preview-content {
    min-height: 300px;
    padding: 20px;
    border: 1px solid #eee;
    position: relative;
  }

  .inspector-pane {
    grid-column: 1 / -1;
    border-top: 1px solid #ccc;
    padding: 20px;
    background: #f5f5f5;
  }

  .info-section {
    margin-bottom: 20px;
    background: white;
    padding: 15px;
    border-radius: 4px;
  }

  pre {
    background: #1e1e1e;
    color: #dcdcdc;
    padding: 10px;
    border-radius: 4px;
    overflow-x: auto;
  }

  button {
    background: #42b883;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
  }

  .preview-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  </style>