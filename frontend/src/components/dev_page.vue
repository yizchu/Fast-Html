<template>
    <PagesOverview />
    <pagePreview />
</template>

<script>
    import PagesOverview from './pages/pages_overview.vue'
    import pagePreview from './preview/pagePreview.vue'


    export default {
        components: {
            PagesOverview,
            pagePreview,
        },

    }
</script>
