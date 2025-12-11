<!--<script>-->
<!--    import "../app.css";-->
<!--</script>-->

<!--<slot />-->

<!--<style>-->
<!--    /* Pas de wrapper bloquant, pas de flex non désiré */-->
<!--    :global(html, body) {-->
<!--        margin: 0;-->
<!--        padding: 0;-->
<!--        height: 100%;-->
<!--        background: #ffffff;-->
<!--    }-->
<!--    .app-root {-->
<!--        /* la “carte” de la miniapp */-->
<!--        min-height: 100vh;-->
<!--        max-width: 480px;-->
<!--        margin: 0 auto;-->
<!--        background: #f9fafb;-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--    }-->

<!--</style>-->


<script>
    import "../app.css";
    import TabBar from "$lib/components/ui/TabBar.svelte";
</script>

<div class="app-root">
    <slot />

<!--    <TabBar /> &lt;!&ndash; si tu as une tab-bar &ndash;&gt;-->
</div>

