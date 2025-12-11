<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->

<!--    export let profile; // { id, fullName, birthDate, avatarUrl, wishlistCount }-->

<!--    const dispatch = createEventDispatcher();-->

<!--    const goBack = () => dispatch('back');-->

<!--    const openWishlist = (id) => {-->
<!--        alert('Открыть вишлист (заглушка), id=' + id);-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--<section class="section-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar size={72} src={profile.avatarUrl} initials={profile.fullName.split(' ').map(n => n[0]).join('').toUpperCase()} />-->
<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->
<!--            <Button kind="ghost" on:click={() => alert('Подписаться / Отписаться (заглушка)')}>-->
<!--                Подписаться-->
<!--            </Button>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Публичные вишлисты · {profile.wishlistCount}</div>-->
<!--    </div>-->
<!--    <div class="empty-note">-->
<!--        Здесь будут публичные вишлисты этого пользователя. Сейчас это заглушка.-->
<!--    </div>-->
<!--    <Button kind="ghost" full on:click={() => openWishlist('demo')}>-->
<!--        Открыть пример вишлиста-->
<!--    </Button>-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    <Button kind="ghost" full on:click={goBack}>Назад</Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->
<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->
<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->
<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->
<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--    }-->
<!--</style>-->


<!--<script>-->
<!--    import { onMount } from 'svelte';-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import { makeProfileUrl } from '$lib/stores/data.js';-->

<!--    // profile vient de SubscriptionsScreen / SubscribersScreen-->
<!--    // { id, fullName, birthDate, avatarUrl, publicWishlists?, subscriptions? }-->
<!--    export let profile;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    let tg = null;-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {-->
<!--            tg = window.Telegram.WebApp;-->
<!--        }-->
<!--    });-->

<!--    // Liste des wislists publics de cet utilisateur (pour l’UI)-->
<!--    $: publicWishlists = profile?.publicWishlists ?? [];-->
<!--    $: subscriptions = profile?.subscriptions ?? [];-->

<!--    const shareInTelegram = () => {-->
<!--        const url = makeProfileUrl(profile.id);-->
<!--        const text = `Профиль ${profile.fullName} в «Подари мне»`;-->

<!--        const shareUrl =-->
<!--            `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;-->

<!--        if (tg?.openTelegramLink) {-->
<!--            tg.openTelegramLink(shareUrl);-->
<!--        } else {-->
<!--            // dev dans le navigateur-->
<!--            window.open(shareUrl, '_blank');-->
<!--        }-->
<!--    };-->

<!--    const copyLink = async () => {-->
<!--        const url = makeProfileUrl(profile.id);-->
<!--        try {-->
<!--            await navigator.clipboard.writeText(url);-->
<!--            alert('Ссылка на профиль скопирована');-->
<!--        } catch (e) {-->
<!--            alert('Не удалось скопировать ссылку');-->
<!--        }-->
<!--    };-->

<!--    const openExampleWishlist = () => {-->
<!--        alert('Открыть пример вишлиста (заглушка)');-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--<section class="section-card profile-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar-->
<!--                size={72}-->
<!--                src={profile.avatarUrl}-->
<!--                initials={profile.fullName-->
<!--        .split(' ')-->
<!--        .map((n) => n[0])-->
<!--        .join('')-->
<!--        .toUpperCase()}-->
<!--        />-->

<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->

<!--            <div class="profile-actions">-->
<!--                <Button on:click={() => alert('Подписаться / Отписаться (заглушка)')}>-->
<!--                    Подписаться-->
<!--                </Button>-->
<!--                <Button kind="ghost" on:click={() => alert('Посмотреть анкету (заглушка)')}>-->
<!--                    Посмотреть анкету-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">-->
<!--            Вишлисты пользователя · {publicWishlists.length}-->
<!--        </div>-->
<!--        &lt;!&ndash; lien "Показать все вишлисты" (заглушка) &ndash;&gt;-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={() => alert('Показать все вишлисты (заглушка)')}-->
<!--        >-->
<!--            Показать все вишлисты-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if publicWishlists.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Здесь пока нет публичных вишлистов.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="wishlists-list">-->
<!--            {#each publicWishlists as wl}-->
<!--                <article class="wishlist-row">-->
<!--                    <div class="wishlist-icon">-->
<!--                        <img src={wl.iconUrl ?? '/icons/card.svg'} alt="" />-->
<!--                    </div>-->
<!--                    <div class="wishlist-main">-->
<!--                        <div class="wishlist-title">{wl.title}</div>-->
<!--                        <div class="wishlist-meta">-->
<!--                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}-->
<!--                            {#if typeof wl.wishesCount === 'number'}-->
<!--                                · {wl.wishesCount} жел.-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Подписки</div>-->
<!--    </div>-->

<!--    {#if subscriptions.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Этот пользователь пока ни на кого не подписан.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="subs-list">-->
<!--            {#each subscriptions as sub}-->
<!--                <article class="sub-row">-->
<!--                    <Avatar-->
<!--                            size={40}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--              .split(' ')-->
<!--              .map((n) => n[0])-->
<!--              .join('')-->
<!--              .toUpperCase()}-->
<!--                    />-->
<!--                    <div class="sub-main">-->
<!--                        <div class="sub-name">{sub.fullName}</div>-->
<!--                        <div class="sub-meta">-->
<!--                            {sub.birthDate} · {sub.wishlistTitle}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Поделиться профилем</div>-->
<!--    </div>-->

<!--    <p class="share-text">-->
<!--        Отправьте ссылку на этот профиль, чтобы друзья могли видеть его вишлисты.-->
<!--    </p>-->

<!--    <Button full on:click={shareInTelegram}>-->
<!--        Поделиться в Telegram-->
<!--    </Button>-->

<!--    <div style="height:8px;"></div>-->

<!--    &lt;!&ndash; style bleu pâle comme le bouton "Назад" &ndash;&gt;-->
<!--    <Button full kind="ghost" on:click={copyLink}>-->
<!--        Скопировать ссылку-->
<!--    </Button>-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Назад-->
<!--    </Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-card {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->

<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--        gap: 8px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .link-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        padding: 0;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .wishlists-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .wishlist-icon {-->
<!--        width: 40px;-->
<!--        height: 40px;-->
<!--        border-radius: 14px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        overflow: hidden;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlist-icon img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .wishlist-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .wishlist-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .subs-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .sub-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .sub-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .sub-name {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .sub-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .share-text {-->
<!--        font-size: 14px;-->
<!--        color: #4b5563;-->
<!--        margin-bottom: 12px;-->
<!--    }-->
<!--</style>-->


<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->

<!--    // Профиль приходит из SubscriptionsScreen / SubscribersScreen-->
<!--    // { id, fullName, birthDate, avatarUrl, publicWishlists?, subscriptions?, isSubscribed? }-->
<!--    export let profile;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    let isSubscribed = !!profile?.isSubscribed;-->

<!--    // Вишлисты и подписки (мок-данные из profile или пустые)-->
<!--    $: publicWishlists = profile?.publicWishlists ?? [];-->
<!--    $: subscriptions   = profile?.subscriptions ?? [];-->

<!--    const toggleSubscribe = () => {-->
<!--        isSubscribed = !isSubscribed;-->
<!--        // позже тут будет API-->
<!--        // сейчас просто заглушка-->
<!--        // alert(isSubscribed ? 'Вы подписались на пользователя' : 'Вы отписались от пользователя');-->
<!--    };-->

<!--    const openQuestionnaire = () => {-->
<!--        // заглушка для анкеты-->
<!--        // alert('Посмотреть анкету (заглушка)');-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--&lt;!&ndash; КАРТОЧКА ПРОФИЛЯ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card profile-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar-->
<!--                size={72}-->
<!--                src={profile.avatarUrl}-->
<!--                initials={profile.fullName-->
<!--                .split(' ')-->
<!--                .map((n) => n[0])-->
<!--                .join('')-->
<!--                .toUpperCase()}-->
<!--        />-->

<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->

<!--            <div class="profile-actions">-->
<!--                <Button on:click={toggleSubscribe}>-->
<!--                    <img-->
<!--                            src={isSubscribed ? '/icons/bell-on.png' : '/icons/bell-off.png'}-->
<!--                            alt=""-->
<!--                            class="icon-16"-->
<!--                    />-->
<!--                    <span>{isSubscribed ? 'Вы подписаны' : 'Подписаться'}</span>-->
<!--                </Button>-->

<!--                <Button kind="ghost" on:click={openQuestionnaire}>-->
<!--                    Посмотреть анкету-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--&lt;!&ndash; ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ · {publicWishlists.length}</div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={() => {/* Показать все вишлисты (заглушка) */}}-->
<!--        >-->
<!--            Показать все вишлисты-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if publicWishlists.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Здесь пока нет публичных вишлистов.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="wishlists-list">-->
<!--            {#each publicWishlists as wl}-->
<!--                <article class="wishlist-row">-->
<!--                    <div class="wishlist-icon">-->
<!--                        <img src={wl.iconUrl ?? '/icons/wishlist-card.png'} alt="" />-->
<!--                    </div>-->
<!--                    <div class="wishlist-main">-->
<!--                        <div class="wishlist-title">{wl.title}</div>-->
<!--                        <div class="wishlist-meta">-->
<!--                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}-->
<!--                            {#if typeof wl.wishesCount === 'number'}-->
<!--                                · {wl.wishesCount} жел.-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; ПОДПИСКИ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">ПОДПИСКИ</div>-->
<!--    </div>-->

<!--    {#if subscriptions.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Этот пользователь пока ни на кого не подписан.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="subs-list">-->
<!--            {#each subscriptions as sub}-->
<!--                <article class="sub-row">-->
<!--                    <Avatar-->
<!--                            size={40}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--                            .split(' ')-->
<!--                            .map((n) => n[0])-->
<!--                            .join('')-->
<!--                            .toUpperCase()}-->
<!--                    />-->
<!--                    <div class="sub-main">-->
<!--                        <div class="sub-name">{sub.fullName}</div>-->
<!--                        <div class="sub-meta">-->
<!--                            {sub.birthDate}-->
<!--                            {#if sub.wishlistTitle}-->
<!--                                · {sub.wishlistTitle}-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Назад-->
<!--    </Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-card {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->

<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .icon-16 {-->
<!--        width: 16px;-->
<!--        height: 16px;-->
<!--        margin-right: 4px;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--        gap: 8px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .link-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        padding: 0;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .wishlists-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .wishlist-icon {-->
<!--        width: 40px;-->
<!--        height: 40px;-->
<!--        border-radius: 14px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        overflow: hidden;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlist-icon img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .wishlist-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .wishlist-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .subs-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .sub-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .sub-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .sub-name {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .sub-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .share-text {-->
<!--        font-size: 14px;-->
<!--        color: #4b5563;-->
<!--        margin-bottom: 12px;-->
<!--    }-->
<!--</style>-->


<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->

<!--    // Профиль приходит из SubscriptionsScreen / SubscribersScreen-->
<!--    // { id, fullName, birthDate, avatarUrl, publicWishlists?, subscriptions?, isSubscribed?, questionnaire? }-->
<!--    export let profile;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    // состояние подписки только в UI (потом здесь будет запрос к API)-->
<!--    let isSubscribed = !!profile?.isSubscribed;-->

<!--    // мок-данные для вишлистов и подписок-->
<!--    $: publicWishlists = profile?.publicWishlists ?? [];-->
<!--    $: subscriptions   = profile?.subscriptions ?? [];-->

<!--    const toggleSubscribe = () => {-->
<!--        isSubscribed = !isSubscribed;-->
<!--        // TODO: позже вызвать API-->
<!--    };-->

<!--    const openQuestionnaire = () => {-->
<!--        // TODO: открыть отдельный экран анкеты-->
<!--        // пока заглушка-->
<!--        alert('Открыть полную анкету (заглушка)');-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--&lt;!&ndash; КАРТОЧКА ПРОФИЛЯ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card profile-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar-->
<!--                size={72}-->
<!--                src={profile.avatarUrl}-->
<!--                initials={profile.fullName-->
<!--                .split(' ')-->
<!--                .map((n) => n[0])-->
<!--                .join('')-->
<!--                .toUpperCase()}-->
<!--        />-->

<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->

<!--            <div class="profile-actions">-->
<!--                <Button on:click={toggleSubscribe}>-->
<!--                    <img-->
<!--                            src={isSubscribed ? '/icons/bell-on.png' : '/icons/bell-off.png'}-->
<!--                            alt=""-->
<!--                            class="icon-16"-->
<!--                    />-->
<!--                    <span>{isSubscribed ? 'Вы подписаны' : 'Подписаться'}</span>-->
<!--                </Button>-->

<!--                <Button kind="ghost" on:click={openQuestionnaire}>-->
<!--                    Посмотреть анкету-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--&lt;!&ndash; ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ · {publicWishlists.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={() => {/* Показать все вишлисты (заглушка) */}}-->
<!--        >-->
<!--            Показать все вишлисты-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if publicWishlists.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Здесь пока нет публичных вишлистов.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="wishlists-list">-->
<!--            {#each publicWishlists as wl}-->
<!--                <article class="wishlist-row">-->
<!--                    <div class="wishlist-icon">-->
<!--                        <img src={wl.iconUrl ?? '/icons/wishlist-card.png'} alt="" />-->
<!--                    </div>-->
<!--                    <div class="wishlist-main">-->
<!--                        <div class="wishlist-title">{wl.title}</div>-->
<!--                        <div class="wishlist-meta">-->
<!--                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}-->
<!--                            {#if typeof wl.wishesCount === 'number'}-->
<!--                                · {wl.wishesCount} жел.-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; ПОДПИСКИ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ПОДПИСКИ · {subscriptions.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={() => {/* Показать всех (заглушка) */}}-->
<!--        >-->
<!--            Показать всех-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if subscriptions.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Этот пользователь пока ни на кого не подписан.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="subs-list">-->
<!--            {#each subscriptions as sub}-->
<!--                <article class="sub-row">-->
<!--                    <Avatar-->
<!--                            size={40}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--                            .split(' ')-->
<!--                            .map((n) => n[0])-->
<!--                            .join('')-->
<!--                            .toUpperCase()}-->
<!--                    />-->
<!--                    <div class="sub-main">-->
<!--                        <div class="sub-name">{sub.fullName}</div>-->
<!--                        <div class="sub-meta">-->
<!--                            {sub.birthDate}-->
<!--                            {#if sub.wishlistTitle}-->
<!--                                · {sub.wishlistTitle}-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; АНКЕТА ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Интересы и запреты</div>-->
<!--    </div>-->

<!--    {#if profile.questionnaire &&-->
<!--    ((profile.questionnaire.interests && profile.questionnaire.interests.length) ||-->
<!--        (profile.questionnaire.noGifts && profile.questionnaire.noGifts.length))}-->
<!--        {#if profile.questionnaire.interests?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Что дарить:</div>-->
<!--                <ul class="q-list">-->
<!--                    {#each profile.questionnaire.interests as item}-->
<!--                        <li>{item}</li>-->
<!--                    {/each}-->
<!--                </ul>-->
<!--            </div>-->
<!--        {/if}-->

<!--        {#if profile.questionnaire.noGifts?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Чего лучше не дарить:</div>-->
<!--                <ul class="q-list">-->
<!--                    {#each profile.questionnaire.noGifts as item}-->
<!--                        <li>{item}</li>-->
<!--                    {/each}-->
<!--                </ul>-->
<!--            </div>-->
<!--        {/if}-->

<!--        <Button kind="ghost" full on:click={openQuestionnaire}>-->
<!--            Посмотреть полную анкету-->
<!--        </Button>-->
<!--    {:else}-->
<!--        <p class="empty-note">-->
<!--            Пользователь ещё не заполнил анкету.-->
<!--        </p>-->
<!--    {/if}-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    &lt;!&ndash; тот же бледно-голубой стиль, что и в других экранах &ndash;&gt;-->
<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Назад-->
<!--    </Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-card {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->

<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .icon-16 {-->
<!--        width: 16px;-->
<!--        height: 16px;-->
<!--        margin-right: 4px;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--        gap: 8px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .section-title-with-icon {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 6px;-->
<!--        font-size: 14px;-->
<!--        font-weight: 600;-->
<!--        text-transform: uppercase;-->
<!--    }-->

<!--    .section-icon {-->
<!--        width: 18px;-->
<!--        height: 18px;-->
<!--    }-->

<!--    .link-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        padding: 0;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .wishlists-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .wishlist-icon {-->
<!--        width: 40px;-->
<!--        height: 40px;-->
<!--        border-radius: 14px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        overflow: hidden;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlist-icon img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .wishlist-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .wishlist-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .subs-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .sub-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .sub-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .sub-name {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .sub-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .q-block {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .q-label {-->
<!--        font-size: 13px;-->
<!--        font-weight: 600;-->
<!--        margin-bottom: 4px;-->
<!--    }-->

<!--    .q-list {-->
<!--        margin: 0;-->
<!--        padding-left: 18px;-->
<!--        font-size: 13px;-->
<!--        color: #374151;-->
<!--    }-->

<!--    .q-list li + li {-->
<!--        margin-top: 2px;-->
<!--    }-->

<!--    .share-text {-->
<!--        font-size: 14px;-->
<!--        color: #4b5563;-->
<!--        margin-bottom: 12px;-->
<!--    }-->
<!--</style>-->


<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->

<!--    // Профиль другого пользователя-->
<!--    // {-->
<!--    //   id, fullName, birthDate, avatarUrl,-->
<!--    //   publicWishlists?, subscriptions?,-->
<!--    //   isSubscribed?, questionnaire?-->
<!--    // }-->
<!--    export let profile;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    // локальное состояние подписки (потом заменишь на API)-->
<!--    let isSubscribed = !!profile?.isSubscribed;-->

<!--    // мок-данные-->
<!--    $: publicWishlists = profile?.publicWishlists ?? [];-->
<!--    $: subscriptions   = profile?.subscriptions ?? [];-->

<!--    // клик по "Подписаться / Вы подписаны"-->
<!--    const toggleSubscribe = () => {-->
<!--        isSubscribed = !isSubscribed;-->

<!--        // даём знать наверх (MainScreen / parent)-->
<!--        dispatch('toggle-subscribe', {-->
<!--            profileId: profile.id,-->
<!--            value: isSubscribed-->
<!--        });-->
<!--    };-->

<!--    // клик по "Посмотреть анкету" или "Посмотреть полную анкету"-->
<!--    const openQuestionnaire = () => {-->
<!--        dispatch('open-questionnaire', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->

<!--    // клик по "Показать все вишлисты"-->
<!--    const showAllWishlists = () => {-->
<!--        dispatch('show-all-wishlists', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->

<!--    // клик по "Показать всех" (подписки)-->
<!--    const showAllSubscriptions = () => {-->
<!--        dispatch('show-all-subscriptions', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--&lt;!&ndash; КАРТОЧКА ПРОФИЛЯ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card profile-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar-->
<!--                size={72}-->
<!--                src={profile.avatarUrl}-->
<!--                initials={profile.fullName-->
<!--                .split(' ')-->
<!--                .map((n) => n[0])-->
<!--                .join('')-->
<!--                .toUpperCase()}-->
<!--        />-->

<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->

<!--            <div class="profile-actions">-->
<!--                <Button on:click={toggleSubscribe}>-->
<!--                    <img-->
<!--                            src={isSubscribed ? '/icons/bell-on.png' : '/icons/bell-off.png'}-->
<!--                            alt=""-->
<!--                            class="icon-16"-->
<!--                    />-->
<!--                    <span>{isSubscribed ? 'Вы подписаны' : 'Подписаться'}</span>-->
<!--                </Button>-->

<!--                <Button kind="ghost" on:click={openQuestionnaire}>-->
<!--                    Посмотреть анкету-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--&lt;!&ndash; ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ · {publicWishlists.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={showAllWishlists}-->
<!--        >-->
<!--            Показать все вишлисты-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if publicWishlists.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Здесь пока нет публичных вишлистов.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="wishlists-list">-->
<!--            {#each publicWishlists as wl}-->
<!--                <article class="wishlist-row">-->
<!--                    <div class="wishlist-icon">-->
<!--                        <img src={wl.iconUrl ?? '/icons/wishlist-card.png'} alt="" />-->
<!--                    </div>-->
<!--                    <div class="wishlist-main">-->
<!--                        <div class="wishlist-title">{wl.title}</div>-->
<!--                        <div class="wishlist-meta">-->
<!--                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}-->
<!--                            {#if typeof wl.wishesCount === 'number'}-->
<!--                                · {wl.wishesCount} жел.-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; ПОДПИСКИ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ПОДПИСКИ · {subscriptions.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={showAllSubscriptions}-->
<!--        >-->
<!--            Показать всех-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if subscriptions.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Этот пользователь пока ни на кого не подписан.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="subs-list">-->
<!--            {#each subscriptions as sub}-->
<!--                <article class="sub-row">-->
<!--                    <Avatar-->
<!--                            size={40}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--                            .split(' ')-->
<!--                            .map((n) => n[0])-->
<!--                            .join('')-->
<!--                            .toUpperCase()}-->
<!--                    />-->
<!--                    <div class="sub-main">-->
<!--                        <div class="sub-name">{sub.fullName}</div>-->
<!--                        <div class="sub-meta">-->
<!--                            {sub.birthDate}-->
<!--                            {#if sub.wishlistTitle}-->
<!--                                · {sub.wishlistTitle}-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; АНКЕТА ПОЛЬЗОВАТЕЛЯ — КРАТКО &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Интересы и запреты</div>-->
<!--    </div>-->

<!--    {#if profile.questionnaire &&-->
<!--    ((profile.questionnaire.interests && profile.questionnaire.interests.length) ||-->
<!--        (profile.questionnaire.noGifts && profile.questionnaire.noGifts.length))}-->

<!--        {#if profile.questionnaire.interests?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Что дарить:</div>-->
<!--                <ul class="q-list">-->
<!--                    {#each profile.questionnaire.interests as item}-->
<!--                        <li>{item}</li>-->
<!--                    {/each}-->
<!--                </ul>-->
<!--            </div>-->
<!--        {/if}-->

<!--        {#if profile.questionnaire.noGifts?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Чего лучше не дарить:</div>-->
<!--                <ul class="q-list">-->
<!--                    {#each profile.questionnaire.noGifts as item}-->
<!--                        <li>{item}</li>-->
<!--                    {/each}-->
<!--                </ul>-->
<!--            </div>-->
<!--        {/if}-->

<!--        <Button kind="ghost" full on:click={openQuestionnaire}>-->
<!--            Посмотреть полную анкету-->
<!--        </Button>-->
<!--    {:else}-->
<!--        <p class="empty-note">-->
<!--            Пользователь ещё не заполнил анкету.-->
<!--        </p>-->
<!--    {/if}-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Назад-->
<!--    </Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-card {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->

<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .icon-16 {-->
<!--        width: 16px;-->
<!--        height: 16px;-->
<!--        margin-right: 4px;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--        gap: 8px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .section-title-with-icon {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 6px;-->
<!--        font-size: 14px;-->
<!--        font-weight: 600;-->
<!--        text-transform: uppercase;-->
<!--    }-->

<!--    .section-icon {-->
<!--        width: 18px;-->
<!--        height: 18px;-->
<!--    }-->

<!--    .link-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        padding: 0;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .wishlists-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .wishlist-icon {-->
<!--        width: 40px;-->
<!--        height: 40px;-->
<!--        border-radius: 14px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        overflow: hidden;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlist-icon img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .wishlist-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .wishlist-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .subs-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .sub-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .sub-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .sub-name {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .sub-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .q-block {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .q-label {-->
<!--        font-size: 13px;-->
<!--        font-weight: 600;-->
<!--        margin-bottom: 4px;-->
<!--    }-->

<!--    .q-list {-->
<!--        margin: 0;-->
<!--        padding-left: 18px;-->
<!--        font-size: 13px;-->
<!--        color: #374151;-->
<!--    }-->

<!--    .q-list li + li {-->
<!--        margin-top: 2px;-->
<!--    }-->
<!--</style>-->



<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->

<!--    // Профиль другого пользователя-->
<!--    // {-->
<!--    //   id, fullName, birthDate, avatarUrl,-->
<!--    //   publicWishlists?, subscriptions?,-->
<!--    //   isSubscribed?, questionnaire?-->
<!--    // }-->
<!--    export let profile;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    // локальное состояние подписки (потом заменишь на API)-->
<!--    let isSubscribed = !!profile?.isSubscribed;-->

<!--    // мок-данные (или реальные данные из API)-->
<!--    $: publicWishlists = profile?.publicWishlists ?? [];-->
<!--    $: subscriptions   = profile?.subscriptions ?? [];-->

<!--    // клик по "Подписаться / Вы подписаны"-->
<!--    const toggleSubscribe = () => {-->
<!--        isSubscribed = !isSubscribed;-->

<!--        // даём знать наверх (MainScreen / parent)-->
<!--        dispatch('toggle-subscribe', {-->
<!--            profileId: profile.id,-->
<!--            value: isSubscribed-->
<!--        });-->
<!--    };-->

<!--    // клик по "Посмотреть анкету" или "Посмотреть полную анкету"-->
<!--    const openQuestionnaire = () => {-->
<!--        dispatch('open-questionnaire', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->

<!--    // клик по "Показать все вишлисты"-->
<!--    const showAllWishlists = () => {-->
<!--        dispatch('show-all-wishlists', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->

<!--    // клик по "Показать всех" (подписки)-->
<!--    const showAllSubscriptions = () => {-->
<!--        dispatch('show-all-subscriptions', {-->
<!--            profileId: profile.id-->
<!--        });-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--</header>-->

<!--&lt;!&ndash; КАРТОЧКА ПРОФИЛЯ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card profile-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar-->
<!--                size={72}-->
<!--                src={profile.avatarUrl}-->
<!--                initials={profile.fullName-->
<!--                .split(' ')-->
<!--                .map((n) => n[0])-->
<!--                .join('')-->
<!--                .toUpperCase()}-->
<!--        />-->

<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{profile.fullName}</div>-->
<!--            <div class="profile-birth">{profile.birthDate}</div>-->

<!--            <div class="profile-actions">-->
<!--                <Button on:click={toggleSubscribe}>-->
<!--                    <img-->
<!--                            src={isSubscribed ? '/icons/bell-on.png' : '/icons/bell-off.png'}-->
<!--                            alt=""-->
<!--                            class="icon-16"-->
<!--                    />-->
<!--                    <span>{isSubscribed ? 'Вы подписаны' : 'Подписаться'}</span>-->
<!--                </Button>-->

<!--                <Button kind="ghost" on:click={openQuestionnaire}>-->
<!--                    Посмотреть анкету-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->

<!--&lt;!&ndash; ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ · {publicWishlists.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={showAllWishlists}-->
<!--        >-->
<!--            Показать все вишлисты-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if publicWishlists.length > 0}-->
<!--        &lt;!&ndash; Превью до 5 иконок вишлистов &ndash;&gt;-->
<!--        <div class="preview-row">-->
<!--            {#each publicWishlists.slice(0, 5) as wl}-->
<!--                <div class="preview-avatar">-->
<!--                    <img src={wl.iconUrl ?? '/icons/wishlist-card.png'} alt="" />-->
<!--                </div>-->
<!--            {/each}-->

<!--            {#if publicWishlists.length > 5}-->
<!--                <div class="preview-more">-->
<!--                    +{publicWishlists.length - 5}-->
<!--                </div>-->
<!--            {/if}-->
<!--        </div>-->
<!--    {/if}-->

<!--    {#if publicWishlists.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Здесь пока нет публичных вишлистов.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="wishlists-list">-->
<!--            {#each publicWishlists as wl}-->
<!--                <article class="wishlist-row">-->
<!--                    <div class="wishlist-icon">-->
<!--                        <img src={wl.iconUrl ?? '/icons/wishlist-card.png'} alt="" />-->
<!--                    </div>-->
<!--                    <div class="wishlist-main">-->
<!--                        <div class="wishlist-title">{wl.title}</div>-->
<!--                        <div class="wishlist-meta">-->
<!--                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}-->
<!--                            {#if typeof wl.wishesCount === 'number'}-->
<!--                                · {wl.wishesCount} жел.-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; ПОДПИСКИ &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="section-title-with-icon">-->
<!--            <img src="/icons/tab-list.png" alt="" class="section-icon" />-->
<!--            <span>ПОДПИСКИ · {subscriptions.length}</span>-->
<!--        </div>-->
<!--        <button-->
<!--                type="button"-->
<!--                class="link-btn"-->
<!--                on:click={showAllSubscriptions}-->
<!--        >-->
<!--            Показать всех-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if subscriptions.length > 0}-->
<!--        &lt;!&ndash; Превью до 5 аватаров подписок &ndash;&gt;-->
<!--        <div class="preview-row">-->
<!--            {#each subscriptions.slice(0, 5) as sub}-->
<!--                <div class="preview-avatar">-->
<!--                    <Avatar-->
<!--                            size={32}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--                            .split(' ')-->
<!--                            .map((n) => n[0])-->
<!--                            .join('')-->
<!--                            .toUpperCase()}-->
<!--                    />-->
<!--                </div>-->
<!--            {/each}-->

<!--            {#if subscriptions.length > 5}-->
<!--                <div class="preview-more">-->
<!--                    +{subscriptions.length - 5}-->
<!--                </div>-->
<!--            {/if}-->
<!--        </div>-->
<!--    {/if}-->

<!--    {#if subscriptions.length === 0}-->
<!--        <p class="empty-note">-->
<!--            Этот пользователь пока ни на кого не подписан.-->
<!--        </p>-->
<!--    {:else}-->
<!--        <div class="subs-list">-->
<!--            {#each subscriptions as sub}-->
<!--                <article class="sub-row">-->
<!--                    <Avatar-->
<!--                            size={40}-->
<!--                            src={sub.avatarUrl}-->
<!--                            initials={sub.fullName-->
<!--                            .split(' ')-->
<!--                            .map((n) => n[0])-->
<!--                            .join('')-->
<!--                            .toUpperCase()}-->
<!--                    />-->
<!--                    <div class="sub-main">-->
<!--                        <div class="sub-name">{sub.fullName}</div>-->
<!--                        <div class="sub-meta">-->
<!--                            {sub.birthDate}-->
<!--                            {#if sub.wishlistTitle}-->
<!--                                · {sub.wishlistTitle}-->
<!--                            {/if}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </article>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->
<!--</section>-->

<!--&lt;!&ndash; АНКЕТА ПОЛЬЗОВАТЕЛЯ — КРАТКО &ndash;&gt;-->
<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Интересы и запреты</div>-->
<!--    </div>-->

<!--    {#if profile.questionnaire &&-->
<!--    ((profile.questionnaire.interests && profile.questionnaire.interests.length) ||-->
<!--        (profile.questionnaire.noGifts && profile.questionnaire.noGifts.length))}-->

<!--        {#if profile.questionnaire.interests?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Что дарить?</div>-->
<!--                <div class="tag-row">-->
<!--                    {#each profile.questionnaire.interests as item}-->
<!--                        <span class="tag-chip">{item}</span>-->
<!--                    {/each}-->
<!--                </div>-->
<!--            </div>-->
<!--        {/if}-->

<!--        {#if profile.questionnaire.noGifts?.length}-->
<!--            <div class="q-block">-->
<!--                <div class="q-label">Что вам не дарить?</div>-->
<!--                <div class="tag-row">-->
<!--                    {#each profile.questionnaire.noGifts as item}-->
<!--                        <span class="tag-chip tag-chip&#45;&#45;danger">{item}</span>-->
<!--                    {/each}-->
<!--                </div>-->
<!--            </div>-->
<!--        {/if}-->

<!--        <Button kind="ghost" full on:click={openQuestionnaire}>-->
<!--            Посмотреть полную анкету-->
<!--        </Button>-->
<!--    {:else}-->
<!--        <p class="empty-note">-->
<!--            Пользователь ещё не заполнил анкету.-->
<!--        </p>-->
<!--    {/if}-->
<!--</section>-->

<!--<div style="padding:0 16px 12px;">-->
<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Назад-->
<!--    </Button>-->
<!--</div>-->

<!--<style>-->
<!--    .profile-card {-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-row {-->
<!--        display: flex;-->
<!--        gap: 12px;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .profile-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .profile-name {-->
<!--        font-size: 18px;-->
<!--        font-weight: 600;-->
<!--    }-->

<!--    .profile-birth {-->
<!--        font-size: 13px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .icon-16 {-->
<!--        width: 16px;-->
<!--        height: 16px;-->
<!--        margin-right: 4px;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        justify-content: space-between;-->
<!--        align-items: center;-->
<!--        gap: 8px;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .section-title-with-icon {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 6px;-->
<!--        font-size: 14px;-->
<!--        font-weight: 600;-->
<!--        text-transform: uppercase;-->
<!--    }-->

<!--    .section-icon {-->
<!--        width: 18px;-->
<!--        height: 18px;-->
<!--    }-->

<!--    .link-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        padding: 0;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    /* Préviews (jusqu’à 5 éléments) */-->
<!--    .preview-row {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 6px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .preview-avatar {-->
<!--        width: 32px;-->
<!--        height: 32px;-->
<!--        border-radius: 999px;-->
<!--        overflow: hidden;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .preview-avatar img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: cover;-->
<!--    }-->

<!--    .preview-more {-->
<!--        min-width: 32px;-->
<!--        height: 32px;-->
<!--        border-radius: 999px;-->
<!--        background: #e5edff;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        font-size: 12px;-->
<!--        color: #1d4ed8;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlists-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .wishlist-icon {-->
<!--        width: 40px;-->
<!--        height: 40px;-->
<!--        border-radius: 14px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        overflow: hidden;-->
<!--        flex-shrink: 0;-->
<!--    }-->

<!--    .wishlist-icon img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .wishlist-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .wishlist-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .subs-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .sub-row {-->
<!--        display: flex;-->
<!--        gap: 8px;-->
<!--        align-items: center;-->
<!--        padding: 6px 8px;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--    }-->

<!--    .sub-main {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .sub-name {-->
<!--        font-size: 14px;-->
<!--        font-weight: 500;-->
<!--    }-->

<!--    .sub-meta {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->

<!--    .q-block {-->
<!--        margin-bottom: 12px;-->
<!--    }-->

<!--    .q-label {-->
<!--        font-size: 13px;-->
<!--        font-weight: 600;-->
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .tag-row {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 6px;-->
<!--    }-->

<!--    .tag-chip {-->
<!--        padding: 6px 10px;-->
<!--        border-radius: 999px;-->
<!--        background: #f3f4f6;-->
<!--        font-size: 13px;-->
<!--        color: #374151;-->
<!--    }-->

<!--    .tag-chip&#45;&#45;danger {-->
<!--        background: #fee2e2;-->
<!--    }-->
<!--</style>-->






<script>
    import { createEventDispatcher } from 'svelte';
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import Button from '$lib/components/ui/Button.svelte';

    // Профиль другого пользователя
    // {
    //   id, fullName, birthDate, avatarUrl,
    //   publicWishlists?, subscriptions?,
    //   isSubscribed?, questionnaire?
    // }
    export let profile;

    const dispatch = createEventDispatcher();
    const goBack = () => dispatch('back');

    let isSubscribed = !!profile?.isSubscribed;

    $: publicWishlists = profile?.publicWishlists ?? [];
    $: subscriptions   = profile?.subscriptions ?? [];

    // только те вишлисты, у которых есть иконка
    $: publicWishlistsWithIcon = publicWishlists.filter((wl) => !!wl.iconUrl);

    const toggleSubscribe = () => {
        isSubscribed = !isSubscribed;
        dispatch('toggle-subscribe', {
            profileId: profile.id,
            value: isSubscribed
        });
    };

    const showAllWishlists = () => {
        dispatch('show-all-wishlists', { profileId: profile.id });
    };

    const showAllSubscriptions = () => {
        dispatch('show-all-subscriptions', { profileId: profile.id });
    };
</script>

<header class="app-header">
    <div class="h1">Профиль</div>
</header>

<section class="section-card profile-card">
    <div class="profile-row">
        <Avatar
                size={72}
                src={profile.avatarUrl}
                initials={profile.fullName
                .split(' ')
                .map((n) => n[0])
                .join('')
                .toUpperCase()}
        />

        <div class="profile-main">
            <div class="profile-name">{profile.fullName}</div>
            <div class="profile-birth">{profile.birthDate}</div>

            <div class="profile-actions">
                <Button kind="ghost" on:click={toggleSubscribe}>
                    <img
                            src={isSubscribed ? '/icons/bell-on.png' : '/icons/bell-off.png'}
                            alt=""
                            class="icon-16"
                    />
                    <span>{isSubscribed ? 'Вы подписаны' : 'Подписаться'}</span>
                </Button>
                <!-- plus de bouton "Посмотреть анкету" ici -->
            </div>
        </div>
    </div>
</section>

<!-- ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ -->
<section class="section-card">
    <div class="section-header">
        <div class="section-title-with-icon">
            <img src="/icons/gift-check.png" alt="" class="section-icon" />
            <div class="section-title-main">
                <span>ВИШЛИСТЫ ПОЛЬЗОВАТЕЛЯ · {publicWishlists.length}</span>

                {#if publicWishlistsWithIcon.length}
<!--                    <div class="mini-icons">-->
<!--                        {#each publicWishlistsWithIcon.slice(0, 5) as wl}-->
<!--                            <div class="mini-icon">-->
<!--                                <img src={wl.iconUrl} alt={wl.title} />-->
<!--                            </div>-->
<!--                        {/each}-->
<!--                    </div>-->
                {/if}
            </div>
        </div>
        <button
                type="button"
                class="link-btn"
                on:click={showAllWishlists}
        >
            Показать все вишлисты
        </button>
    </div>

    {#if publicWishlists.length === 0}
        <p class="empty-note">
            Здесь пока нет публичных вишлистов.
        </p>
    {:else}
        <div class="wishlists-list">
            {#each publicWishlists as wl}
                <article class="wishlist-row">
                    <div class="wishlist-icon">
                        <img src={wl.iconUrl ?? '/icons/gift-check.png'} alt={wl.title} />
                    </div>
                    <div class="wishlist-main">
                        <div class="wishlist-title">{wl.title}</div>
                        <div class="wishlist-meta">
                            {wl.visibility === 'public' ? 'Виден всем' : 'Доступ ограничен'}
                            {#if typeof wl.wishesCount === 'number'}
                                · {wl.wishesCount} жел.
                            {/if}
                        </div>
                    </div>
                </article>
            {/each}
        </div>
    {/if}
</section>

<!-- ПОДПИСКИ -->
<section class="section-card">
    <div class="section-header">
        <div class="section-title-with-icon">
            <img src="/icons/follow.png" alt="" class="section-icon" />
            <div class="section-title-main">
                <span>ПОДПИСКИ · {subscriptions.length}</span>

                {#if subscriptions.length}
                    <div class="mini-icons">
                        {#each subscriptions.slice(0, 5) as sub}
<!--                            <div class="mini-icon">-->
<!--                                <Avatar-->
<!--                                        size={24}-->
<!--                                        src={sub.avatarUrl}-->
<!--                                        initials={sub.fullName-->
<!--                                        .split(' ')-->
<!--                                        .map((n) => n[0])-->
<!--                                        .join('')-->
<!--                                        .toUpperCase()}-->
<!--                                />-->
<!--                            </div>-->
                        {/each}
                    </div>
                {/if}
            </div>
        </div>
        <button
                type="button"
                class="link-btn"
                on:click={showAllSubscriptions}
        >
            Показать всех
        </button>
    </div>

    {#if subscriptions.length === 0}
        <p class="empty-note">
            Этот пользователь пока ни на кого не подписан.
        </p>
    {:else}
        <div class="subs-list">
            {#each subscriptions as sub}
                <article class="sub-row">
                    <Avatar
                            size={40}
                            src={sub.avatarUrl}
                            initials={sub.fullName
                            .split(' ')
                            .map((n) => n[0])
                            .join('')
                            .toUpperCase()}
                    />
                    <div class="sub-main">
                        <div class="sub-name">{sub.fullName}</div>
                        <div class="sub-meta">
                            {sub.birthDate}
                            {#if sub.wishlistTitle}
                                · {sub.wishlistTitle}
                            {/if}
                        </div>
                    </div>
                </article>
            {/each}
        </div>
    {/if}
</section>

<!-- ИНТЕРЕСЫ И ЗАПРЕТЫ — ТОЛЬКО КРАТКО, БЕЗ КНОПКИ -->
<section class="section-card">
    <div class="section-header">
        <div class="h2">Интересы и запреты</div>
    </div>

    {#if profile.questionnaire &&
    ((profile.questionnaire.interests && profile.questionnaire.interests.length) ||
        (profile.questionnaire.noGifts && profile.questionnaire.noGifts.length))}

        {#if profile.questionnaire.interests?.length}
            <div class="q-block">
                <div class="q-label">Что дарить?</div>
                <div class="q-pills">
                    {#each profile.questionnaire.interests as item}
                        <span class="q-pill q-pill--ok">{item}</span>
                    {/each}
                </div>
            </div>
        {/if}

        {#if profile.questionnaire.noGifts?.length}
            <div class="q-block">
                <div class="q-label">Что вам не дарить?</div>
                <div class="q-pills">
                    {#each profile.questionnaire.noGifts as item}
                        <span class="q-pill q-pill--no">{item}</span>
                    {/each}
                </div>
            </div>
        {/if}

        <!-- plus de bouton "Посмотреть полную анкету" -->
    {:else}
        <p class="empty-note">
            Пользователь ещё не заполнил анкету.
        </p>
    {/if}
</section>

<div style="padding:0 16px 12px;">
    <Button kind="ghost" full on:click={goBack}>
        Назад
    </Button>
</div>

<style>
    .profile-card {
        margin-bottom: 8px;
    }

    .profile-row {
        display: flex;
        gap: 12px;
        align-items: center;
    }

    .profile-main {
        flex: 1;
    }

    .profile-name {
        font-size: 18px;
        font-weight: 600;
    }

    .profile-birth {
        font-size: 13px;
        color: #6b7280;
        margin-top: 2px;
        margin-bottom: 8px;
    }

    .profile-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;

    }

    .icon-16 {
        width: 16px;
        height: 16px;
        margin-right: 4px;
    }

    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        margin-bottom: 6px;
    }

    .section-title-with-icon {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
    }

    .section-title-main {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .section-icon {
        width: 18px;
        height: 18px;
    }

    .link-btn {
        border: none;
        background: transparent;
        color: #1d4ed8;
        font-size: 13px;
        padding: 0;
        cursor: pointer;
    }

    .mini-icons {
        display: flex;
        align-items: center;
    }

    /*.mini-icon {*/
    /*    width: 24px;*/
    /*    height: 24px;*/
    /*    border-radius: 999px;*/
    /*    overflow: hidden;*/
    /*    border: 2px solid #fff;*/
    /*    margin-left: -6px;*/
    /*    background: #e5e7eb;*/
    /*}*/

    /*.mini-icon:first-child {*/
    /*    margin-left: 0;*/
    /*}*/

    .mini-icon img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .wishlists-list {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .wishlist-row {
        display: flex;
        gap: 8px;
        align-items: center;
        padding: 6px 8px;
        border-radius: 12px;
        background: #f9fafb;
    }

    .wishlist-icon {
        width: 40px;
        height: 40px;
        border-radius: 14px;
        background: #f3f4f6;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        flex-shrink: 0;
    }

    .wishlist-icon img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    .wishlist-main {
        flex: 1;
    }

    .wishlist-title {
        font-size: 14px;
        font-weight: 500;
    }

    .wishlist-meta {
        font-size: 12px;
        color: #6b7280;
    }

    .subs-list {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .sub-row {
        display: flex;
        gap: 8px;
        align-items: center;
        padding: 6px 8px;
        border-radius: 12px;
        background: #f9fafb;
    }

    .sub-main {
        flex: 1;
    }

    .sub-name {
        font-size: 14px;
        font-weight: 500;
    }

    .sub-meta {
        font-size: 12px;
        color: #6b7280;
    }

    .q-block {
        margin-bottom: 8px;
    }

    .q-label {
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 4px;
    }

    .q-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }

    .q-pill {
        font-size: 13px;
        padding: 4px 8px;
        border-radius: 999px;
        background: #f3f4f6;
    }

    .q-pill--ok {
        background: #e0f2fe;
        color: #0369a1;
    }

    .q-pill--no {
        background: #fee2e2;
        color: #b91c1c;
    }

    .q-list li + li {
        margin-top: 2px;
    }
</style>
