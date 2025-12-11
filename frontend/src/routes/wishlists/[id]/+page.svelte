<script>
    import { page } from '$app/stores';
    import { wishlistsStore, wishesStore } from '$lib/stores/data.js';
    import { goto } from '$app/navigation';



    $: wishlistId = Number($page.params.id);
    $: wishlist = $wishlistsStore.find((wl) => wl.id === wishlistId);
    $: wishlistWishes =
        $wishesStore.filter((w) => (w.wishlistIds || []).includes(wishlistId));

    // revenir vers l’écran précédent (mainscreen avec l’onglet ouvert)
    const goBack = () => {
        if (typeof history !== 'undefined' && history.length > 1) {
            history.back();
        } else {
            // fallback si la personne a ouvert le lien directement
            goto('/');
        }
    };
</script>

{#if !wishlist}
    <section class="section-card">
        <p class="empty-note">
            Вишлист не найден или был удалён.
        </p>
        <button class="back-btn" type="button" on:click={goBack}>← К спискам</button>
    </section>
{:else}
    <header class="app-header">
        <div class="h1">{wishlist.title}</div>
        <button class="icon-btn" type="button" on:click={goBack}>
            <img src="/icons/tab-gift.png" alt="К вишлистам" />
        </button>
    </header>

    <section class="section-card wishlist-open">
        <div class="wl-hero">
            <div class="wl-hero-cover">
                {#if wishlist.coverUrl}
                    <img src={wishlist.coverUrl} alt={wishlist.title} />
                {:else}
                    <img src="/icons/card.svg" alt="Подарок" />
                {/if}
            </div>
            <div class="wl-hero-main">
                <div class="wl-hero-title">{wishlist.title}</div>
                {#if wishlist.description}
                    <p class="wl-hero-desc">{wishlist.description}</p>
                {/if}
                <p class="wl-hero-meta">
                    Всего желаний: {wishlistWishes.length}
                </p>
            </div>
        </div>

        {#if wishlistWishes.length === 0}
            <p class="empty-note">
                В этом вишлисте пока нет желаний.
            </p>
        {:else}
            <div class="wish-grid">
                {#each wishlistWishes as wish}
                    <article class="wish-card">
                        <div class="wish-card-image">
                            {#if wish.imageUrl}
                                <img src={wish.imageUrl} alt={wish.title} />
                            {:else}
                                <img src="/icons/gift-ori.svg" alt="Подарок" />
                            {/if}
                        </div>
                        <div class="wish-card-body">
                            <div class="wish-title" title={wish.title}>{wish.title}</div>
                            {#if wish.price != null}
                                <div class="wish-price">{wish.price} {wish.currency}</div>
                            {/if}
                        </div>
                    </article>
                {/each}
            </div>
        {/if}
    </section>
{/if}


<style>
    /* fond gris clair derrière la carte */
    :global(body) {
        background: #f3f4f6;
    }

    .icon-btn {
        border: none;
        background: transparent;
        cursor: pointer;
        padding: 4px;
        margin-right: 4px;
    }

    .icon-btn img {
        width: 20px;
        height: 20px;
        display: block;
    }

    .back-btn {
        border: none;
        background: #eff6ff;
        color: #2563eb;
        border-radius: 999px;
        padding: 6px 12px;
        font-size: 14px;
        cursor: pointer;
    }

    /* >>> ICI : on redéfinit section-card pour cette page uniquement <<< */
    .section-card {
        margin: 12px 16px 16px;
        padding: 16px;
        border-radius: 24px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.08);
    }

    .wishlist-open .wl-hero {
        display: flex;
        gap: 10px;
        margin-bottom: 12px;
    }

    .wl-hero-cover {
        width: 60px;
        height: 60px;
        border-radius: 18px;
        overflow: hidden;
        background: #f3f4f6;
        flex-shrink: 0;
    }

    .wl-hero-cover img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    .wl-hero-main {
        flex: 1;
    }

    .wl-hero-title {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 8px;
        text-overflow: ellipsis;
    }

    .wl-hero-desc {
        font-size: 13px;
        color: #4b5563;
        margin: 0 0 4px;
    }

    .wl-hero-meta {
        font-size: 12px;
        color: #6b7280;
        margin: 0;
    }

    .wish-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 8px;
        margin-top: 10px;
    }

    .wish-card {
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        background: #ffffff;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .wish-card-image {
        height: 150px;
        background: #f3f4f6;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
    }

    .wish-card-image img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    .wish-card-body {
        padding: 8px 8px 10px;
    }

    .wish-title {
        font-size: 14px;
        font-weight: 500;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .wish-price {
        font-size: 13px;
        color: #111827;
        margin-top: 2px;
    }

    .app-header {
        padding: 0 16px;
        margin-top: 12px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }


</style>


