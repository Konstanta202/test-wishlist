<script>
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import TextField from '$lib/components/ui/TextField.svelte';
    import { createEventDispatcher } from 'svelte';
    import { subscriptionsStore } from '$lib/stores/data.js';

    const dispatch = createEventDispatcher();

    let query = '';

    // список берём из стора
    $: items = $subscriptionsStore;

    const filtered = () => {
        const q = query.trim().toLowerCase();
        if (!q) return items;

        return items.filter((i) => {
            const name = i.fullName?.toLowerCase() ?? '';
            const occasion =
                i.mainOccasion?.toLowerCase() ??
                i.mainWishlistTitle?.toLowerCase() ??
                i.wishlistTitle?.toLowerCase() ??
                '';
            return name.includes(q) || occasion.includes(q);
        });
    };

    const unsubscribe = (id) => {
        if (!confirm('Отписаться?')) return;
        subscriptionsStore.update((list) => list.filter((i) => i.id !== id));
    };

    const getInitials = (name) =>
        (name || '')
            .trim()
            .split(' ')
            .slice(0, 2)
            .map((p) => p[0])
            .join('')
            .toUpperCase();

    const getOccasion = (item) =>
        item.mainOccasion || item.mainWishlistTitle || item.wishlistTitle || '';
</script>

<header class="app-header">
    <div class="h1">Подписки</div>
</header>

<section class="section-card">
    <TextField bind:value={query} label="Поиск" placeholder="Имя, вишлист..." />
</section>

<section class="section-card">
    {#if items.length === 0}
        <p class="empty-note">Вы пока ни на кого не подписаны.</p>
    {:else}
        <div class="subs-list">
            {#each filtered() as item}
                <article
                        class="subs-item"
                        on:click={() =>
            dispatch('openProfile', {
              profile: {
                id: item.id,
                fullName: item.fullName,
                birthDate: item.birthDate,
                avatarUrl: item.avatarUrl || '',
                wishlistCount: 0
              }
            })
          }
                >
                    <Avatar size={44} initials={getInitials(item.fullName)} />

                    <div class="subs-main">
                        <div class="subs-title">{item.fullName}</div>
                        <div class="subs-meta">
                            {item.birthDate}
                            {#if getOccasion(item)}
                                · {getOccasion(item)}
                            {/if}
                        </div>
                    </div>

                    <button
                            class="subs-btn"
                            type="button"
                            on:click|stopPropagation={() => unsubscribe(item.id)}
                    >
                        Отписаться
                    </button>
                </article>
            {/each}
        </div>
    {/if}
</section>

<style>
    .subs-list {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .subs-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
    }

    .subs-main {
        flex: 1;
    }

    .subs-title {
        font-size: 15px;
        font-weight: 500;
    }

    .subs-meta {
        font-size: 12px;
        color: #6b7280;
    }

    .subs-btn {
        border-radius: 999px;
        border: none;
        padding: 6px 10px;
        font-size: 12px;
        background: #fee2e2;
        color: #b91c1c;
        cursor: pointer;
    }
</style>
