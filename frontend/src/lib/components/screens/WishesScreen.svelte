<script>
    import Button from '$lib/components/ui/Button.svelte';
    import TextField from '$lib/components/ui/TextField.svelte';
    import { wishesStore, wishlistsStore } from '$lib/stores/data.js';

    const iconGift = '/icons/gift3.png';
    const iconPinOn = '/icons/pin-on.png';
    const iconPinOff = '/icons/pin-off.png';
    const iconEdit = '/icons/edit.png';
    const iconTrash = '/icons/trash.png';
    const iconPlus = '/icons/add.png';

    let showForm = false;
    let editingId = null;

    let imageFile = null;
    let imagePreviewUrl = '';

    let form = {
        title: '',
        price: '',
        currency: '',
        link: '',
        description: '',
        pinned: false,
        wishlistIds: []
    };

    let errors = {
        title: '',
        price: '',
        link: ''
    };

    const currencies = ['RUB', 'BYN', 'USD', 'EUR', 'UAH', 'KZT'];

    const openForm = () => {
        showForm = true;
        editingId = null;
        form = {
            title: '',
            price: '',
            currency: '',
            link: '',
            description: '',
            pinned: false,
            wishlistIds: []
        };
        errors = { title: '', price: '', link: '' };
        imageFile = null;
        imagePreviewUrl = '';
    };

    const openEdit = (wish) => {
        showForm = true;
        editingId = wish.id;
        form = {
            title: wish.title,
            price: wish.price != null ? String(wish.price) : '',
            currency:
                wish.currency && wish.currency !== '₽'
                    ? wish.currency
                    : wish.currency
                        ? 'RUB'
                        : '',
            link: wish.link || '',
            description: wish.description || '',
            pinned: !!wish.pinned,
            wishlistIds: wish.wishlistIds || []
        };
        errors = { title: '', price: '', link: '' };
        imageFile = null;
        imagePreviewUrl = wish.imageUrl || '';
    };

    const validate = () => {
        errors = { title: '', price: '', link: '' };

        if (!form.title.trim()) {
            errors.title = 'Название обязательно';
        } else if (form.title.trim().length > 100) {
            errors.title = 'Слишком длинное название (макс. 100 символов)';
        }

        if (form.price || form.currency) {
            if (!form.price || !form.currency) {
                errors.price =
                    'Нужно указать и цену, и валюту, либо оставить оба поля пустыми';
            } else {
                const value = Number(form.price.replace(',', '.'));
                if (Number.isNaN(value) || value < 0 || value > 10000000) {
                    errors.price = 'Цена должна быть числом от 0 до 10 000 000';
                }
            }
        }

        if (form.link) {
            const re = /^https?:\/\//i;
            if (!re.test(form.link)) {
                errors.link = 'Некорректная ссылка (нужен http:// или https://)';
            }
        }

        return !errors.title && !errors.price && !errors.link;
    };

    const handleImageChange = (event) => {
        const file = event.target.files?.[0];
        if (!file) return;
        imageFile = file;
        if (imagePreviewUrl) URL.revokeObjectURL(imagePreviewUrl);
        imagePreviewUrl = URL.createObjectURL(file);
    };

    const toggleWishlistId = (id, checked) => {
        if (checked) {
            if (!form.wishlistIds.includes(id)) {
                form = { ...form, wishlistIds: [...form.wishlistIds, id] };
            }
        } else {
            form = {
                ...form,
                wishlistIds: form.wishlistIds.filter((wid) => wid !== id)
            };
        }
    };

    const saveWish = () => {
        if (!validate()) return;

        const normalizedPrice = form.price ? Number(form.price.replace(',', '.')) : null;
        const normalizedCurrency = form.currency
            ? form.currency === 'RUB'
                ? '₽'
                : form.currency
            : '';

        wishesStore.update((list) => {
            if (editingId) {
                return list.map((w) =>
                    w.id === editingId
                        ? {
                            ...w,
                            title: form.title.trim(),
                            price: normalizedPrice,
                            currency: normalizedCurrency,
                            link: form.link || '',
                            description: form.description || '',
                            imageUrl: imagePreviewUrl,
                            pinned: form.pinned,
                            wishlistIds: [...form.wishlistIds]
                        }
                        : w
                );
            }

            const newWish = {
                id: Date.now(),
                title: form.title.trim(),
                price: normalizedPrice,
                currency: normalizedCurrency,
                link: form.link || '',
                description: form.description || '',
                imageUrl: imagePreviewUrl,
                pinned: form.pinned,
                wishlistIds: [...form.wishlistIds]
            };
            return [newWish, ...list];
        });

        showForm = false;
    };

    const deleteWish = (id) => {
        if (!confirm('Удалить желание полностью?')) return;
        wishesStore.update((list) => list.filter((w) => w.id !== id));
    };

    const togglePinned = (id) => {
        wishesStore.update((list) =>
            list.map((w) =>
                w.id === id
                    ? {
                        ...w,
                        pinned: !w.pinned
                    }
                    : w
            )
        );
    };

    const sortedWishes = () => {
        const pinned = $wishesStore.filter((w) => w.pinned);
        const others = $wishesStore.filter((w) => !w.pinned);
        return [...pinned, ...others];
    };
</script>

<header class="app-header">
    <div class="h1">Все ваши желания</div>
</header>

<section class="section-card">
    {#if $wishesStore.length === 0}
        <p class="empty-note">
            У вас пока нет желаний. Нажмите «Новое желание», чтобы добавить первое.
        </p>
    {:else}
        <div class="wish-grid">
            {#each sortedWishes() as wish}
                <article class="wish-card">
                    <div class="wish-card-image">
                        {#if wish.imageUrl}
                            <img src={wish.imageUrl} alt={wish.title} />
                        {:else}
                            <img src={iconGift} alt="Подарок" />
                        {/if}

                        <button
                                type="button"
                                class="pin-btn"
                                on:click|stopPropagation={() => togglePinned(wish.id)}
                                aria-label={wish.pinned ? 'Открепить' : 'Закрепить'}
                        >
                            <img
                                    src={wish.pinned ? iconPinOn : iconPinOff}
                                    alt=""
                            />
                        </button>
                    </div>

                    <div class="wish-card-body">
                        <div class="wish-title" title={wish.title}>{wish.title}</div>
                        {#if wish.price != null}
                            <div class="wish-price">{wish.price} {wish.currency}</div>
                        {/if}
                        <div class="wish-actions">
                            <button
                                    type="button"
                                    class="icon-wrapper"
                                    on:click={() => openEdit(wish)}
                                    aria-label="Редактировать"
                            >
                                <img src={iconEdit} alt="" />
                            </button>
                            <button
                                    type="button"
                                    class="icon-wrapper"
                                    on:click={() => deleteWish(wish.id)}
                                    aria-label="Удалить"
                            >
                                <img src={iconTrash} alt="" />
                            </button>
                        </div>
                    </div>
                </article>
            {/each}
        </div>
    {/if}
</section>

<div style="padding:0 16px 12px;">
    <Button full on:click={openForm}>+ Новое желание</Button>
<!--    <Button full on:click={openForm}>-->
<!--        <img src={iconPlus} alt="" class="btn-icon" />-->
<!--        <span>Новое желание</span>-->
<!--    </Button>-->
</div>

{#if showForm}
    <div class="backdrop">
        <div class="panel">
            <h2>{editingId ? 'Редактировать желание' : 'Новое желание'}</h2>
            <div class="panel-body">
                <TextField
                        bind:value={form.title}
                        label="Название"
                        required
                        error={errors.title}
                        maxlength={100}
                />
                <div style="height:8px;"></div>
                <TextField
                        bind:value={form.link}
                        label="Ссылка на товар"
                        placeholder="https://..."
                        error={errors.link}
                        maxlength={2048}
                />
                <div style="height:8px;"></div>
                <div class="row">
                    <TextField
                            bind:value={form.price}
                            label="Цена"
                            placeholder="0"
                            error={errors.price}
                    />
                    <label class="field">
                        <div class="field-label">Валюта</div>
                        <select bind:value={form.currency}>
                            <option value="">—</option>
                            {#each currencies as c}
                                <option value={c}>{c}</option>
                            {/each}
                        </select>
                    </label>
                </div>
                <div style="height:8px;"></div>
                <label class="field">
                    <div class="field-label">Описание</div>
                    <textarea bind:value={form.description} maxlength={500} rows="3"></textarea>
                </label>

                <div style="height:4px;"></div>
                <label class="field">
                    <div class="field-label">Фотография подарка</div>
                    <input type="file" accept="image/*" on:change={handleImageChange} />
                    {#if imagePreviewUrl}
<!--                        <div class="image-preview">-->
<!--                            <img src={imagePreviewUrl} alt="Превью подарка" />-->
<!--                        </div>-->
                    {/if}
                </label>

                <div style="height:8px;"></div>
                <label class="field">
                    <div class="field-label">Закрепить</div>
                    <label
                            style="display:flex;align-items:center;gap:6px;font-size:14px;"
                    >
                        <input type="checkbox" bind:checked={form.pinned} />
                        <span>Показать желание в начале списка</span>
                    </label>
                </label>

                <div style="height:8px;"></div>
                <label class="field">
                    <div class="field-label">Добавить в вишлисты</div>

                    {#if $wishlistsStore.length === 0}
                        <p class="hint">
                            У вас пока нет вишлистов. Это желание будет сохранено в общий
                            список.
                        </p>
                    {:else}
                        <div class="wishlist-checkboxes">
                            {#each $wishlistsStore as wl}
                                <label class="checkbox-row">
                                    <input
                                            type="checkbox"
                                            checked={form.wishlistIds.includes(wl.id)}
                                            on:change={(e) =>
                                            toggleWishlistId(wl.id, e.target.checked)}
                                    />
                                    <span>{wl.title}</span>
                                </label>
                            {/each}
                        </div>
                    {/if}
                </label>

                <div class="panel-actions">
                    <Button kind="ghost" on:click={() => (showForm = false)}>Отмена</Button>
                    <Button on:click={saveWish}>Сохранить</Button>
                </div>
            </div>
        </div>
    </div>
{/if}

<style>
    .wish-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 8px;
    }

    .wish-card {
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        background: #ffffff;
        display: flex;
        flex-direction: column;
        padding: 0;
        overflow: hidden;
    }

    .wish-card-image {
        position: relative;
        height: 150px;
        border-radius: 18px 18px 0 0;
        background: #f3f4f6;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        padding: 10px;
    }

    .wish-card-image img {
        width: 100%;
        height: 100%;
        object-fit: contain; /* image plus petite, entière */
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

    .wish-actions {
        margin-top: 6px;
        display: flex;
        justify-content: flex-end;
        gap: 4px;
    }

    .icon-wrapper {
        border: none;
        background: transparent;
        padding: 2px;
        cursor: pointer;
        border-radius: 999px;
    }

    .icon-wrapper img {
        width: 18px;
        height: 18px;
        display: block;
    }

    .pin-btn {
        position: absolute;
        top: 6px;
        right: 6px;
        border: none;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 999px;
        padding: 2px;
        cursor: pointer;
    }

    .pin-btn img {
        width: 16px;
        height: 16px;
        display: block;
    }

    .btn-icon {
        width: 18px;
        height: 18px;
        margin-right: 4px;
    }

    .row {
        display: flex;
        gap: 8px;
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

    select {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 6px 8px;
        font-size: 14px;
    }

    textarea {
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 8px 10px;
        font-size: 14px;
        resize: vertical;
    }

    .wishlist-checkboxes {
        display: flex;
        flex-direction: column;
        gap: 4px;
        max-height: 120px;
        overflow-y: auto;
    }

    .checkbox-row {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 14px;
    }

    .hint {
        font-size: 12px;
        color: #6b7280;
        margin-top: 4px;
    }

    .image-preview {
        position: relative;
        margin-top: 6px;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        max-height: 50px;
    }

    .image-preview img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    /*!* ====== MODAL style identique aux вишлисты ====== *!*/
    /*.backdrop {*/
    /*    position: fixed;*/
    /*    inset: 0;*/
    /*    background: rgba(15, 23, 42, 0.35);*/
    /*    display: flex;*/
    /*    justify-content: center;*/
    /*    align-items: center;*/
    /*    z-index: 40;*/
    /*    padding: 16px;*/
    /*}*/

    /*.panel {*/
    /*    width: 100%;*/
    /*    max-width: 430px;*/
    /*    background: #fff;*/
    /*    border-radius: 24px;*/
    /*    padding: 12px 16px 16px;*/
    /*    box-shadow: 0 10px 40px rgba(15, 23, 42, 0.35);*/
    /*    max-height: calc(100vh - 40px);*/
    /*    display: flex;*/
    /*    flex-direction: column;*/
    /*    overflow-y: auto;*/
    /*    -webkit-overflow-scrolling: touch;*/
    /*    flex-shrink: 0;*/


    /*}*/

    /*.panel h2 {*/
    /*    margin: 0 0 8px;*/
    /*    font-size: 18px;*/
    /*    !*overflow-y: auto;*!*/
    /*    !*-webkit-overflow-scrolling: touch;*!*/
    /*}*/

    /*.panel-body {*/
    /*    display: flex;*/
    /*    flex-direction: column;*/
    /*    gap: 4px;*/
    /*    padding: 4px;*/
    /*    overflow-y: auto;*/
    /*    -webkit-overflow-scrolling: touch;*/
    /*    flex-shrink: 0;*/
    /*}*/

    /*.panel-actions {*/
    /*    margin-top: 10px;*/
    /*    display: flex;*/
    /*    justify-content: flex-end;*/
    /*    gap: 8px;*/
    /*    flex-shrink: 0;*/
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
        padding: 4px;
        width: 100%;
        box-sizing: border-box;
        flex-shrink: 0;
        /* petit “coussin” pour quand le clavier est ouvert */
        padding-bottom: 120px;               /* ← important pour dégager les boutons du clavier */
    }

    .panel-actions {
        margin-top: 10px;
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        flex-shrink: 0;
    }




</style>


