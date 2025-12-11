<!--&lt;!&ndash;<script>&ndash;&gt;-->
<!--&lt;!&ndash;  import { onMount } from 'svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import StartScreen from '$lib/components/screens/StartScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import MainScreen from '$lib/components/screens/MainScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import WishesScreen from '$lib/components/screens/WishesScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;  import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';&ndash;&gt;-->

<!--&lt;!&ndash;  let currentScreen = 'start';&ndash;&gt;-->

<!--&lt;!&ndash;  let user = {&ndash;&gt;-->
<!--&lt;!&ndash;    id: 'demo-user-1',&ndash;&gt;-->
<!--&lt;!&ndash;    fullName: 'Анна Подаркова',&ndash;&gt;-->
<!--&lt;!&ndash;    birthDate: '12.03.1998',&ndash;&gt;-->
<!--&lt;!&ndash;    avatarUrl: '',&ndash;&gt;-->
<!--&lt;!&ndash;    showSubscriptions: true,&ndash;&gt;-->
<!--&lt;!&ndash;    ui: {&ndash;&gt;-->
<!--&lt;!&ndash;      textSize: 'medium',&ndash;&gt;-->
<!--&lt;!&ndash;      theme: 'system'&ndash;&gt;-->
<!--&lt;!&ndash;    },&ndash;&gt;-->
<!--&lt;!&ndash;    notifications: {&ndash;&gt;-->
<!--&lt;!&ndash;      birthdayReminders: true,&ndash;&gt;-->
<!--&lt;!&ndash;      newFollowers: true,&ndash;&gt;-->
<!--&lt;!&ndash;      postBirthday: true,&ndash;&gt;-->
<!--&lt;!&ndash;      wishlistRequests: true&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;  };&ndash;&gt;-->

<!--&lt;!&ndash;  const navigate = (to) => {&ndash;&gt;-->
<!--&lt;!&ndash;    currentScreen = to;&ndash;&gt;-->
<!--&lt;!&ndash;  };&ndash;&gt;-->

<!--&lt;!&ndash;  onMount(() => {&ndash;&gt;-->
<!--&lt;!&ndash;    if (typeof window !== 'undefined' && window.Telegram && window.Telegram.WebApp) {&ndash;&gt;-->
<!--&lt;!&ndash;      const tg = window.Telegram.WebApp;&ndash;&gt;-->
<!--&lt;!&ndash;      tg.ready();&ndash;&gt;-->
<!--&lt;!&ndash;      tg.expand();&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;  });&ndash;&gt;-->
<!--&lt;!&ndash;</script>&ndash;&gt;-->

<!--&lt;!&ndash;{#if currentScreen === 'start'}&ndash;&gt;-->
<!--&lt;!&ndash;  <StartScreen on:start={() => navigate('main')} />&ndash;&gt;-->
<!--&lt;!&ndash;{:else}&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="app-scroll">&ndash;&gt;-->
<!--&lt;!&ndash;    {#if currentScreen === 'main'}&ndash;&gt;-->
<!--&lt;!&ndash;      <MainScreen&ndash;&gt;-->
<!--&lt;!&ndash;        {user}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openSettings={() => navigate('settings')}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openQuestionnaire={() => navigate('questionnaire')}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openWishes={() => navigate('wishes')}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openWishlists={() => navigate('wishlists')}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openSubscriptions={() => navigate('subscriptions')}&ndash;&gt;-->
<!--&lt;!&ndash;        on:openSubscribers={() => navigate('subscribers')}&ndash;&gt;-->
<!--&lt;!&ndash;      />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'settings'}&ndash;&gt;-->
<!--&lt;!&ndash;      <SettingsScreen {user} />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'questionnaire'}&ndash;&gt;-->
<!--&lt;!&ndash;      <QuestionnaireScreen />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'wishes'}&ndash;&gt;-->
<!--&lt;!&ndash;      <WishesScreen />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'wishlists'}&ndash;&gt;-->
<!--&lt;!&ndash;      <WishlistsScreen />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'subscriptions'}&ndash;&gt;-->
<!--&lt;!&ndash;      <SubscriptionsScreen />&ndash;&gt;-->
<!--&lt;!&ndash;    {:else if currentScreen === 'subscribers'}&ndash;&gt;-->
<!--&lt;!&ndash;      <SubscribersScreen />&ndash;&gt;-->
<!--&lt;!&ndash;    {/if}&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->

<!--&lt;!&ndash;  <nav class="tab-bar">&ndash;&gt;-->
<!--&lt;!&ndash;    <button class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`} type="button" on:click={() => navigate('main')}>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>🏠</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>Главная</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;    </button>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`} type="button" on:click={() => navigate('wishes')}>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>🎁</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>Желания</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;    </button>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`} type="button" on:click={() => navigate('wishlists')}>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>📋</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>Вишлисты</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;    </button>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`} type="button" on:click={() => navigate('subscriptions')}>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>👀</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>Подписки</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;    </button>&ndash;&gt;-->
<!--&lt;!&ndash;    <button class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`} type="button" on:click={() => navigate('settings')}>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>⚙️</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span>Настройки</span>&ndash;&gt;-->
<!--&lt;!&ndash;      <span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;    </button>&ndash;&gt;-->
<!--&lt;!&ndash;  </nav>&ndash;&gt;-->
<!--&lt;!&ndash;{/if}&ndash;&gt;-->

<!--<script>-->
<!--    import { onMount } from 'svelte';-->
<!--    import StartScreen from '$lib/components/screens/StartScreen.svelte';-->
<!--    import MainScreen from '$lib/components/screens/MainScreen.svelte';-->
<!--    import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';-->
<!--    import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';-->
<!--    import WishesScreen from '$lib/components/screens/WishesScreen.svelte';-->
<!--    import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';-->
<!--    import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';-->
<!--    import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';-->
<!--    import ShareProfileScreen from '$lib/components/screens/ShareProfileScreen.svelte';-->
<!--    import OtherProfileScreen from '$lib/components/screens/OtherProfileScreen.svelte';-->




<!--    let currentScreen = 'start';-->
<!--    let viewedProfile = null;  // NEW-->

<!--    let user = {-->
<!--        id: 'demo-user-1',-->
<!--        fullName: 'Анна Подаркова',-->
<!--        birthDate: '12.03.1998',-->
<!--        avatarUrl: '',-->
<!--        showSubscriptions: true,-->
<!--        ui: {-->
<!--            textSize: 'medium',-->
<!--            theme: 'system'-->
<!--        },-->
<!--        notifications: {-->
<!--            birthdayReminders: true,-->
<!--            newFollowers: true,-->
<!--            postBirthday: true,-->
<!--            wishlistRequests: true-->
<!--        }-->
<!--    };-->

<!--    function openOtherProfile(profile) {-->
<!--        viewedProfile = profile;-->
<!--        currentScreen = 'otherProfile';-->
<!--    }-->


<!--    function navigate(screen) {-->
<!--        currentScreen = screen;-->
<!--    }-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram && window.Telegram.WebApp) {-->
<!--            const tg = window.Telegram.WebApp;-->
<!--            tg.ready();-->
<!--            tg.expand();-->
<!--        }-->
<!--    });-->
<!--</script>-->
<!--<div class="screen">-->
<!--&lt;!&ndash;{#if currentScreen === 'start'}&ndash;&gt;-->
<!--&lt;!&ndash;    <StartScreen on:start={() => navigate('main')} />&ndash;&gt;-->
<!--&lt;!&ndash;{:else}&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="app-shell">&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="app-scroll">&ndash;&gt;-->
<!--&lt;!&ndash;            {#if currentScreen === 'main'}&ndash;&gt;-->
<!--&lt;!&ndash;                <MainScreen&ndash;&gt;-->
<!--&lt;!&ndash;                        {user}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openSettings={() => navigate('settings')}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openQuestionnaire={() => navigate('questionnaire')}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openWishes={() => navigate('wishes')}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openWishlists={() => navigate('wishlists')}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openSubscriptions={() => navigate('subscriptions')}&ndash;&gt;-->
<!--&lt;!&ndash;                        on:openSubscribers={() => navigate('subscribers')}&ndash;&gt;-->
<!--&lt;!&ndash;                />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'settings'}&ndash;&gt;-->
<!--&lt;!&ndash;                <SettingsScreen {user} />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'questionnaire'}&ndash;&gt;-->
<!--&lt;!&ndash;                <QuestionnaireScreen />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'wishes'}&ndash;&gt;-->
<!--&lt;!&ndash;                <WishesScreen />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'wishlists'}&ndash;&gt;-->
<!--&lt;!&ndash;                <WishlistsScreen />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'subscriptions'}&ndash;&gt;-->
<!--&lt;!&ndash;                <SubscriptionsScreen />&ndash;&gt;-->
<!--&lt;!&ndash;            {:else if currentScreen === 'subscribers'}&ndash;&gt;-->
<!--&lt;!&ndash;                <SubscribersScreen />&ndash;&gt;-->
<!--&lt;!&ndash;            {/if}&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->

<!--&lt;!&ndash;        <nav class="tab-bar">&ndash;&gt;-->
<!--&lt;!&ndash;            <button&ndash;&gt;-->
<!--&lt;!&ndash;                    type="button"&ndash;&gt;-->
<!--&lt;!&ndash;                    class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}&ndash;&gt;-->
<!--&lt;!&ndash;                    on:click={() => navigate('main')}&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;                <span>🏠</span><span>Главная</span><span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;            </button>&ndash;&gt;-->
<!--&lt;!&ndash;            <button&ndash;&gt;-->
<!--&lt;!&ndash;                    type="button"&ndash;&gt;-->
<!--&lt;!&ndash;                    class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}&ndash;&gt;-->
<!--&lt;!&ndash;                    on:click={() => navigate('wishes')}&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;                <span>🎁</span><span>Желания</span><span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;            </button>&ndash;&gt;-->
<!--&lt;!&ndash;            <button&ndash;&gt;-->
<!--&lt;!&ndash;                    type="button"&ndash;&gt;-->
<!--&lt;!&ndash;                    class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}&ndash;&gt;-->
<!--&lt;!&ndash;                    on:click={() => navigate('wishlists')}&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;                <span>📋</span><span>Вишлисты</span><span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;            </button>&ndash;&gt;-->
<!--&lt;!&ndash;            <button&ndash;&gt;-->
<!--&lt;!&ndash;                    type="button"&ndash;&gt;-->
<!--&lt;!&ndash;                    class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}&ndash;&gt;-->
<!--&lt;!&ndash;                    on:click={() => navigate('subscriptions')}&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;                <span>👀</span><span>Подписки</span><span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;            </button>&ndash;&gt;-->
<!--&lt;!&ndash;            <button&ndash;&gt;-->
<!--&lt;!&ndash;                    type="button"&ndash;&gt;-->
<!--&lt;!&ndash;                    class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}&ndash;&gt;-->
<!--&lt;!&ndash;                    on:click={() => navigate('settings')}&ndash;&gt;-->
<!--&lt;!&ndash;            >&ndash;&gt;-->
<!--&lt;!&ndash;                <span>⚙️</span><span>Настройки</span><span class="tab-dot"></span>&ndash;&gt;-->
<!--&lt;!&ndash;            </button>&ndash;&gt;-->
<!--&lt;!&ndash;        </nav>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->
<!--&lt;!&ndash;{/if}&ndash;&gt;-->


<!--{#if currentScreen === 'start'}-->
<!--    &lt;!&ndash; Start a sa propre mise en page mais dans le même "cadre" &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <StartScreen on:start={() => navigate('main')} />-->
<!--    </div>-->
<!--{:else}-->
<!--    <div class="app-root">-->
<!--        <div class="app-scroll">-->

<!--            {#if currentScreen === 'main'}-->
<!--                <MainScreen-->
<!--                        {user}-->
<!--                        on:openSettings={() => navigate('settings')}-->
<!--                        on:openQuestionnaire={() => navigate('questionnaire')}-->
<!--                        on:openWishes={() => navigate('wishes')}-->
<!--                        on:openWishlists={() => navigate('wishlists')}-->
<!--                        on:openSubscriptions={() => navigate('subscriptions')}-->
<!--                        on:openSubscribers={() => navigate('subscribers')}-->
<!--                        on:openShareProfile={() => navigate('shareProfile')}-->
<!--                />-->
<!--            {:else if currentScreen === 'settings'}-->
<!--                <SettingsScreen {user} />-->
<!--            {:else if currentScreen === 'questionnaire'}-->
<!--                <QuestionnaireScreen />-->
<!--            {:else if currentScreen === 'wishes'}-->
<!--                <WishesScreen />-->
<!--            {:else if currentScreen === 'wishlists'}-->
<!--                <WishlistsScreen />-->
<!--            {:else if currentScreen === 'subscriptions'}-->
<!--                <SubscriptionsScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->
<!--            {:else if currentScreen === 'subscribers'}-->
<!--                <SubscribersScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->
<!--            {:else if currentScreen === 'shareProfile'}-->
<!--                <ShareProfileScreen {user} on:back={() => navigate('main')} />-->
<!--            {:else if currentScreen === 'otherProfile'}-->
<!--                {#if viewedProfile}-->
<!--&lt;!&ndash;                    <OtherProfileScreen {profile=viewedProfile} on:back={() => navigate('main')} />&ndash;&gt;-->
<!--                    <OtherProfileScreen-->
<!--                            profile={viewedProfile}-->
<!--                            on:back={() => navigate('main')}-->
<!--                    />-->

<!--                {/if}-->
<!--            {/if}-->


<!--            &lt;!&ndash;{#if currentScreen === 'main'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <MainScreen&ndash;&gt;-->
<!--            &lt;!&ndash;            {user}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openSettings={() => navigate('settings')}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openQuestionnaire={() => navigate('questionnaire')}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openWishes={() => navigate('wishes')}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openWishlists={() => navigate('wishlists')}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openSubscriptions={() => navigate('subscriptions')}&ndash;&gt;-->
<!--            &lt;!&ndash;            on:openSubscribers={() => navigate('subscribers')}&ndash;&gt;-->
<!--            &lt;!&ndash;    />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'settings'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <SettingsScreen {user} />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'questionnaire'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <QuestionnaireScreen />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'wishes'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <WishesScreen />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'wishlists'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <WishlistsScreen />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'subscriptions'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <SubscriptionsScreen />&ndash;&gt;-->
<!--            &lt;!&ndash;{:else if currentScreen === 'subscribers'}&ndash;&gt;-->
<!--            &lt;!&ndash;    <SubscribersScreen />&ndash;&gt;-->
<!--            &lt;!&ndash;{/if}&ndash;&gt;-->




<!--        </div>-->

<!--        <nav class="tab-bar">-->
<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('main')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-home.png" alt="" />-->
<!--                <span>Главная</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishes')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-gift.png" alt="" />-->
<!--                <span>Желания</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishlists')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-list.png" alt="" />-->
<!--                <span>Вишлисты</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('subscriptions')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-eye.png" alt="" />-->
<!--                <span>Подписки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('settings')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-settings.png" alt="" />-->
<!--                <span>Настройки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->
<!--        </nav>-->
<!--    </div>-->
<!--{/if}-->
<!--</div>-->

<!--<style>-->

<!--    /* plein écran à l’intérieur de la miniapp */-->
<!--    .screen {-->
<!--        flex: 1;-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        padding: 16px;-->
<!--        box-sizing: border-box;-->
<!--        overflow-y: auto;-->
<!--    }-->


<!--    .app-root {-->
<!--        min-height: 100vh;-->
<!--        width: 100%;-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        align-items: center;-->
<!--        background: #ffffff;          /* même fond que StartScreen */-->
<!--    }-->

<!--    .app-scroll {-->
<!--        width: 100%;-->
<!--        max-width: 430px;             /* largeur iPhone */-->
<!--        flex: 1;-->
<!--        overflow-y: auto;-->
<!--        padding-bottom: 72px;         /* espace pour la tab-bar */-->
<!--        background: #ffffff;-->
<!--    }-->

<!--    .tab-bar {-->
<!--        position: fixed;-->
<!--        bottom: 0;-->
<!--        left: 50%;-->
<!--        transform: translateX(-50%);-->
<!--        width: 100%;-->
<!--        max-width: 430px;             /* aligné sur le contenu */-->
<!--        height: 64px;-->
<!--        background: #ffffff;-->
<!--        border-top: 1px solid #e5e7eb;-->
<!--        display: flex;-->
<!--        justify-content: space-around;-->
<!--        align-items: center;-->
<!--    }-->

<!--    .tab-item {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        align-items: center;-->
<!--        gap: 2px;-->
<!--        border: none;-->
<!--        background: transparent;-->
<!--        font-size: 11px;-->
<!--        color: #6b7280;-->
<!--        cursor: pointer;-->
<!--        padding: 4px 6px;-->
<!--    }-->

<!--    .tab-icon {-->
<!--        width: 22px;-->
<!--        height: 22px;-->
<!--        object-fit: contain;-->
<!--    }-->

<!--    .tab-item.active {-->
<!--        color: #2563eb;-->
<!--    }-->

<!--    .tab-dot {-->
<!--        width: 5px;-->
<!--        height: 5px;-->
<!--        border-radius: 999px;-->
<!--        background: transparent;-->
<!--    }-->

<!--    .tab-item.active .tab-dot {-->
<!--        background: #2563eb;-->
<!--    }-->


<!--     :global(html, body) {-->
<!--         margin: 0;-->
<!--         padding: 0;-->
<!--         height: 100%;-->
<!--         background: #ffffff;-->
<!--         overflow-x: hidden; /* NEW : pas de scroll horizontal */-->
<!--         scrollbar-width: none;-->
<!--     }-->



<!--</style>-->

<!--<script>-->
<!--    import { onMount } from 'svelte';-->
<!--    import StartScreen from '$lib/components/screens/StartScreen.svelte';-->
<!--    import MainScreen from '$lib/components/screens/MainScreen.svelte';-->
<!--    import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';-->
<!--    import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';-->
<!--    import WishesScreen from '$lib/components/screens/WishesScreen.svelte';-->
<!--    import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';-->
<!--    import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';-->
<!--    import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';-->
<!--    import ShareProfileScreen from '$lib/components/screens/ShareProfileScreen.svelte';-->
<!--    import OtherProfileScreen from '$lib/components/screens/OtherProfileScreen.svelte';-->

<!--    import { demoAnnaProfile } from '$lib/stores/data.js';-->

<!--    // let currentScreen = 'other-profile';-->


<!--    let currentScreen = 'start';-->
<!--    let viewedProfile = null;-->

<!--    let user = {-->
<!--        id: 'demo-user-1',-->
<!--        fullName: 'Анна Подаркова',-->
<!--        birthDate: '12.03.1998',-->
<!--        avatarUrl: '',-->
<!--        showSubscriptions: true,-->
<!--        ui: {-->
<!--            textSize: 'medium',-->
<!--            theme: 'system'-->
<!--        },-->
<!--        notifications: {-->
<!--            birthdayReminders: true,-->
<!--            newFollowers: true,-->
<!--            postBirthday: true,-->
<!--            wishlistRequests: true-->
<!--        }-->
<!--    };-->

<!--    function navigate(screen) {-->
<!--        currentScreen = screen;-->
<!--    }-->

<!--    function openOtherProfile(profile) {-->
<!--        viewedProfile = profile;-->
<!--        currentScreen = 'otherProfile';-->
<!--    }-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram && window.Telegram.WebApp) {-->
<!--            const tg = window.Telegram.WebApp;-->
<!--            tg.ready();-->
<!--            tg.expand();-->
<!--        }-->
<!--    });-->
<!--</script>-->

<!--{#if currentScreen === 'start'}-->
<!--    &lt;!&ndash; Écran de démarrage plein écran &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <StartScreen on:start={() => navigate('main')} />-->
<!--    </div>-->
<!--{:else}-->
<!--    &lt;!&ndash; Shell commun : header + contenu scrollable + tab-bar &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <div class="app-scroll">-->
<!--            {#if currentScreen === 'other-profile'}-->
<!--                <OtherProfileScreen-->
<!--                        profile={demoAnnaProfile}-->
<!--                        on:back={() => console.log('Назад (здесь вернёшься на Главную)')}-->
<!--                        on:toggle-subscribe={(e) => console.log('subscribe toggle', e.detail)}-->
<!--                        on:show-all-wishlists={(e) => console.log('show all wishlists', e.detail)}-->
<!--                        on:show-all-subscriptions={(e) => console.log('show all subs', e.detail)}-->
<!--                        on:open-questionnaire={(e) => console.log('open questionnaire', e.detail)}-->
<!--                />-->
<!--            {/if}-->

<!--            {#if currentScreen === 'main'}-->
<!--                <MainScreen-->
<!--                        {user}-->
<!--                        on:openSettings={() => navigate('settings')}-->
<!--                        on:openQuestionnaire={() => navigate('questionnaire')}-->
<!--                        on:openWishes={() => navigate('wishes')}-->
<!--                        on:openWishlists={() => navigate('wishlists')}-->
<!--                        on:openSubscriptions={() => navigate('subscriptions')}-->
<!--                        on:openSubscribers={() => navigate('subscribers')}-->
<!--                        on:openShareProfile={() => navigate('shareProfile')}-->
<!--                />-->
<!--            {:else if currentScreen === 'settings'}-->
<!--                <SettingsScreen {user} />-->
<!--            {:else if currentScreen === 'questionnaire'}-->
<!--                <QuestionnaireScreen />-->
<!--            {:else if currentScreen === 'wishes'}-->
<!--                <WishesScreen />-->
<!--            {:else if currentScreen === 'wishlists'}-->
<!--                <WishlistsScreen />-->
<!--            {:else if currentScreen === 'subscriptions'}-->
<!--                <SubscriptionsScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />-->
<!--            {:else if currentScreen === 'subscribers'}-->
<!--                <SubscribersScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />-->
<!--            {:else if currentScreen === 'shareProfile'}-->
<!--                <ShareProfileScreen {user} on:back={() => navigate('main')} />-->
<!--            {:else if currentScreen === 'otherProfile'}-->
<!--                {#if viewedProfile}-->
<!--                    <OtherProfileScreen-->
<!--                            profile={viewedProfile}-->
<!--                            on:back={() => navigate('main')}-->
<!--                    />-->
<!--                {/if}-->
<!--            {/if}-->
<!--        </div>-->

<!--        <nav class="tab-bar">-->
<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('main')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-home.png" alt="" />-->
<!--                <span>Главная</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishes')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-gift.png" alt="" />-->
<!--                <span>Желания</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishlists')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-list.png" alt="" />-->
<!--                <span>Вишлисты</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('subscriptions')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-eye.png" alt="" />-->
<!--                <span>Подписки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('settings')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-settings.png" alt="" />-->
<!--                <span>Настройки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->
<!--        </nav>-->
<!--    </div>-->
<!--{/if}-->

<!--<style>-->

<!--</style>-->




<!--&lt;!&ndash;Teste User-Anna&ndash;&gt;-->

<!--<script>-->
<!--    import { onMount } from 'svelte';-->

<!--    import StartScreen from '$lib/components/screens/StartScreen.svelte';-->
<!--    import MainScreen from '$lib/components/screens/MainScreen.svelte';-->
<!--    import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';-->
<!--    import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';-->
<!--    import WishesScreen from '$lib/components/screens/WishesScreen.svelte';-->
<!--    import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';-->
<!--    import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';-->
<!--    import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';-->
<!--    import ShareProfileScreen from '$lib/components/screens/ShareProfileScreen.svelte';-->
<!--    import OtherProfileScreen from '$lib/components/screens/OtherProfileScreen.svelte';-->

<!--    // pour tester Анну как «invité»-->
<!--    import { demoAnnaProfile } from '$lib/stores/data.js';-->

<!--    // écran actuel-->
<!--    let currentScreen = 'start';        // 'start' au début-->
<!--    let viewedProfile = null;           // профиль, который мы смотрим как гость-->

<!--    // ton utilisateur courant (Анна Подаркова)-->
<!--    let user = {-->
<!--        id: 'demo-user-1',-->
<!--        fullName: 'Анна Подаркова',-->
<!--        birthDate: '12.03.1998',-->
<!--        avatarUrl: '',-->
<!--        showSubscriptions: true,-->
<!--        ui: {-->
<!--            textSize: 'medium',-->
<!--            theme: 'system'-->
<!--        },-->
<!--        notifications: {-->
<!--            birthdayReminders: true,-->
<!--            newFollowers: true,-->
<!--            postBirthday: true,-->
<!--            wishlistRequests: true-->
<!--        }-->
<!--    };-->

<!--    function navigate(screen) {-->
<!--        currentScreen = screen;-->
<!--    }-->

<!--    // appelé quand on clique sur quelqu’un dans Subscriptions / Subscribers-->
<!--    function openOtherProfile(profile) {-->
<!--        viewedProfile = profile;-->
<!--        currentScreen = 'otherProfile';-->
<!--    }-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram && window.Telegram.WebApp) {-->
<!--            const tg = window.Telegram.WebApp;-->
<!--            tg.ready();-->
<!--            tg.expand();-->
<!--        }-->

<!--        // 👉 Pour tester l’écran invité с Анной напрямую, dé-commente :-->
<!--        viewedProfile = demoAnnaProfile;-->
<!--        currentScreen = 'otherProfile';-->
<!--    });-->
<!--</script>-->

<!--{#if currentScreen === 'start'}-->
<!--    &lt;!&ndash; Écran de démarrage plein écran &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <StartScreen on:start={() => navigate('main')} />-->
<!--    </div>-->
<!--{:else}-->
<!--    &lt;!&ndash; Shell commun &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <div class="app-scroll">-->
<!--            {#if currentScreen === 'main'}-->
<!--                <MainScreen-->
<!--                        {user}-->
<!--                        on:openSettings={() => navigate('settings')}-->
<!--                        on:openQuestionnaire={() => navigate('questionnaire')}-->
<!--                        on:openWishes={() => navigate('wishes')}-->
<!--                        on:openWishlists={() => navigate('wishlists')}-->
<!--                        on:openSubscriptions={() => navigate('subscriptions')}-->
<!--                        on:openSubscribers={() => navigate('subscribers')}-->
<!--                        on:openShareProfile={() => navigate('shareProfile')}-->
<!--                />-->

<!--            {:else if currentScreen === 'settings'}-->
<!--                <SettingsScreen {user} />-->

<!--            {:else if currentScreen === 'questionnaire'}-->
<!--                <QuestionnaireScreen />-->

<!--            {:else if currentScreen === 'wishes'}-->
<!--                <WishesScreen />-->

<!--            {:else if currentScreen === 'wishlists'}-->
<!--                <WishlistsScreen />-->

<!--            {:else if currentScreen === 'subscriptions'}-->
<!--                &lt;!&ndash; клик по пользователю -> openOtherProfile &ndash;&gt;-->
<!--                <SubscriptionsScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />-->

<!--            {:else if currentScreen === 'subscribers'}-->
<!--                <SubscribersScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />-->

<!--            {:else if currentScreen === 'shareProfile'}-->
<!--                <ShareProfileScreen {user} on:back={() => navigate('main')} />-->

<!--            {:else if currentScreen === 'otherProfile'}-->
<!--                {#if viewedProfile}-->
<!--                    <OtherProfileScreen-->
<!--                            profile={viewedProfile}-->
<!--                            on:back={() => navigate('main')}-->
<!--                            on:toggle-subscribe={(e) => console.log('subscribe toggle', e.detail)}-->
<!--                            on:show-all-wishlists={() => navigate('wishlists')}-->
<!--                            on:show-all-subscriptions={() => navigate('subscriptions')}-->
<!--                            on:open-questionnaire={() => navigate('questionnaire')}-->
<!--                    />-->
<!--                {/if}-->
<!--            {/if}-->
<!--        </div>-->

<!--        &lt;!&ndash; Tab bar &ndash;&gt;-->
<!--        <nav class="tab-bar">-->
<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('main')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-home.png" alt="" />-->
<!--                <span>Главная</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishes')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-gift.png" alt="" />-->
<!--                <span>Желания</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishlists')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-list.png" alt="" />-->
<!--                <span>Вишлисты</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('subscriptions')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-eye.png" alt="" />-->
<!--                <span>Подписки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('settings')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-settings.png" alt="" />-->
<!--                <span>Настройки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->
<!--        </nav>-->
<!--    </div>-->
<!--{/if}-->

<!--<style>-->
<!--    /* tes styles ici */-->
<!--</style>-->

<!--VERSION FINALE-->

<!--<script>-->
<!--    import { onMount } from 'svelte';-->

<!--    import StartScreen from '$lib/components/screens/StartScreen.svelte';-->
<!--    import MainScreen from '$lib/components/screens/MainScreen.svelte';-->
<!--    import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';-->
<!--    import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';-->
<!--    import WishesScreen from '$lib/components/screens/WishesScreen.svelte';-->
<!--    import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';-->
<!--    import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';-->
<!--    import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';-->
<!--    import ShareProfileScreen from '$lib/components/screens/ShareProfileScreen.svelte';-->
<!--    import OtherProfileScreen from '$lib/components/screens/OtherProfileScreen.svelte';-->

<!--    // écran actuel-->
<!--    let currentScreen = 'start';-->
<!--    let viewedProfile = null;-->

<!--    // utilisateur courant (celui connecté)-->
<!--    let user = {-->
<!--        id: 'demo-user-1',-->
<!--        fullName: 'Анна Подаркова',-->
<!--        birthDate: '12.03.1998',-->
<!--        avatarUrl: '',-->
<!--        showSubscriptions: true,-->
<!--        ui: {-->
<!--            textSize: 'medium',-->
<!--            theme: 'system'-->
<!--        },-->
<!--        notifications: {-->
<!--            birthdayReminders: true,-->
<!--            newFollowers: true,-->
<!--            postBirthday: true,-->
<!--            wishlistRequests: true-->
<!--        }-->
<!--    };-->

<!--    function navigate(screen) {-->
<!--        currentScreen = screen;-->
<!--    }-->

<!--    function openOtherProfile(profile) {-->
<!--        viewedProfile = profile;-->
<!--        currentScreen = 'otherProfile';-->
<!--    }-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {-->
<!--            const tg = window.Telegram.WebApp;-->
<!--            tg.ready();-->
<!--            tg.expand();-->
<!--        }-->
<!--    });-->
<!--</script>-->

<!--{#if currentScreen === 'start'}-->
<!--    <div class="app-root">-->
<!--        <StartScreen on:start={() => navigate('main')} />-->
<!--    </div>-->

<!--{:else}-->
<!--    <div class="app-root">-->
<!--        <div class="app-scroll">-->

<!--            {#if currentScreen === 'main'}-->
<!--                <MainScreen-->
<!--                        {user}-->
<!--                        on:openSettings={() => navigate('settings')}-->
<!--                        on:openQuestionnaire={() => navigate('questionnaire')}-->
<!--                        on:openWishes={() => navigate('wishes')}-->
<!--                        on:openWishlists={() => navigate('wishlists')}-->
<!--                        on:openSubscriptions={() => navigate('subscriptions')}-->
<!--                        on:openSubscribers={() => navigate('subscribers')}-->
<!--                        on:openShareProfile={() => navigate('shareProfile')}-->
<!--                />-->

<!--            {:else if currentScreen === 'settings'}-->
<!--                <SettingsScreen {user} />-->

<!--            {:else if currentScreen === 'questionnaire'}-->
<!--                <QuestionnaireScreen />-->

<!--            {:else if currentScreen === 'wishes'}-->
<!--                <WishesScreen />-->

<!--            {:else if currentScreen === 'wishlists'}-->
<!--                <WishlistsScreen />-->

<!--            {:else if currentScreen === 'subscriptions'}-->
<!--                <SubscriptionsScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->

<!--            {:else if currentScreen === 'subscribers'}-->
<!--                <SubscribersScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->

<!--            {:else if currentScreen === 'shareProfile'}-->
<!--                <ShareProfileScreen-->
<!--                        {user}-->
<!--                        on:back={() => navigate('main')}-->
<!--                />-->

<!--            {:else if currentScreen === 'otherProfile'}-->
<!--                {#if viewedProfile}-->
<!--                    <OtherProfileScreen-->
<!--                            profile={viewedProfile}-->
<!--                            on:back={() => navigate('main')}-->
<!--                            on:toggle-subscribe={(e) => console.log('toggle', e.detail)}-->
<!--                            on:show-all-wishlists={() => navigate('wishlists')}-->
<!--                            on:show-all-subscriptions={() => navigate('subscriptions')}-->
<!--                    />-->
<!--                {/if}-->
<!--            {/if}-->

<!--        </div>-->

<!--        <nav class="tab-bar">-->
<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('main')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-home.png" alt="" />-->
<!--                <span>Главная</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishes')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-gift.png" alt="" />-->
<!--                <span>Желания</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('wishlists')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-list.png" alt="" />-->
<!--                <span>Вишлисты</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('subscriptions')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-eye.png" alt="" />-->
<!--                <span>Подписки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}-->
<!--                    on:click={() => navigate('settings')}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-settings.png" alt="" />-->
<!--                <span>Настройки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->
<!--        </nav>-->
<!--    </div>-->
<!--{/if}-->

<!--<style>-->
<!--    /* tes styles comme avant */-->
<!--</style>-->


<!--&lt;!&ndash;TEST USER NOTIFICATION&ndash;&gt;-->

<!--<script>-->
<!--    import { onMount } from "svelte";-->

<!--    // Écrans-->
<!--    import StartScreen from "$lib/components/screens/StartScreen.svelte";-->
<!--    import MainScreen from "$lib/components/screens/MainScreen.svelte";-->
<!--    import SettingsScreen from "$lib/components/screens/SettingsScreen.svelte";-->
<!--    import QuestionnaireScreen from "$lib/components/screens/QuestionnaireScreen.svelte";-->
<!--    import WishesScreen from "$lib/components/screens/WishesScreen.svelte";-->
<!--    import WishlistsScreen from "$lib/components/screens/WishlistsScreen.svelte";-->
<!--    import SubscriptionsScreen from "$lib/components/screens/SubscriptionsScreen.svelte";-->
<!--    import SubscribersScreen from "$lib/components/screens/SubscribersScreen.svelte";-->
<!--    import ShareProfileScreen from "$lib/components/screens/ShareProfileScreen.svelte";-->
<!--    import OtherProfileScreen from "$lib/components/screens/OtherProfileScreen.svelte";-->

<!--    // État de navigation-->
<!--    let currentScreen = "start";-->
<!--    let viewedProfile = null;-->

<!--    // User de test (le même qu’avant)-->
<!--    let user = {-->
<!--        id: "demo-user-1",-->
<!--        fullName: "Анна Подаркова",-->
<!--        birthDate: "12.03.1998",-->
<!--        avatarUrl: "",-->
<!--        showSubscriptions: true,-->
<!--        ui: {-->
<!--            textSize: "medium",-->
<!--            theme: "system"-->
<!--        },-->
<!--        notifications: {-->
<!--            birthdayReminders: true,-->
<!--            newFollowers: true,-->
<!--            postBirthday: true,-->
<!--            wishlistRequests: true-->
<!--        }-->
<!--    };-->

<!--    function navigate(screen) {-->
<!--        currentScreen = screen;-->
<!--    }-->

<!--    function openOtherProfile(profile) {-->
<!--        viewedProfile = profile;-->
<!--        currentScreen = "otherProfile";-->
<!--    }-->

<!--    onMount(() => {-->
<!--        if (typeof window !== "undefined" && window.Telegram?.WebApp) {-->
<!--            const tg = window.Telegram.WebApp;-->
<!--            tg.ready();-->
<!--            tg.expand();-->
<!--        }-->
<!--    });-->
<!--</script>-->

<!--{#if currentScreen === "start"}-->
<!--    &lt;!&ndash; Écran de démarrage &ndash;&gt;-->
<!--    <div class="app-root">-->
<!--        <StartScreen on:start={() => navigate("main")} />-->
<!--    </div>-->
<!--{:else}-->
<!--    &lt;!&ndash; Shell principal &ndash;&gt;-->

<!--    <div class={`app-root text-${user.ui.textSize} theme-${user.ui.theme}`}>-->

<!--&lt;!&ndash;    <div class="app-root">&ndash;&gt;-->
<!--        <div class="app-scroll">-->
<!--            {#if currentScreen === "main"}-->
<!--                <MainScreen-->
<!--                        {user}-->
<!--                        on:openSettings={() => navigate("settings")}-->
<!--                        on:openQuestionnaire={() => navigate("questionnaire")}-->
<!--                        on:openWishes={() => navigate("wishes")}-->
<!--                        on:openWishlists={() => navigate("wishlists")}-->
<!--                        on:openSubscriptions={() => navigate("subscriptions")}-->
<!--                        on:openSubscribers={() => navigate("subscribers")}-->
<!--                        on:openShareProfile={() => navigate("shareProfile")}-->
<!--                />-->

<!--            {:else if currentScreen === "settings"}-->
<!--                <SettingsScreen {user} />-->

<!--            {:else if currentScreen === "questionnaire"}-->
<!--                <QuestionnaireScreen />-->

<!--            {:else if currentScreen === "wishes"}-->
<!--                <WishesScreen />-->

<!--            {:else if currentScreen === "wishlists"}-->
<!--                <WishlistsScreen />-->

<!--            {:else if currentScreen === "subscriptions"}-->
<!--                <SubscriptionsScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->

<!--            {:else if currentScreen === "subscribers"}-->
<!--                <SubscribersScreen-->
<!--                        on:openProfile={(e) => openOtherProfile(e.detail.profile)}-->
<!--                />-->

<!--            {:else if currentScreen === "shareProfile"}-->
<!--                <ShareProfileScreen {user} on:back={() => navigate("main")} />-->

<!--            {:else if currentScreen === "otherProfile"}-->
<!--                {#if viewedProfile}-->
<!--                    <OtherProfileScreen-->
<!--                            profile={viewedProfile}-->
<!--                            on:back={() => navigate("main")}-->
<!--                    />-->
<!--                {/if}-->
<!--            {/if}-->
<!--        </div>-->

<!--        &lt;!&ndash; Tab bar &ndash;&gt;-->
<!--        <nav class="tab-bar">-->
<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === "main" ? "active" : ""}`}-->
<!--                    on:click={() => navigate("main")}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-home.png" alt="" />-->
<!--                <span>Главная</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === "wishes" ? "active" : ""}`}-->
<!--                    on:click={() => navigate("wishes")}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-gift.png" alt="" />-->
<!--                <span>Желания</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === "wishlists" ? "active" : ""}`}-->
<!--                    on:click={() => navigate("wishlists")}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-list.png" alt="" />-->
<!--                <span>Вишлисты</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === "subscriptions" ? "active" : ""}`}-->
<!--                    on:click={() => navigate("subscriptions")}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-eye.png" alt="" />-->
<!--                <span>Подписки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->

<!--            <button-->
<!--                    type="button"-->
<!--                    class={`tab-item ${currentScreen === "settings" ? "active" : ""}`}-->
<!--                    on:click={() => navigate("settings")}-->
<!--            >-->
<!--                <img class="tab-icon" src="/icons/tab-settings.png" alt="" />-->
<!--                <span>Настройки</span>-->
<!--                <span class="tab-dot"></span>-->
<!--            </button>-->
<!--        </nav>-->
<!--    </div>-->
<!--{/if}-->

<!--<style>-->
<!--    /* si tu avais déjà des styles globaux ici, remets-les */-->

<!--    /* taille de base */-->
<!--    .app-root {-->
<!--        font-size: 16px;-->
<!--        background-color: #f3f4f6;-->
<!--        color: #111827;-->
<!--    }-->

<!--    /* -&#45;&#45;&#45;&#45; TEST Размер текста -&#45;&#45;&#45;&#45; */-->
<!--    .app-root.text-small {-->
<!--        font-size: 14px;-->
<!--    }-->

<!--    .app-root.text-medium {-->
<!--        font-size: 16px;-->
<!--    }-->

<!--    .app-root.text-large {-->
<!--        font-size: 18px;-->
<!--    }-->

<!--    /* -&#45;&#45;&#45;&#45; TEST Тема -&#45;&#45;&#45;&#45; */-->
<!--    .app-root.theme-light {-->
<!--        background-color: #f3f4f6;-->
<!--        color: #111827;-->
<!--    }-->

<!--    .app-root.theme-dark {-->
<!--        background-color: #020617;  /* fond foncé */-->
<!--        color: #f9fafb;             /* texte clair */-->
<!--    }-->

<!--    .app-root.theme-system {-->
<!--        /* pour le test on laisse comme medium/light */-->
<!--    }-->

<!--</style>-->


<script>
    import { onMount } from 'svelte';

    import StartScreen from '$lib/components/screens/StartScreen.svelte';
    import MainScreen from '$lib/components/screens/MainScreen.svelte';
    import SettingsScreen from '$lib/components/screens/SettingsScreen.svelte';
    import QuestionnaireScreen from '$lib/components/screens/QuestionnaireScreen.svelte';
    import WishesScreen from '$lib/components/screens/WishesScreen.svelte';
    import WishlistsScreen from '$lib/components/screens/WishlistsScreen.svelte';
    import SubscriptionsScreen from '$lib/components/screens/SubscriptionsScreen.svelte';
    import SubscribersScreen from '$lib/components/screens/SubscribersScreen.svelte';
    import ShareProfileScreen from '$lib/components/screens/ShareProfileScreen.svelte';
    import OtherProfileScreen from '$lib/components/screens/OtherProfileScreen.svelte';

    import { userStore } from '$lib/stores/data.js';

    let currentScreen = 'start';
    let viewedProfile = null;

    // user vient du store
    $: user = $userStore;

    function navigate(screen) {
        currentScreen = screen;
    }

    function openOtherProfile(profile) {
        viewedProfile = profile;
        currentScreen = 'otherProfile';
    }

    onMount(() => {
        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
            const tg = window.Telegram.WebApp;
            tg.ready();
            tg.expand();
        }
    });
</script>

{#if !user}
    <!-- Si jamais le user n'est pas encore chargé -->
    <div class="app-root light medium">
        Загрузка...
    </div>
{:else}
    {#if currentScreen === 'start'}
        <div class="app-root {user.ui.theme} {user.ui.textSize}">
            <StartScreen on:start={() => navigate('main')} />
        </div>
    {:else}
        <div class="app-root {user.ui.theme} {user.ui.textSize}">
            <div class="app-scroll">
                {#if currentScreen === 'main'}
                    <MainScreen
                            {user}
                            on:openSettings={() => navigate('settings')}
                            on:openQuestionnaire={() => navigate('questionnaire')}
                            on:openWishes={() => navigate('wishes')}
                            on:openWishlists={() => navigate('wishlists')}
                            on:openSubscriptions={() => navigate('subscriptions')}
                            on:openSubscribers={() => navigate('subscribers')}
                            on:openShareProfile={() => navigate('shareProfile')}
                    />
                {:else if currentScreen === 'settings'}
                    <SettingsScreen {user} />
                {:else if currentScreen === 'questionnaire'}
                    <QuestionnaireScreen />
                {:else if currentScreen === 'wishes'}
                    <WishesScreen />
                {:else if currentScreen === 'wishlists'}
                    <WishlistsScreen />
                {:else if currentScreen === 'subscriptions'}
                    <SubscriptionsScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />
                {:else if currentScreen === 'subscribers'}
                    <SubscribersScreen on:openProfile={(e) => openOtherProfile(e.detail.profile)} />
                {:else if currentScreen === 'shareProfile'}
                    <ShareProfileScreen {user} on:back={() => navigate('main')} />
                {:else if currentScreen === 'otherProfile'}
                    {#if viewedProfile}
                        <OtherProfileScreen
                                profile={viewedProfile}
                                on:back={() => navigate('main')}
                        />
                    {/if}
                {/if}
            </div>

            <!-- TAB BAR -->
            <nav class="tab-bar">
                <button
                        type="button"
                        class={`tab-item ${currentScreen === 'main' ? 'active' : ''}`}
                        on:click={() => navigate('main')}
                >
                    <img class="tab-icon" src="/icons/tab-home.png" alt="" />
                    <span>Главная</span>
                    <span class="tab-dot"></span>
                </button>

                <button
                        type="button"
                        class={`tab-item ${currentScreen === 'wishes' ? 'active' : ''}`}
                        on:click={() => navigate('wishes')}
                >
                    <img class="tab-icon" src="/icons/tab-gift.png" alt="" />
                    <span>Желания</span>
                    <span class="tab-dot"></span>
                </button>

                <button
                        type="button"
                        class={`tab-item ${currentScreen === 'wishlists' ? 'active' : ''}`}
                        on:click={() => navigate('wishlists')}
                >
                    <img class="tab-icon" src="/icons/tab-list.png" alt="" />
                    <span>Вишлисты</span>
                    <span class="tab-dot"></span>
                </button>

                <button
                        type="button"
                        class={`tab-item ${currentScreen === 'subscriptions' ? 'active' : ''}`}
                        on:click={() => navigate('subscriptions')}
                >
                    <img class="tab-icon" src="/icons/tab-eye.png" alt="" />
                    <span>Подписки</span>
                    <span class="tab-dot"></span>
                </button>

                <button
                        type="button"
                        class={`tab-item ${currentScreen === 'settings' ? 'active' : ''}`}
                        on:click={() => navigate('settings')}
                >
                    <img class="tab-icon" src="/icons/tab-settings.png" alt="" />
                    <span>Настройки</span>
                    <span class="tab-dot"></span>
                </button>
            </nav>
        </div>
    {/if}
{/if}

<style>

</style>



<!--PEUT_ETRE FINAL GLOBLAL-->


