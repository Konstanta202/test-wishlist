<!--&lt;!&ndash;<script>&ndash;&gt;-->
<!--&lt;!&ndash;    import Button from '$lib/components/ui/Button.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;    import Avatar from '$lib/components/ui/Avatar.svelte';&ndash;&gt;-->
<!--&lt;!&ndash;    import { createEventDispatcher } from 'svelte';&ndash;&gt;-->

<!--&lt;!&ndash;    export let user;&ndash;&gt;-->

<!--&lt;!&ndash;    const dispatch = createEventDispatcher();&ndash;&gt;-->

<!--&lt;!&ndash;    const goBack = () => dispatch('back');&ndash;&gt;-->

<!--&lt;!&ndash;    const copyLink = () => {&ndash;&gt;-->
<!--&lt;!&ndash;        // stub, plus tard tu pourras utiliser navigator.clipboard&ndash;&gt;-->
<!--&lt;!&ndash;        alert('Ссылка на профиль скопирована (заглушка)');&ndash;&gt;-->
<!--&lt;!&ndash;    };&ndash;&gt;-->
<!--&lt;!&ndash;</script>&ndash;&gt;-->

<!--&lt;!&ndash;<header class="app-header">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="h1">Поделиться профилем</div>&ndash;&gt;-->
<!--&lt;!&ndash;</header>&ndash;&gt;-->

<!--&lt;!&ndash;<section class="section-card">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="share-header">&ndash;&gt;-->
<!--&lt;!&ndash;        <Avatar size={56} src={user.avatarUrl} initials={user.fullName.split(' ').map(n => n[0]).join('').toUpperCase()} />&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="share-main">&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="share-name">{user.fullName}</div>&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="share-id">ID: {user.id}</div>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->

<!--&lt;!&ndash;    <p class="share-text">&ndash;&gt;-->
<!--&lt;!&ndash;        Отправьте ссылку на свой профиль, чтобы друзья могли видеть ваши желания и вишлисты.&ndash;&gt;-->
<!--&lt;!&ndash;    </p>&ndash;&gt;-->

<!--&lt;!&ndash;    <Button full on:click={copyLink}>Скопировать ссылку</Button>&ndash;&gt;-->

<!--&lt;!&ndash;    <div style="height:8px;"></div>&ndash;&gt;-->
<!--&lt;!&ndash;    <Button kind="ghost" full on:click={goBack}>Вернуться в профиль</Button>&ndash;&gt;-->
<!--&lt;!&ndash;</section>&ndash;&gt;-->

<!--&lt;!&ndash;<style>&ndash;&gt;-->
<!--&lt;!&ndash;    .share-header {&ndash;&gt;-->
<!--&lt;!&ndash;        display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;        align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;        gap: 10px;&ndash;&gt;-->
<!--&lt;!&ndash;        margin-bottom: 8px;&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;    .share-main {&ndash;&gt;-->
<!--&lt;!&ndash;        display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;        flex-direction: column;&ndash;&gt;-->
<!--&lt;!&ndash;        gap: 2px;&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;    .share-name {&ndash;&gt;-->
<!--&lt;!&ndash;        font-size: 16px;&ndash;&gt;-->
<!--&lt;!&ndash;        font-weight: 600;&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;    .share-id {&ndash;&gt;-->
<!--&lt;!&ndash;        font-size: 12px;&ndash;&gt;-->
<!--&lt;!&ndash;        color: #6b7280;&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;    .share-text {&ndash;&gt;-->
<!--&lt;!&ndash;        font-size: 14px;&ndash;&gt;-->
<!--&lt;!&ndash;        color: #4b5563;&ndash;&gt;-->
<!--&lt;!&ndash;        margin-bottom: 16px;&ndash;&gt;-->
<!--&lt;!&ndash;    }&ndash;&gt;-->
<!--&lt;!&ndash;</style>&ndash;&gt;-->


<!--<script>-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import { createEventDispatcher } from 'svelte';-->

<!--    // user = profil courant (id, fullName, avatarUrl, etc.)-->
<!--    export let user;-->

<!--    const dispatch = createEventDispatcher();-->

<!--    const goBack = () => dispatch('back');-->

<!--    // Génère le lien public vers le profil (pour ViewOtherProfileScreen)-->
<!--    const buildProfileLink = () => {-->
<!--        const base = window.location.origin + window.location.pathname;-->
<!--        const params = new URLSearchParams({-->
<!--            view: 'profile',   // tu pourras le lire dans ton App.svelte-->
<!--            userId: user.id-->
<!--        });-->
<!--        return `${base}?${params.toString()}`;-->
<!--    };-->

<!--    const showMessage = (text) => {-->
<!--        const tg = window.Telegram?.WebApp;-->
<!--        if (tg?.showPopup) {-->
<!--            tg.showPopup({ message: text });-->
<!--        } else {-->
<!--            alert(text);-->
<!--        }-->
<!--    };-->

<!--    const copyLink = async () => {-->
<!--        const link = buildProfileLink();-->

<!--        try {-->
<!--            if (navigator.clipboard?.writeText) {-->
<!--                await navigator.clipboard.writeText(link);-->
<!--            } else {-->
<!--                // petit fallback pour vieux navigateurs-->
<!--                const input = document.createElement('input');-->
<!--                input.value = link;-->
<!--                document.body.appendChild(input);-->
<!--                input.select();-->
<!--                document.execCommand('copy');-->
<!--                document.body.removeChild(input);-->
<!--            }-->
<!--            showMessage('Ссылка на профиль скопирована');-->
<!--        } catch (e) {-->
<!--            showMessage('Не удалось скопировать ссылку');-->
<!--        }-->
<!--    };-->

<!--    const shareInTelegram = async () => {-->
<!--        const link = buildProfileLink();-->
<!--        const tg = window.Telegram?.WebApp;-->

<!--        // Inline Mode: ouvrir la sélection de chat avec le lien prêt-->
<!--        if (tg?.switchInlineQuery) {-->
<!--            tg.switchInlineQuery(link, true);-->
<!--        } else {-->
<!--            // en dehors de Telegram → au moins on copie le lien-->
<!--            await copyLink();-->
<!--        }-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Поделиться профилем</div>-->
<!--</header>-->

<!--<section class="section-card">-->
<!--    <div class="share-header">-->
<!--        <Avatar-->
<!--                size={56}-->
<!--                src={user.avatarUrl}-->
<!--                initials={user.fullName.split(' ').map(n => n[0]).join('').toUpperCase()}-->
<!--        />-->
<!--        <div class="share-main">-->
<!--            <div class="share-name">{user.fullName}</div>-->
<!--            <div class="share-id">ID: {user.id}</div>-->
<!--        </div>-->
<!--    </div>-->

<!--    <p class="share-text">-->
<!--        Отправьте ссылку на свой профиль, чтобы друзья могли видеть ваши желания и вишлисты.-->
<!--    </p>-->

<!--    &lt;!&ndash; 1) Partager dans un chat (Inline Mode) &ndash;&gt;-->
<!--    <Button full on:click={shareInTelegram}>-->
<!--        Поделиться в Telegram-->
<!--    </Button>-->

<!--    <div style="height:8px;"></div>-->

<!--    &lt;!&ndash; 2) Copier le lien &ndash;&gt;-->
<!--    <Button full on:click={copyLink}>-->
<!--        Скопировать ссылку-->
<!--    </Button>-->

<!--    <div style="height:8px;"></div>-->

<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Вернуться в профиль-->
<!--    </Button>-->
<!--</section>-->

<!--<style>-->
<!--    .share-header {-->
<!--        display: flex;-->
<!--        align-items: center;-->
<!--        gap: 10px;-->
<!--        margin-bottom: 8px;-->
<!--    }-->
<!--    .share-main {-->
<!--        display: flex;-->
<!--        flex-direction: column;-->
<!--        gap: 2px;-->
<!--    }-->
<!--    .share-name {-->
<!--        font-size: 16px;-->
<!--        font-weight: 600;-->
<!--    }-->
<!--    .share-id {-->
<!--        font-size: 12px;-->
<!--        color: #6b7280;-->
<!--    }-->
<!--    .share-text {-->
<!--        font-size: 14px;-->
<!--        color: #4b5563;-->
<!--        margin-bottom: 16px;-->
<!--    }-->
<!--</style>-->


<!--<script>-->
<!--    import { onMount } from 'svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import { createEventDispatcher } from 'svelte';-->

<!--    export let user;-->

<!--    const dispatch = createEventDispatcher();-->
<!--    const goBack = () => dispatch('back');-->

<!--    let tg = null;-->

<!--    onMount(() => {-->
<!--        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {-->
<!--            tg = window.Telegram.WebApp;-->
<!--        }-->
<!--    });-->

<!--    const shareInTelegram = () => {-->
<!--        // 1) URL du profil dans ton bot (à adapter avec ton vrai bot)-->
<!--        const profileUrl =-->
<!--            `https://t.me/@padari_minyebot/app?startapp=profile_${user.id}`;-->

<!--        // 2) Texte qui accompagnera le lien-->
<!--        const text = `Мой профиль в «Подари мне»`;-->

<!--        // 3) URL spéciale de partage Telegram-->
<!--        const shareUrl =-->
<!--            `https://t.me/share/url?url=${encodeURIComponent(profileUrl)}&text=${encodeURIComponent(text)}`;-->

<!--        // 4) Ouvrir la fenêtre de partage-->
<!--        if (tg && tg.openTelegramLink) {-->
<!--            tg.openTelegramLink(shareUrl);-->
<!--        } else {-->
<!--            // fallback pour le dev dans le navigateur-->
<!--            window.open(shareUrl, '_blank');-->
<!--        }-->
<!--    };-->

<!--    const copyLink = async () => {-->
<!--        const profileUrl =-->
<!--            `https://t.me/@padari_minyebot/app?startapp=profile_${user.id}`;-->

<!--        try {-->
<!--            await navigator.clipboard.writeText(profileUrl);-->
<!--            alert('Ссылка на профиль скопирована');-->
<!--        } catch (e) {-->
<!--            alert('Не удалось скопировать ссылку');-->
<!--        }-->
<!--    };-->
<!--</script>-->

<!--<header class="app-header">-->
<!--    <div class="h1">Поделиться профилем</div>-->
<!--</header>-->

<!--<section class="section-card">-->
<!--    <div class="share-header">-->
<!--        <Avatar-->
<!--                size={56}-->
<!--                src={user.avatarUrl}-->
<!--                initials={user.fullName-->
<!--        .split(' ')-->
<!--        .map((n) => n[0])-->
<!--        .join('')-->
<!--        .toUpperCase()}-->
<!--        />-->
<!--        <div class="share-main">-->
<!--            <div class="share-name">{user.fullName}</div>-->
<!--            <div class="share-id">ID: {user.id}</div>-->
<!--        </div>-->
<!--    </div>-->

<!--    <p class="share-text">-->
<!--        Отправьте ссылку на свой профиль, чтобы друзья могли видеть ваши желания и-->
<!--        вишлисты.-->
<!--    </p>-->

<!--    &lt;!&ndash; 1) Partager directement dans Telegram &ndash;&gt;-->
<!--    <Button full on:click={shareInTelegram}>-->
<!--        Поделиться в Telegram-->
<!--    </Button>-->

<!--    <div style="height:8px;"></div>-->

<!--    &lt;!&ndash; 2) Garder aussi le bouton copier si tu veux &ndash;&gt;-->
<!--    <Button full kind="secondary" on:click={copyLink}>-->
<!--        Скопировать ссылку-->
<!--    </Button>-->

<!--    <div style="height:8px;"></div>-->

<!--    <Button kind="ghost" full on:click={goBack}>-->
<!--        Вернуться в профиль-->
<!--    </Button>-->
<!--</section>-->


<script>
    import { onMount } from 'svelte';
    import Button from '$lib/components/ui/Button.svelte';
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import { createEventDispatcher } from 'svelte';
    import { makeProfileUrl, makeProfileShareUrl } from '$lib/stores/data.js';

    export let user;

    const dispatch = createEventDispatcher();
    const goBack = () => dispatch('back');

    let tg = null;

    onMount(() => {
        if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
            tg = window.Telegram.WebApp;
        }
    });

    const shareInTelegram = () => {
        const shareUrl = makeProfileShareUrl(user.id);

        if (tg && tg.openTelegramLink) {
            tg.openTelegramLink(shareUrl);
        } else {
            // fallback pour dev dans le navigateur
            window.open(shareUrl, '_blank');
        }
    };

    const copyLink = async () => {
        const profileUrl = makeProfileUrl(user.id);

        try {
            await navigator.clipboard.writeText(profileUrl);
            alert('Ссылка на профиль скопирована');
        } catch (e) {
            alert('Не удалось скопировать ссылку');
        }
    };
</script>

<header class="app-header">
    <div class="h1">Поделиться профилем</div>
</header>

<section class="section-card">
    <div class="share-header">
        <Avatar
                size={56}
                src={user.avatarUrl}
                initials={user.fullName
        .split(' ')
        .map((n) => n[0])
        .join('')
        .toUpperCase()}
        />
        <div class="share-main">
            <div class="share-name">{user.fullName}</div>
            <div class="share-id">ID: {user.id}</div>
        </div>
    </div>

    <p class="share-text">
        Отправьте ссылку на свой профиль, чтобы друзья могли видеть ваши желания и
        вишлисты.
    </p>

    <!-- même style bleu pâle que le bouton "Вернуться" -->
    <Button full kind="ghost" on:click={shareInTelegram}>
        Поделиться в Telegram
    </Button>

    <div style="height:8px;"></div>

    <Button full kind="ghost" on:click={copyLink}>
        Скопировать ссылку
    </Button>

    <div style="height:8px;"></div>

    <Button kind="ghost" full on:click={goBack}>
        Вернуться в профиль
    </Button>
</section>

