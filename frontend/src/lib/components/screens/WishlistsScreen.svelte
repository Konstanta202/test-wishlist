<script>
    import Button from '$lib/components/ui/Button.svelte';
    import TextField from '$lib/components/ui/TextField.svelte';
    import { wishlistsStore, wishesStore } from '$lib/stores/data.js';
    import { goto } from '$app/navigation';

    const ICON_EDIT = '/icons/edit.png';
    const ICON_TRASH = '/icons/trash.png';
    const ICON_GIFT = '/icons/card.svg';

    let showForm = false;
    let editingId = null;
    let coverPreviewUrl = '';

    let form = {
        title: '',
        description: '',
        privacy: 'private'
    };

    let errors = {
        title: ''
    };

    const openCreate = () => {
        showForm = true;
        editingId = null;
        form = { title: '', description: '', privacy: 'private' };
        errors = { title: '' };
        coverPreviewUrl = '';
    };

    const openEdit = (wl) => {
        showForm = true;
        editingId = wl.id;
        form = {
            title: wl.title,
            description: wl.description || '',
            privacy: wl.privacy
        };
        errors = { title: '' };
        coverPreviewUrl = wl.coverUrl || '';
    };

    const handleCoverChange = (event) => {
        const file = event.target.files?.[0];
        if (!file) return;
        if (coverPreviewUrl) URL.revokeObjectURL(coverPreviewUrl);
        coverPreviewUrl = URL.createObjectURL(file);
    };

    const validate = () => {
        errors.title = '';
        const t = form.title.trim();
        if (!t) {
            errors.title = 'Название обязательно';
        } else if (t.length > 50) {
            errors.title = 'Максимум 50 символов';
        }
        return !errors.title;
    };

    const save = () => {
        if (!validate()) return;

        wishlistsStore.update((list) => {
            if (editingId) {
                return list.map((wl) =>
                    wl.id === editingId
                        ? {
                            ...wl,
                            title: form.title.trim(),
                            description: form.description,
                            privacy: form.privacy,
                            coverUrl: coverPreviewUrl
                        }
                        : wl
                );
            }

            const newId = Date.now();
            return [
                ...list,
                {
                    id: newId,
                    title: form.title.trim(),
                    description: form.description,
                    privacy: form.privacy,
                    coverUrl: coverPreviewUrl
                }
            ];
        });

        showForm = false;
    };

    const remove = (id) => {
        if (!confirm('Удалить вишлист?')) return;

        wishlistsStore.update((list) => list.filter((wl) => wl.id !== id));

        // убрать этот id из желаний
        wishesStore.update((list) =>
            list.map((w) => ({
                ...w,
                wishlistIds: (w.wishlistIds || []).filter((wid) => wid !== id)
            }))
        );
    };

    const privacyLabel = (p) => {
        if (p === 'public') return 'Виден всем';
        if (p === 'restricted') return 'Для определённых пользователей';
        return 'Виден только вам';
    };

    // пересчитываем количество желаний в каждом списке
    const getWishlistCount = (wishlistId) =>
        $wishesStore.filter((w) => (w.wishlistIds || []).includes(wishlistId))
            .length;

    const openWishlist = (id) => {
        // TODO: страница «Открыть вишлист»
        // например /wishlists/[id]
        goto(`/wishlists/${id}`);
    };

    // const openWishlist = (id) => {
    //     // on ne navigue plus, on délègue au parent (mainscreen)
    //     dispatch('openWishlist', { id });
    // };

</script>

<header class="app-header">
    <div class="h1">Все ваши вишлисты</div>
</header>

<section class="section-card">
    {#if $wishlistsStore.length === 0}
        <p class="empty-note">
            У вас пока нет вишлистов. Создайте первый, чтобы сгруппировать свои желания.
        </p>
    {:else}
        <div class="wishlist-list">
            {#each $wishlistsStore as wl}
                <div
                        class="wishlist-item"
                        role="button"
                        tabindex="0"
                        on:click={() => openWishlist(wl.id)}
                        on:keydown={(e) =>
                        (e.key === 'Enter' || e.key === ' ') && openWishlist(wl.id)}
                >
                    <div class="wishlist-cover">
                        {#if wl.coverUrl}
                            <img src={wl.coverUrl} alt={wl.title} />
                        {:else}
                            <img src={ICON_GIFT} alt="Подарок" />
                        {/if}
                    </div>

                    <div class="wishlist-main">
                        <div class="wishlist-title" title={wl.title}>{wl.title}</div>
                        <div class="wishlist-meta">
                            <span>{privacyLabel(wl.privacy)}</span>
                            <span> · {getWishlistCount(wl.id)} жел.</span>
                        </div>
                    </div>

                    <div class="wishlist-actions">
                        <button
                                type="button"
                                class="icon-wrapper"
                                on:click|stopPropagation={() => openEdit(wl)}
                                aria-label="Редактировать вишлист"
                        >
                            <img src={ICON_EDIT} alt="" class="icon-btn" />
                        </button>
                        <button
                                type="button"
                                class="icon-wrapper"
                                on:click|stopPropagation={() => remove(wl.id)}
                                aria-label="Удалить вишлист"
                        >
                            <img src={ICON_TRASH} alt="" class="icon-btn" />
                        </button>
                    </div>
                </div>
            {/each}
        </div>
    {/if}
</section>

<div style="padding:0 16px 12px;">
    <Button full on:click={openCreate}>+ Создать вишлист</Button>
</div>

{#if showForm}
    <div class="backdrop">
        <div class="panel">
            <h2>{editingId ? 'Редактировать вишлист' : 'Новый вишлист'}</h2>
            <div class="panel-body">
                <TextField
                        bind:value={form.title}
                        label="Название"
                        maxlength={50}
                        required
                        error={errors.title}
                />
                <div style="height:8px;"></div>

                <label class="field">
                    <div class="field-label">Описание</div>
                    <textarea
                            bind:value={form.description}
                            maxlength={250}
                            rows="3"
                    ></textarea>
                </label>

                <div style="height:8px;"></div>
                <label class="field">
                    <div class="field-label">Приватность</div>
                    <select bind:value={form.privacy}>
                        <option value="private">Виден только вам</option>
                        <option value="restricted">Для определённых пользователей</option>
                        <option value="public">Виден всем</option>
                    </select>
                </label>

                <p class="hint">
                    Для приватных списков ссылка не генерируется.
                    Для «определённых пользователей» доступ даётся по заявке.
                </p>

                <div style="height:8px;"></div>
                <label class="field">
                    <div class="field-label">Обложка списка</div>
                    <input type="file" accept="image/*" on:change={handleCoverChange} />
                    {#if coverPreviewUrl}
<!--                        <div class="cover-preview">-->
<!--                            <img src={coverPreviewUrl} alt="Превью обложки" />-->
<!--                        </div>-->
                    {/if}
                </label>

                <div class="panel-actions">
                    <Button kind="ghost" on:click={() => (showForm = false)}
                    >Отмена</Button
                    >
                    <Button on:click={save}>Сохранить</Button>
                </div>
            </div>
        </div>
    </div>
{/if}

<style>
    .wishlist-list {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .wishlist-item {
        display: flex;
        gap: 10px;
        align-items: center;
        padding: 8px;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        cursor: pointer;
        width: 100%;
        text-align: left;
    }

    .wishlist-item:focus-visible {
        outline: 2px solid #2563eb;
        outline-offset: 2px;
    }

    .wishlist-cover {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        background: #f3f4f6;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        overflow: hidden;
    }

    .wishlist-cover img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .wishlist-main {
        flex: 1;
    }

    .wishlist-title {
        font-size: 15px;
        font-weight: 500;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }

    .wishlist-meta {
        font-size: 12px;
        color: #6b7280;
        margin-top: 2px;
    }

    .wishlist-actions {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .icon-wrapper {
        border: none;
        background: transparent;
        cursor: pointer;
        padding: 4px;
        border-radius: 999px;
    }

    .icon-btn {
        width: 18px;
        height: 18px;
        display: block;
    }

    /*.backdrop {*/
    /*    position: fixed;*/
    /*    inset: 0;*/
    /*    background: rgba(15, 23, 42, 0.35);*/
    /*    display: flex;*/
    /*    justify-content: center;*/
    /*    align-items: center;*/
    /*    z-index: 40;*/
    /*    padding: 16px;*/
    /*    overflow-y: auto;*/
    /*    -webkit-overflow-scrolling: touch;*/

    /*}*/

    /*.panel {*/
    /*    width: 100%;*/
    /*    max-width: 430px;*/
    /*    max-height: 90vh;*/
    /*    background: #fff;*/
    /*    border-radius: 24px;*/
    /*    padding: 12px 16px 16px;*/
    /*    box-shadow: 0 10px 40px rgba(15, 23, 42, 0.35);*/
    /*    display: flex;*/
    /*    flex-direction: column;*/
    /*    overflow-y: auto;*/
    /*    -webkit-overflow-scrolling: touch;*/
    /*}*/

    /*.panel h2 {*/
    /*    margin: 0 0 8px;*/
    /*    font-size: 18px;*/
    /*    flex-shrink: 0;*/

    /*}*/

    /*.panel-body {*/
    /*    display: flex;*/
    /*    flex-direction: column;*/
    /*    gap: 4px;*/
    /*    padding-right: 4px;*/
    /*    overflow-y: auto;*/
    /*    -webkit-overflow-scrolling: touch;*/
    /*}*/


    .backdrop {
        position: fixed;
        inset: 0;
        background: rgba(15, 23, 42, 0.35);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;         /* ← au lieu de center */
        padding: 24px 16px 16px;
        box-sizing: border-box;
        z-index: 40;
        overflow-y: auto;                    /* ← le backdrop peut scroller */
        -webkit-overflow-scrolling: touch;
    }

    .panel {
        width: 100%;
        max-width: 430px;
        background: #fff;
        border-radius: 24px;
        padding: 12px 16px 16px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.35);
        display: flex;
        flex-direction: column;
        /* plus de max-height/overflow ici : on laisse le backdrop gérer le scroll */
    }

    .panel h2 {
        margin: 0 0 8px;
        font-size: 18px;
        flex-shrink: 0;
    }

    .panel-body {
        display: flex;
        flex-direction: column;
        gap: 4px;
        width: 100%;
        box-sizing: border-box;
        flex-shrink: 0;
        /* petit “coussin” pour quand le clavier est ouvert */
        /* ← important pour dégager les boutons du clavier */
        padding: 4px 4px 120px;
    }

    .panel-actions {
        margin-top: 10px;
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        flex-shrink: 0;
    }



    .field {
        display: flex;
        flex-direction: column;
        gap: 4px;
        font-size: 14px;
    }

    .field-label {
        color: #374151;
    }

    textarea {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 8px 10px;
        font-size: 14px;
        resize: vertical;
    }

    select {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 6px 8px;
        font-size: 14px;


    }

    .hint {
        font-size: 12px;
        color: #6b7280;
        margin-top: 4px;

    }

    /*.cover-preview {*/
    /*    margin-top: 6px;*/
    /*    border-radius: 12px;*/
    /*    border: 1px solid #e5e7eb;*/
    /*    overflow: hidden;*/
    /*    max-height: 140px;*/
    /*}*/

    /*.cover-preview img {*/
    /*    width: 100%;*/
    /*    height: 100%;*/
    /*    object-fit: cover;*/
    /*}*/
</style>
