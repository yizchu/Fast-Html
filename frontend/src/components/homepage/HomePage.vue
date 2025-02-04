<template>
    <div>
        <h1>Home Page</h1>
        <p>Welcome to the home page</p>
    </div>
</template>

<script>
export default {
    data(){
        return {
            username: this.$route.query.username,
        }
    },
    mounted() {
        this.$nextTick(() => {
            this.$Notice.info({
            title: 'Welcome back, ' + this.username,
        });
    })},
}

</script>