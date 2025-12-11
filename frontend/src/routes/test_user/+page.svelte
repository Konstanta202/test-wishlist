<!--http://localhost:5173/test_user-->

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

    // Анна как «демо-профиль»
    import { demoAnnaProfile } from '$lib/stores/data.js';

    // экран actuel
    let currentScreen = 'start';
    let viewedProfile = null;

    // ton utilisateur courant (Анна Подаркова)
    // IMPORTANT : même id que demoAnnaProfile
    let user = {
        id: demoAnnaProfile.id,          // 'u-anna'
        fullName: demoAnnaProfile.fullName,
        birthDate: demoAnnaProfile.birthDate,
        avatarUrl: demoAnnaProfile.avatarUrl || '',
        showSubscriptions: true,
        ui: {
            textSize: 'medium',
            theme: 'system'
        },
        notifications: {
            birthdayReminders: true,
            newFollowers: true,
            postBirthday: true,
            wishlistRequests: true
        }
    };

    function navigate(screen) {
        currentScreen = screen;
    }

    // appelé quand on clique sur quelqu’un dans Subscriptions / Subscribers
    function openOtherProfile(profile) {
        viewedProfile = profile;
        currentScreen = 'otherProfile';
    }

    onMount(() => {
        // 1) Cas TELEGRAM : on lit start_param
        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
            const tg = window.Telegram.WebApp;
            tg.ready();
            tg.expand();

            const startParam = tg.initDataUnsafe?.start_param;

            // lien du type ...?startapp=profile_u-anna
            if (startParam && startParam.startsWith('profile_')) {
                const profileId = decodeURIComponent(
                    startParam.slice('profile_'.length)
                );

                if (profileId === demoAnnaProfile.id) {
                    // on ouvre directement le profil d'Анна comme invité
                    viewedProfile = demoAnnaProfile;
                    currentScreen = 'otherProfile';
                    return;
                }

                // plus tard : ici tu pourras faire un fetch vers ton backend
                // pour charger d'autres profils par id
            }

            // si pas de start_param spécial -> flow normal
            currentScreen = 'start';
        } else {
            // 2) Cas NAVIGATEUR (dev local) :
            // on montre directement Анну comme invité pour tester l'écran
            viewedProfile = demoAnnaProfile;
            currentScreen = 'otherProfile';
        }
    });
</script>

{#if currentScreen === 'start'}
    <!-- Écran de démarrage plein écran -->
    <div class="app-root">
        <StartScreen on:start={() => navigate('main')} />
    </div>
{:else}
    <!-- Shell commun -->
    <div class="app-root">
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
                <!-- клик по пользователю -> openOtherProfile -->
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
                            on:toggle-subscribe={(e) => console.log('subscribe toggle', e.detail)}
                            on:show-all-wishlists={() => navigate('wishlists')}
                            on:show-all-subscriptions={() => navigate('subscriptions')}
                            on:open-questionnaire={() => navigate('questionnaire')}
                    />
                {/if}
            {/if}
        </div>

        <!-- Tab bar -->
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

<style>
    /* tes styles ici */
</style>
