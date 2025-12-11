<!--&lt;!&ndash;<script>&ndash;&gt;-->
<!--&lt;!&ndash;    import { createEventDispatcher } from 'svelte';&ndash;&gt;-->
<!--&lt;!&ndash;    import Avatar from '$lib/components/ui/Avatar.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;    import Button from '$lib/components/ui/Button.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;    import { wishlistsStore, wishesStore } from '$lib/stores/data.js';&ndash;&gt;-->

<!--&lt;!&ndash;    export let user;&ndash;&gt;-->

<!--&lt;!&ndash;    const dispatch = createEventDispatcher();&ndash;&gt;-->

<!--&lt;!&ndash;    const openSettings = () => dispatch('openSettings');&ndash;&gt;-->
<!--&lt;!&ndash;    const openQuestionnaire = () => dispatch('openQuestionnaire');&ndash;&gt;-->
<!--&lt;!&ndash;    const openWishes = () => dispatch('openWishes');&ndash;&gt;-->
<!--&lt;!&ndash;    const openWishlists = () => dispatch('openWishlists');&ndash;&gt;-->
<!--&lt;!&ndash;    const openSubscriptions = () => dispatch('openSubscriptions');&ndash;&gt;-->
<!--&lt;!&ndash;    const openSubscribers = () => dispatch('openSubscribers');&ndash;&gt;-->
<!--&lt;!&ndash;    const openShareProfile = () => dispatch('openShareProfile');&ndash;&gt;-->

<!--&lt;!&ndash;    const getInitials = (name) => {&ndash;&gt;-->
<!--&lt;!&ndash;        if (!name) return '??';&ndash;&gt;-->
<!--&lt;!&ndash;        const parts = name.trim().split(' ');&ndash;&gt;-->
<!--&lt;!&ndash;        return parts.slice(0, 2).map((p) => p[0]).join('').toUpperCase();&ndash;&gt;-->
<!--&lt;!&ndash;    };&ndash;&gt;-->

<!--&lt;!&ndash;    // считаем кол-во из стор&ndash;&gt;-->
<!--&lt;!&ndash;    $: n_wishes = $wishesStore.length;&ndash;&gt;-->
<!--&lt;!&ndash;    $: n_wishlist = $wishlistsStore.length;&ndash;&gt;-->
<!--&lt;!&ndash;    const n_sub = 3;&ndash;&gt;-->
<!--&lt;!&ndash;    const n_subi = 5;&ndash;&gt;-->
<!--&lt;!&ndash;</script>&ndash;&gt;-->



<!--&lt;!&ndash;<header class="app-header">&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="h1">Профиль</div>&ndash;&gt;-->
<!--&lt;!&ndash;  <button class="icon-btn" type="button" on:click={openSettings}><img class="tab-dot" src="/icons/tab-settings.png" alt="" /></button>&ndash;&gt;-->
<!--&lt;!&ndash;    <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;</header>&ndash;&gt;-->

<!--&lt;!&ndash;<section class="section-card">&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="profile-row">&ndash;&gt;-->
<!--&lt;!&ndash;    <Avatar size={72} src={user.avatarUrl} initials={getInitials(user.fullName)} />&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="profile-main">&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="profile-name">{user.fullName}</div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="profile-birth">{user.birthDate}</div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="profile-actions">&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <Button kind="ghost" on:click={() => alert('share profile UI here')}>Поделиться профилем</Button>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          <Button kind="ghost" on:click={openShareProfile}>Поделиться профилем</Button>&ndash;&gt;-->

<!--&lt;!&ndash;          <Button kind="ghost" on:click={openQuestionnaire}>Посмотреть анкету</Button>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--&lt;!&ndash;  <button class="ghost-link" type="button" on:click={openWishes}>&ndash;&gt;-->
<!--&lt;!&ndash;    Все ваши желания · {n_wishes}&ndash;&gt;-->
<!--&lt;!&ndash;  </button>&ndash;&gt;-->
<!--&lt;!&ndash;</section>&ndash;&gt;-->

<!--&lt;!&ndash;&lt;!&ndash;<section class="section-card">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;  <div class="section-header">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;    <div class="h2">Ваши вишлисты · {n_wishlist}</div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;    <button class="tiny-link" type="button" on:click={openWishlists}>Показать все</button>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;  </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;  <div class="empty-note">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;    Здесь появятся ваши вишлисты. Создайте первый, чтобы друзья знали, что вам подарить.&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;  </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;  <Button full kind="ghost" on:click={openWishlists}>+ Создать вишлист</Button>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;</section>&ndash;&gt;&ndash;&gt;-->

<!--&lt;!&ndash;<section class="section-card">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="section-header">&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="h2">Ваши вишлисты · {n_wishlist}</div>&ndash;&gt;-->
<!--&lt;!&ndash;        <button class="tiny-link" type="button" on:click={openWishlists}>Показать все</button>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->

<!--&lt;!&ndash;    {#if $wishlistsStore.length === 0}&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="empty-note">&ndash;&gt;-->
<!--&lt;!&ndash;            Здесь появятся ваши вишлисты. Создайте первый, чтобы друзья знали, что вам подарить.&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;    {:else}&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="wishlist-list">&ndash;&gt;-->
<!--&lt;!&ndash;            {#each $wishlistsStore.slice(0, 3) as wl}&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="wishlist-row" on:click={openWishlists}>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div class="wishlist-cover-small">&ndash;&gt;-->
<!--&lt;!&ndash;                        {#if wl.coverUrl}&ndash;&gt;-->
<!--&lt;!&ndash;                            <img src={wl.coverUrl} alt={wl.title} />&ndash;&gt;-->
<!--&lt;!&ndash;                        {:else}&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;                            <span>🎁</span>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;                        {/if}&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div class="wishlist-main-small">&ndash;&gt;-->
<!--&lt;!&ndash;                        <div class="wishlist-title-small" title={wl.title}>{wl.title}</div>&ndash;&gt;-->
<!--&lt;!&ndash;                        <div class="wishlist-meta-small">&ndash;&gt;-->
<!--&lt;!&ndash;              <span>&ndash;&gt;-->
<!--&lt;!&ndash;                {wl.privacy === 'public'&ndash;&gt;-->
<!--&lt;!&ndash;                    ? 'Виден всем'&ndash;&gt;-->
<!--&lt;!&ndash;                    : wl.privacy === 'restricted'&ndash;&gt;-->
<!--&lt;!&ndash;                        ? 'Для определённых пользователей'&ndash;&gt;-->
<!--&lt;!&ndash;                        : 'Виден только вам'}&ndash;&gt;-->
<!--&lt;!&ndash;              </span>&ndash;&gt;-->
<!--&lt;!&ndash;                            <span> · {wl.count} жел.</span>&ndash;&gt;-->
<!--&lt;!&ndash;                        </div>&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->
<!--&lt;!&ndash;            {/each}&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;    {/if}&ndash;&gt;-->

<!--&lt;!&ndash;    <Button full kind="ghost" on:click={openWishlists}>+ Создать вишлист</Button>&ndash;&gt;-->
<!--&lt;!&ndash;</section>&ndash;&gt;-->



<!--&lt;!&ndash;<section class="section-card">&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="section-header">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="h2">Подписки · {n_sub}</div>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class="tiny-link" type="button" on:click={openSubscriptions}>Показать всех</button>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="empty-note">Вы ещё ни на кого не подписаны.</div>&ndash;&gt;-->
<!--&lt;!&ndash;</section>&ndash;&gt;-->

<!--&lt;!&ndash;<section class="section-card">&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="section-header">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="h2">Подписчики · {n_subi}</div>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class="tiny-link" type="button" on:click={openSubscribers}>Показать всех</button>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="empty-note">У вас пока нет подписчиков.</div>&ndash;&gt;-->
<!--&lt;!&ndash;</section>&ndash;&gt;-->

<!--&lt;!&ndash;<style>&ndash;&gt;-->
<!--&lt;!&ndash;  /*.icon-btn {*/&ndash;&gt;-->
<!--&lt;!&ndash;  /*  border: none;*/&ndash;&gt;-->
<!--&lt;!&ndash;  /*  background: transparent;*/&ndash;&gt;-->
<!--&lt;!&ndash;  /*  font-size: 12px;*/&ndash;&gt;-->
<!--&lt;!&ndash;  /*  cursor: pointer;*/&ndash;&gt;-->
<!--&lt;!&ndash;  /*}*/&ndash;&gt;-->

<!--&lt;!&ndash;  .wishlist-cover-small{&ndash;&gt;-->
<!--&lt;!&ndash;      width: 52px;&ndash;&gt;-->
<!--&lt;!&ndash;      height: 52px;&ndash;&gt;-->
<!--&lt;!&ndash;      border-radius: 16px;&ndash;&gt;-->
<!--&lt;!&ndash;      background: #f3f4f6;&ndash;&gt;-->
<!--&lt;!&ndash;      display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;      align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;      justify-content: center;&ndash;&gt;-->
<!--&lt;!&ndash;      flex-shrink: 0;&ndash;&gt;-->
<!--&lt;!&ndash;      overflow: hidden;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .icon-btn {&ndash;&gt;-->
<!--&lt;!&ndash;      border: none;&ndash;&gt;-->
<!--&lt;!&ndash;      background: transparent;&ndash;&gt;-->
<!--&lt;!&ndash;      cursor: pointer;&ndash;&gt;-->
<!--&lt;!&ndash;      padding: 4px;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .tab-dot {&ndash;&gt;-->
<!--&lt;!&ndash;      width: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;      height: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;      /*font-size: 20px; !* plus petit *!*/&ndash;&gt;-->
<!--&lt;!&ndash;      /*!*border-radius: 999px;*!*/&ndash;&gt;-->
<!--&lt;!&ndash;      margin-right: 0px;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->



<!--&lt;!&ndash;  .profile-row {&ndash;&gt;-->
<!--&lt;!&ndash;    display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;    gap: 12px;&ndash;&gt;-->
<!--&lt;!&ndash;    align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .profile-main {&ndash;&gt;-->
<!--&lt;!&ndash;    flex: 1;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .profile-name {&ndash;&gt;-->
<!--&lt;!&ndash;    font-size: 18px;&ndash;&gt;-->
<!--&lt;!&ndash;    font-weight: 600;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .profile-birth {&ndash;&gt;-->
<!--&lt;!&ndash;    font-size: 13px;&ndash;&gt;-->
<!--&lt;!&ndash;    color: #6b7280;&ndash;&gt;-->
<!--&lt;!&ndash;    margin-top: 2px;&ndash;&gt;-->
<!--&lt;!&ndash;    margin-bottom: 6px;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .profile-actions {&ndash;&gt;-->
<!--&lt;!&ndash;    display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;    flex-wrap: wrap;&ndash;&gt;-->
<!--&lt;!&ndash;    gap: 4px;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .ghost-link {&ndash;&gt;-->
<!--&lt;!&ndash;    margin-top: 10px;&ndash;&gt;-->
<!--&lt;!&ndash;    padding: 8px 0 0;&ndash;&gt;-->
<!--&lt;!&ndash;    border: none;&ndash;&gt;-->
<!--&lt;!&ndash;    background: transparent;&ndash;&gt;-->
<!--&lt;!&ndash;    color: #2563eb;&ndash;&gt;-->
<!--&lt;!&ndash;    font-size: 14px;&ndash;&gt;-->
<!--&lt;!&ndash;    cursor: pointer;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .section-header {&ndash;&gt;-->
<!--&lt;!&ndash;    display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;    align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;    justify-content: space-between;&ndash;&gt;-->
<!--&lt;!&ndash;    margin-bottom: 8px;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->

<!--&lt;!&ndash;  .tiny-link {&ndash;&gt;-->
<!--&lt;!&ndash;    border: none;&ndash;&gt;-->
<!--&lt;!&ndash;    background: transparent;&ndash;&gt;-->
<!--&lt;!&ndash;    color: #2563eb;&ndash;&gt;-->
<!--&lt;!&ndash;    font-size: 13px;&ndash;&gt;-->
<!--&lt;!&ndash;    cursor: pointer;&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->



<!--&lt;!&ndash;</style>&ndash;&gt;-->


<!--<script>-->
<!--    import { createEventDispatcher } from 'svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import { wishlistsStore, wishesStore } from '$lib/stores/data.js';-->


<!--    export let user;-->

<!--    const dispatch = createEventDispatcher();-->

<!--    const openSettings = () => dispatch('openSettings');-->
<!--    const openQuestionnaire = () => dispatch('openQuestionnaire');-->
<!--    const openWishes = () => dispatch('openWishes');-->
<!--    const openWishlists = () => dispatch('openWishlists');-->
<!--    const openSubscriptions = () => dispatch('openSubscriptions');-->
<!--    const openSubscribers = () => dispatch('openSubscribers');-->
<!--    const openShareProfile = () => dispatch('openShareProfile');-->



<!--    const getInitials = (name) => {-->
<!--        if (!name) return '??';-->
<!--        const parts = name.trim().split(' ');-->
<!--        return parts.slice(0, 2).map((p) => p[0]).join('').toUpperCase();-->
<!--    };-->

<!--    $: n_wishes = $wishesStore.length;-->
<!--    $: n_wishlist = $wishlistsStore.length;-->
<!--    const n_sub = 3;-->
<!--    const n_subi = 5;-->

<!--    const getWishlistCount = (wishlistId) =>-->
<!--        $wishesStore.filter((w) => (w.wishlistIds || []).includes(wishlistId)).length;-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Профиль</div>-->
<!--    <button class="icon-btn" type="button" on:click={openSettings}>-->
<!--        <img src="/icons/tab-settings.png" alt="" />-->
<!--    </button>-->
<!--</header>-->

<!--<section class="section-card">-->
<!--    <div class="profile-row">-->
<!--        <Avatar size={72} src={user.avatarUrl} initials={getInitials(user.fullName)} />-->
<!--        <div class="profile-main">-->
<!--            <div class="profile-name">{user.fullName}</div>-->
<!--            <div class="profile-birth">{user.birthDate}</div>-->
<!--            <div class="profile-actions">-->
<!--                <Button kind="ghost" on:click={openShareProfile}>-->
<!--                    <img src="/icons/share.png" alt="" class="btn-icon" />-->
<!--                    <span>Поделиться профилем</span>-->
<!--                </Button>-->

<!--                <Button kind="ghost" on:click={openQuestionnaire}>-->
<!--                    <img src="/icons/edit.png" alt="" class="btn-icon" />-->
<!--                    <span>Посмотреть анкету</span>-->
<!--                </Button>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--    <button class="ghost-link" type="button" on:click={openWishes}>-->
<!--        Все ваши желания · {n_wishes}-->
<!--    </button>-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Ваши вишлисты · {n_wishlist}</div>-->
<!--        <button class="tiny-link" type="button" on:click={openWishlists}>-->
<!--            Показать все-->
<!--        </button>-->
<!--    </div>-->

<!--    {#if $wishlistsStore.length === 0}-->
<!--        <div class="empty-note">-->
<!--            Здесь появятся ваши вишлисты. Создайте первый, чтобы друзья знали, что вам подарить.-->
<!--        </div>-->
<!--    {:else}-->
<!--        <div class="wishlist-list">-->
<!--            {#each $wishlistsStore.slice(0, 3) as wl}-->
<!--                <button class="wishlist-row" type="button" on:click={openWishlists}>-->
<!--                    <div class="wishlist-cover-small">-->
<!--                        {#if wl.coverUrl}-->
<!--                            <img src={wl.coverUrl} alt={wl.title} />-->
<!--                        {:else}-->
<!--                            <img src="/icons/gift2.svg" alt="Подарок" />-->
<!--                        {/if}-->



<!--                    </div>-->
<!--                    <div class="wishlist-main-small">-->
<!--                        <div class="wishlist-title-small" title={wl.title}>{wl.title}</div>-->
<!--                        <div class="wishlist-meta-small">-->
<!--                            <span class="privacy-chip">-->
<!--                                <img-->
<!--                                        class="privacy-icon"-->
<!--                                        src={wl.privacy === 'public'-->
<!--                                        ? '/icons/view.png'-->
<!--                                        : '/icons/unview.png'}-->
<!--                                        alt=""-->
<!--                                />-->
<!--                                <span>-->
<!--                                    {wl.privacy === 'public'-->
<!--                                        ? 'Виден всем'-->
<!--                                        : wl.privacy === 'restricted'-->
<!--                                            ? 'Для определённых пользователей'-->
<!--                                            : 'Виден только вам'}-->
<!--                                </span>-->
<!--                            </span>-->
<!--                            <span> · {getWishlistCount(wl.id)} жел.</span>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </button>-->
<!--            {/each}-->
<!--        </div>-->
<!--    {/if}-->

<!--    <Button full kind="ghost" on:click={openWishlists}>+ Создать вишлист</Button>-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Подписки · {n_sub}</div>-->
<!--        <button class="tiny-link" type="button" on:click={openSubscriptions}>-->
<!--            Показать всех-->
<!--        </button>-->
<!--    </div>-->
<!--    <div class="empty-note">Вы ещё ни на кого не подписаны.</div>-->
<!--</section>-->

<!--<section class="section-card">-->
<!--    <div class="section-header">-->
<!--        <div class="h2">Подписчики · {n_subi}</div>-->
<!--        <button class="tiny-link" type="button" on:click={openSubscribers}>-->
<!--            Показать всех-->
<!--        </button>-->
<!--    </div>-->
<!--    <div class="empty-note">У вас пока нет подписчиков.</div>-->
<!--</section>-->

<!--<style>-->
<!--    .icon-btn {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        cursor: pointer;-->
<!--        padding: 4px;-->
<!--        margin-right: 4px;-->
<!--    }-->

<!--    .icon-btn img {-->
<!--        width: 20px;-->
<!--        height: 20px;-->
<!--        display: block;-->
<!--    }-->

<!--    .btn-icon {-->
<!--        width: 16px;-->
<!--        height: 16px;-->
<!--        margin-right: 4px;-->
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
<!--        margin-bottom: 6px;-->
<!--    }-->

<!--    .profile-actions {-->
<!--        display: flex;-->
<!--        flex-wrap: wrap;-->
<!--        gap: 4px;-->
<!--    }-->

<!--    .ghost-link {-->
<!--        margin-top: 10px;-->
<!--        padding: 8px 0 0;-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 14px;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .section-header {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: space-between;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .tiny-link {-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        color: #2563eb;-->
<!--        font-size: 13px;-->
<!--        cursor: pointer;-->
<!--    }-->

<!--    .wishlist-list {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 6px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->

<!--    .wishlist-row {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 10px;-->
<!--        padding: 8px;-->
<!--        width: 100%;-->
<!--        border-radius: 12px;-->
<!--        background: #f9fafb;-->
<!--        border: 1px solid #e5e7eb;-->
<!--        cursor: pointer;-->
<!--        text-align: left;-->
<!--    }-->

<!--    .wishlist-cover-small{-->
<!--        width: 52px;-->
<!--        height: 52px;-->
<!--        border-radius: 16px;-->
<!--        background: #f3f4f6;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        justify-content: center;-->
<!--        flex-shrink: 0;-->
<!--        overflow: hidden;-->
<!--    }-->

<!--    .wishlist-cover-small img {-->
<!--        width: 100%;-->
<!--        height: 100%;-->
<!--        object-fit: cover;-->
<!--    }-->

<!--    .wishlist-main-small {-->
<!--        flex: 1;-->
<!--    }-->

<!--    .wishlist-title-small {-->
<!--        font-size: 15px;-->
<!--        font-weight: 500;-->
<!--        white-space: nowrap;-->
<!--        overflow: hidden;-->
<!--        text-overflow: ellipsis;-->
<!--    }-->

<!--    .wishlist-meta-small {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--        margin-top: 2px;-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 4px;-->
<!--    }-->

<!--    .privacy-chip {-->
<!--        display: inline-flex;-->
<!--        align-items: center;-->
<!--        gap: 4px;-->
<!--    }-->

<!--    .privacy-icon {-->
<!--        width: 14px;-->
<!--        height: 14px;-->
<!--        display: block;-->
<!--    }-->
<!--</style>-->


<script>
    import { createEventDispatcher } from 'svelte';
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import Button from '$lib/components/ui/Button.svelte';
    import {otherProfilesMock} from "$lib/stores/data.js";
    import {
        wishlistsStore,
        wishesStore,
        subscriptionsStore,
        subscribersStore
    } from '$lib/stores/data.js';



    export let user;

    const dispatch = createEventDispatcher();

    const openSettings = () => dispatch('openSettings');
    const openQuestionnaire = () => dispatch('openQuestionnaire');
    const openWishes = () => dispatch('openWishes');
    const openWishlists = () => dispatch('openWishlists');
    const openSubscriptions = () => dispatch('openSubscriptions');
    const openSubscribers = () => dispatch('openSubscribers');
    const openShareProfile = () => dispatch('openShareProfile');

    const ICON_GIFT = '/icons/maingift.svg';

    const getInitials = (name) => {
        if (!name) return '??';
        const parts = name.trim().split(' ');
        return parts.slice(0, 2).map((p) => p[0]).join('').toUpperCase();
    };

    $: n_wishes = $wishesStore.length;
    $: n_wishlist = $wishlistsStore.length;
    $: n_sub = $subscriptionsStore.length;
    $: n_subi = $subscribersStore.length;

    const getWishlistCount = (wishlistId) =>
        $wishesStore.filter((w) => (w.wishlistIds || []).includes(wishlistId)).length;
</script>




<div class="screen">
<header class="app-header">
    <div class="h1">Профиль</div>
    <button class="icon-btn" type="button" on:click={openSettings}>
        <img src="/icons/tab-settings.png" alt="" />
    </button>
</header>


<section class="section-card">
    <div class="profile-row">
        <Avatar size={72} src={user.avatarUrl} initials={getInitials(user.fullName)} />
        <div class="profile-main">
            <div class="profile-name">{user.fullName}</div>
            <div class="profile-birth">{user.birthDate}</div>
            <div class="profile-actions">
                <Button kind="ghost" on:click={openShareProfile}>
                    <img src="/icons/share.png" alt="" class="btn-icon" />
                    <span>Поделиться профилем</span>
                </Button>

                <Button kind="ghost" on:click={openQuestionnaire}>
                    <img src="/icons/edit.png" alt="" class="btn-icon" />
                    <span>Посмотреть анкету</span>
                </Button>
            </div>
        </div>
    </div>
    <button class="ghost-link" type="button" on:click={openWishes}>
        Все ваши желания · {n_wishes}
    </button>
</section>

<!-- Вишлисты -->
<section class="section-card">
    <div class="section-header">
        <div class="h2">Ваши вишлисты · {n_wishlist}</div>
        <button class="tiny-link" type="button" on:click={openWishlists}>
            Показать все
        </button>
    </div>

    {#if $wishlistsStore.length === 0}
        <div class="empty-note">
            Здесь появятся ваши вишлисты. Создайте первый, чтобы друзья знали, что вам подарить.
        </div>
    {:else}
        <div class="wishlist-list">
            {#each $wishlistsStore.slice(0, 5) as wl}
                <button class="wishlist-row" type="button" on:click={openWishlists}>
                    <div class="wishlist-cover-small">
                        {#if wl.coverUrl}
                            <img src={wl.coverUrl} alt={wl.title} />
                        {:else}
                            <img src={ICON_GIFT} alt="Подарок"/>
                        {/if}
                    </div>

                    <div class="wishlist-main-small">
                        <div class="wishlist-title-small" title={wl.title}>{wl.title}</div>
                        <div class="wishlist-meta-small">
              <span class="privacy-chip">
                <img
                        class="privacy-icon"
                        src={wl.privacy === 'public'
                    ? '/icons/view.png'
                    : '/icons/unview.png'}
                        alt=""
                />
                <span>
                  {wl.privacy === 'public'
                      ? 'Виден всем'
                      : wl.privacy === 'restricted'
                          ? 'Для определённых пользователей'
                          : 'Виден только вам'}
                </span>
              </span>
                            <span> · {getWishlistCount(wl.id)} жел.</span>
                        </div>
                    </div>
                </button>
            {/each}
        </div>
    {/if}

    <Button full kind="ghost" on:click={openWishlists}>+ Создать вишлист</Button>
</section>

<!-- Подписки -->
{#if user.showSubscriptions}
<section class="section-card">
    <div class="section-header">
        <div class="h2">Подписки · {n_sub}</div>
        <button class="tiny-link" type="button" on:click={openSubscriptions}>
            Показать всех
        </button>
    </div>

    {#if $subscriptionsStore.length === 0}
        <div class="empty-note">Вы ещё ни на кого не подписаны.</div>
    {:else}
        <div class="subs-list">
            {#each $subscriptionsStore.slice(0, 5) as sub}
                <button
                        type="button"
                        class="subs-row"
                        on:click={openSubscriptions}
                >
                    <Avatar
                            size={40}
                            src={sub.avatarUrl}
                            initials={getInitials(sub.fullName)}
                    />
                    <div class="subs-main">
                        <div class="subs-name" title={sub.fullName}>{sub.fullName}</div>
                        <div class="subs-meta">
                            <span>{sub.birthDate}</span>
                            {#if sub.wishlistTitle}
                                <span> · {sub.wishlistTitle}</span>
                            {/if}
                        </div>
                    </div>
                </button>
            {/each}
        </div>
    {/if}
</section>
{/if}
<!-- Подписчики -->

<section class="section-card">
    <div class="section-header">
        <div class="h2">Подписчики · {n_subi}</div>
        <button class="tiny-link" type="button" on:click={openSubscribers}>
            Показать всех
        </button>
    </div>

    {#if $subscribersStore.length === 0}
        <div class="empty-note">У вас пока нет подписчиков.</div>
    {:else}
        <div class="subs-list">
            {#each $subscribersStore.slice(0, 5) as sub}
                <button
                        type="button"
                        class="subs-row"
                        on:click={openSubscribers}
                >
                    <Avatar
                            size={40}
                            src={sub.avatarUrl}
                            initials={getInitials(sub.fullName)}
                    />
                    <div class="subs-main">
                        <div class="subs-name" title={sub.fullName}>{sub.fullName}</div>
                        <div class="subs-meta">
                            <span>{sub.birthDate}</span>
                            {#if sub.wishlistTitle}
                                <span> · {sub.wishlistTitle}</span>
                            {/if}
                        </div>
                    </div>
                </button>
            {/each}
        </div>
    {/if}
</section>
</div>

<style>

/*    !* plein écran à l’intérieur de la miniapp *!*/
/*    .screen {*/
/*        flex: 1;*/
/*        display: flex;*/
/*        flex-direction: column;*/
/*        padding: 16px;*/
/*        box-sizing: border-box;*/
/*        overflow-y: auto;*/
/*    }*/

/*    .icon-btn {*/
/*        border: none;*/
/*        background: transparent;*/
/*        cursor: pointer;*/
/*        padding: 4px;*/
/*        margin-right: 4px;*/
/*    }*/

/*    .icon-btn img {*/
/*        width: 20px;*/
/*        height: 20px;*/
/*        display: block;*/
/*    }*/

/*    .btn-icon {*/
/*        width: 16px;*/
/*        height: 16px;*/
/*        margin-right: 4px;*/
/*    }*/

/*    .profile-row {*/
/*        flex: 1;*/
/*        display: flex;*/
/*        gap: 12px;*/
/*        align-items: center;*/
/*    }*/

/*    .profile-main {*/
/*        flex: 1;*/
/*    }*/

/*    .profile-name {*/
/*        flex: 1;*/
/*        font-size: 18px;*/
/*        font-weight: 600;*/
/*    }*/

/*    .profile-birth {*/
/*        font-size: 13px;*/
/*        color: #6b7280;*/
/*        margin-top: 2px;*/
/*        margin-bottom: 6px;*/
/*    }*/

/*    .profile-actions {*/
/*        display: flex;*/
/*        flex-wrap: wrap;*/
/*        gap: 4px;*/
/*    }*/

/*    .ghost-link {*/
/*        margin-top: 10px;*/
/*        padding: 8px 0 0;*/
/*        border: none;*/
/*        background: transparent;*/
/*        color: #2563eb;*/
/*        font-size: 14px;*/
/*        cursor: pointer;*/
/*    }*/

/*    .section-header {*/
/*        display: flex;*/
/*        align-items: center;*/
/*        justify-content: space-between;*/
/*        margin-bottom: 8px;*/
/*    }*/

/*    .tiny-link {*/
/*        border: none;*/
/*        background: transparent;*/
/*        color: #2563eb;*/
/*        font-size: 13px;*/
/*        cursor: pointer;*/
/*    }*/

/*    .wishlist-list {*/
/*        display: flex;*/
/*        flex-direction: column;*/
/*        gap: 6px;*/
/*        margin-bottom: 8px;*/
/*    }*/

/*    .wishlist-row {*/
/*        display: flex;*/
/*        align-items: center;*/
/*        gap: 10px;*/
/*        padding: 8px;*/
/*        width: 100%;*/
/*        border-radius: 12px;*/
/*        background: #f9fafb;*/
/*        border: 1px solid #e5e7eb;*/
/*        cursor: pointer;*/
/*        text-align: left;*/
/*    }*/

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

.btn-icon {
    width: 16px;
    height: 16px;
    margin-right: 4px;
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
    color: var(--tg-theme-hint-color, #6b7280);
    margin-top: 2px;
    margin-bottom: 6px;
}

.profile-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
}

.ghost-link {
    margin-top: 10px;
    padding: 8px 0 0;
    border: none;
    background: transparent;
    color: var(--tg-theme-link-color, #2563eb);
    font-size: 14px;
    cursor: pointer;
}

.section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
}

.tiny-link {
    border: none;
    background: transparent;
    color: var(--tg-theme-link-color, #2563eb);
    font-size: 13px;
    cursor: pointer;
}

.wishlist-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 8px;
}

.wishlist-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px;
    width: 100%;
    border-radius: 12px;
    background: var(--tg-theme-secondary-bg-color, #f9fafb);
    border: 1px solid var(--tg-theme-secondary-bg-color, #e5e7eb);
    cursor: pointer;
    text-align: left;
}


    .wishlist-cover-small {
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

    .wishlist-cover-small img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .wishlist-main-small {
        flex: 1;
    }

    .wishlist-title-small {
        font-size: 15px;
        font-weight: 500;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .wishlist-meta-small {
        font-size: 12px;
        color: #6b7280;
        margin-top: 2px;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    .privacy-chip {
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }

    .privacy-icon {
        width: 14px;
        height: 14px;
        display: block;
    }

    /* Подписки / Подписчики – тот же стиль, что и у wishlist-row */
    .subs-list {
        display: flex;
        flex-direction: column;
        gap: 6px;
        margin-bottom: 4px;
    }

    .subs-row {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px;
        width: 100%;
        border-radius: 12px;
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        cursor: pointer;
        text-align: left;
    }

    .subs-main {
        flex: 1;
    }

    .subs-name {
        font-size: 15px;
        font-weight: 500;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .subs-meta {
        font-size: 12px;
        color: #6b7280;
        margin-top: 2px;
    }


</style>