<script>
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import { createEventDispatcher } from 'svelte';
    import { subscribersStore } from '$lib/stores/data.js';

    const dispatch = createEventDispatcher();

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

    const toggleBlock = (id) => {
        subscribersStore.update((list) =>
            list.map((f) =>
                f.id === id ? { ...f, blocked: !f.blocked } : f
            )
        );
    };
</script>

<header class="app-header">
    <div class="h1">Подписчики</div>
</header>

<section class="section-card">
    {#if $subscribersStore.length === 0}
        <p class="empty-note">Пока никто не подписан на вас.</p>
    {:else}
        <div class="subs-list">
            {#each $subscribersStore as f}
                <article
                        class="subs-item"
                        on:click={() =>
            dispatch('openProfile', {
              profile: {
                id: f.id,
                fullName: f.fullName,
                birthDate: f.birthDate,
                avatarUrl: f.avatarUrl || '',
                wishlistCount: 0
              }
            })
          }
                >
                    <Avatar size={44} initials={getInitials(f.fullName)} />

                    <div class="subs-main">
                        <div class="subs-title">{f.fullName}</div>
                        <div class="subs-meta">
                            {f.birthDate}
                            {#if getOccasion(f)}
                                · {getOccasion(f)}
                            {/if}
                        </div>
                    </div>

                    <button
                            class="subs-btn"
                            type="button"
                            on:click|stopPropagation={() => toggleBlock(f.id)}
                    >
                        {f.blocked ? 'Разблокировать' : 'Заблокировать'}
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
