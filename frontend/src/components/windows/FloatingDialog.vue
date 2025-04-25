<template>
  <div
    v-if="visible"
    class="floating-dialog"
    :style="{ top: `${position.y}px`, left: `${position.x}px`, width: `${size.width}px`, height: `${size.height}px` }"
    @mousedown="bringToFront"
  >
    <div class="dialog-header" @mousedown="startDrag">
      <span>{{ title }}</span>
      <button class="close-btn" @click="closeDialog">×</button>
    </div>
    <div class="dialog-content">
      <slot></slot>
    </div>
    <div class="resize-handle" @mousedown="startResize"></div>
  </div>
</template>

<script>
export default {
  name: "FloatingDialog",
  props: {
    title: {
      type: String,
      default: "对话框",
    },
    visible: {
      type: Boolean,
      required: true,
    },
  },
  emits: ["update:visible"],
  data() {
    return {
      position: { x: 100, y: 100 },
      size: { width: 400, height: 300 },
      isDragging: false,
      isResizing: false,
      dragStart: { x: 0, y: 0 },
      resizeStart: { width: 0, height: 0, x: 0, y: 0 },
    };
  },
  methods: {
    closeDialog() {
      this.$emit("update:visible", false);
    },
    startDrag(event) {
      this.isDragging = true;
      this.dragStart = { x: event.clientX - this.position.x, y: event.clientY - this.position.y };
      document.addEventListener("mousemove", this.drag);
      document.addEventListener("mouseup", this.stopDrag);
    },
    drag(event) {
      if (this.isDragging) {
        this.position.x = event.clientX - this.dragStart.x;
        this.position.y = event.clientY - this.dragStart.y;
      }
    },
    stopDrag() {
      this.isDragging = false;
      document.removeEventListener("mousemove", this.drag);
      document.removeEventListener("mouseup", this.stopDrag);
    },
    startResize(event) {
      this.isResizing = true;
      this.resizeStart = {
        width: this.size.width,
        height: this.size.height,
        x: event.clientX,
        y: event.clientY,
      };
      document.addEventListener("mousemove", this.resize);
      document.addEventListener("mouseup", this.stopResize);
    },
    resize(event) {
      if (this.isResizing) {
        this.size.width = this.resizeStart.width + (event.clientX - this.resizeStart.x);
        this.size.height = this.resizeStart.height + (event.clientY - this.resizeStart.y);
      }
    },
    stopResize() {
      this.isResizing = false;
      document.removeEventListener("mousemove", this.resize);
      document.removeEventListener("mouseup", this.stopResize);
    },
    bringToFront() {
      const dialogs = document.querySelectorAll(".floating-dialog");
      dialogs.forEach((dialog) => (dialog.style.zIndex = 1));
      this.$el.style.zIndex = 10;
    },
  },
};
</script>

<style scoped>
.floating-dialog {
  position: absolute;
  background: #1e1e1e;
  border: 1px solid #444;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  z-index: 1;
}
.dialog-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #333;
  color: #fff;
  padding: 8px;
  cursor: move;
}
.dialog-content {
  padding: 16px;
  color: #ccc;
}
.close-btn {
  background: transparent;
  border: none;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
}
.resize-handle {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 16px;
  height: 16px;
  cursor: se-resize;
  background: #444;
}
</style>