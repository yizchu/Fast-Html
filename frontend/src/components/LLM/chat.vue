<template>
  <div class="chat-container">
    <div class="chat-messages" ref="chatMessages">
      <div v-for="(message, index) in messages" :key="index" class="chat-message">
        <div :class="['message-content', message.sender === 'user' ? 'right-message' : 'left-message']">
          {{ message.content }}
        </div>
      </div>
    </div>
    <div class="chat-input">
      <input v-model="newMessage" placeholder="输入消息..." @keyup.enter="sendMessage">
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      newMessage: ''
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({
          sender: 'user',
          content: this.newMessage
        });
        this.newMessage = '';
        this.getAIResponse();
        this.scrollToBottom();
      }
    },
    getAIResponse() {
      setTimeout(() => {
        this.messages.push({
          sender: 'ai',
          content: '1'
        });
        this.scrollToBottom();
      }, 1000);
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const chatMessages = this.$refs.chatMessages;
        chatMessages.scrollTop = chatMessages.scrollHeight;
      });
    }
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 400px;
  width: 500px;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: hidden;
}

.chat-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

.chat-message {
  margin-bottom: 10px;
  display: flex;
}

.message-content {
  background-color: #f0f0f0;
  padding: 8px;
  border-radius: 5px;
  display: inline-block;
  max-width: 300px;
  word-wrap: break-word;
  white-space: normal;
}

.right-message {
  margin-left: auto;
  background-color: #dcf8c6;
}

.left-message {
  margin-right: auto;
  background-color: #e5f6ff;
  text-align: left;
  text-align-last: left;
}

.chat-input {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
}

.chat-input input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.chat-input button {
  padding: 8px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.chat-input button:hover {
  background-color: #0056b3;
}
</style>
