<!--<script>-->
<!--  import TextField from '$lib/components/ui/TextField.svelte';-->
<!--  import Toggle from '$lib/components/ui/Toggle.svelte';-->
<!--  import Button from '$lib/components/ui/Button.svelte';-->

<!--  export let user;-->

<!--  let fullName = user.fullName;-->
<!--  let birthDate = user.birthDate;-->
<!--  let showSubscriptions = user.showSubscriptions;-->
<!--  let textSize = user.ui.textSize;-->
<!--  let theme = user.ui.theme;-->
<!--  let notifications = { ...user.notifications };-->

<!--  let errors = {-->
<!--    fullName: '',-->
<!--    birthDate: ''-->
<!--  };-->

<!--  const validate = () => {-->
<!--    errors.fullName = '';-->
<!--    errors.birthDate = '';-->

<!--    const trimmed = fullName.trim();-->
<!--    if (!trimmed) {-->
<!--      errors.fullName = 'Имя и фамилия обязательны';-->
<!--    } else if (trimmed.length > 100) {-->
<!--      errors.fullName = 'Максимум 100 символов';-->
<!--    }-->

<!--    if (!birthDate) {-->
<!--      errors.birthDate = 'Дата рождения обязательна';-->
<!--    } else {-->
<!--      const re = /^\d{2}\.\d{2}\.\d{4}$/;-->
<!--      if (!re.test(birthDate)) {-->
<!--        errors.birthDate = 'Формат: ДД.ММ.ГГГГ';-->
<!--      }-->
<!--    }-->

<!--    return !errors.fullName && !errors.birthDate;-->
<!--  };-->

<!--  const save = () => {-->
<!--    if (!validate()) return;-->

<!--    user.fullName = fullName.trim();-->
<!--    user.birthDate = birthDate;-->
<!--    user.showSubscriptions = showSubscriptions;-->
<!--    user.ui = { textSize, theme };-->
<!--    user.notifications = { ...notifications };-->
<!--    alert('Изменения сохранены ✅');-->
<!--  };-->
<!--</script>-->


<!--<script>-->
<!--    import TextField from '$lib/components/ui/TextField.svelte';-->
<!--    import Toggle from '$lib/components/ui/Toggle.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->

<!--    export let user;-->

<!--    let fullName = user.fullName;-->
<!--    let birthDate = user.birthDate;-->
<!--    let showSubscriptions = user.showSubscriptions;-->
<!--    let textSize = user.ui.textSize;-->
<!--    let theme = user.ui.theme;-->
<!--    let notifications = { ...user.notifications };-->

<!--    let avatarPreviewUrl = user.avatarUrl || '';-->

<!--    let errors = {-->
<!--        fullName: '',-->
<!--        birthDate: ''-->
<!--    };-->

<!--    const handleAvatarChange = (event) => {-->
<!--        const file = event.target.files?.[0];-->
<!--        if (!file) return;-->
<!--        if (avatarPreviewUrl) URL.revokeObjectURL(avatarPreviewUrl);-->
<!--        avatarPreviewUrl = URL.createObjectURL(file);-->
<!--    };-->

<!--    const validate = () => {-->
<!--        errors.fullName = '';-->
<!--        errors.birthDate = '';-->

<!--        const trimmed = fullName.trim();-->
<!--        if (!trimmed) {-->
<!--            errors.fullName = 'Имя и фамилия обязательны';-->
<!--        } else if (trimmed.length > 100) {-->
<!--            errors.fullName = 'Максимум 100 символов';-->
<!--        }-->

<!--        if (!birthDate) {-->
<!--            errors.birthDate = 'Дата рождения обязательна';-->
<!--        } else {-->
<!--            const re = /^\d{2}\.\d{2}\.\d{4}$/;-->
<!--            if (!re.test(birthDate)) {-->
<!--                errors.birthDate = 'Формат: ДД.ММ.ГГГГ';-->
<!--            }-->
<!--        }-->

<!--        return !errors.fullName && !errors.birthDate;-->
<!--    };-->

<!--    const save = () => {-->
<!--        if (!validate()) return;-->

<!--        user.fullName = fullName.trim();-->
<!--        user.birthDate = birthDate;-->
<!--        user.showSubscriptions = showSubscriptions;-->
<!--        user.ui = { textSize, theme };-->
<!--        user.notifications = { ...notifications };-->
<!--        user.avatarUrl = avatarPreviewUrl; // <&#45;&#45; on sauvegarde l’URL côté front-->

<!--        alert('Изменения сохранены ✅');-->
<!--    };-->
<!--</script>-->

<script>
    import Avatar from '$lib/components/ui/Avatar.svelte';
    import TextField from '$lib/components/ui/TextField.svelte';
    import Toggle from '$lib/components/ui/Toggle.svelte';
    import Button from '$lib/components/ui/Button.svelte';

    export let user;

    let fullName = user.fullName;
    let birthDate = user.birthDate;
    let showSubscriptions = user.showSubscriptions;
    let textSize = user.ui.textSize;
    let theme = user.ui.theme;
    let notifications = {...user.notifications};

    // NEW : preview de la photo de profil
    let avatarPreviewUrl = user.avatarUrl || '';

    const handleAvatarChange = (event) => {
        const file = event.target.files?.[0];
        if (!file) return;

        if (avatarPreviewUrl) URL.revokeObjectURL(avatarPreviewUrl);
        avatarPreviewUrl = URL.createObjectURL(file);

        // plus tard tu pourras envoyer "file" à ton API
    };

    let errors = {
        fullName: '',
        birthDate: ''
    };

    const validate = () => {
        errors.fullName = '';
        errors.birthDate = '';

        const trimmed = fullName.trim();
        if (!trimmed) {
            errors.fullName = 'Имя и фамилия обязательны';
        } else if (trimmed.length > 100) {
            errors.fullName = 'Максимум 100 символов';
        }

        if (!birthDate) {
            errors.birthDate = 'Дата рождения обязательна';
        } else {
            const re = /^\d{2}\.\d{2}\.\d{4}$/;
            if (!re.test(birthDate)) {
                errors.birthDate = 'Формат: ДД.ММ.ГГГГ';
            }
        }

        return !errors.fullName && !errors.birthDate;
    };

    const save = () => {
        if (!validate()) return;

        user.fullName = fullName.trim();
        user.birthDate = birthDate;
        user.showSubscriptions = showSubscriptions;
        user.ui = {textSize, theme};
        user.notifications = {...notifications};
        user.avatarUrl = avatarPreviewUrl; // NEW : on garde l’URL

        alert('Изменения сохранены ✅');
    };
</script>


<header class="app-header">
    <div class="h1">Настройки</div>
</header>

<!--<section class="section-card">-->
<!--  <div class="h2">Профиль</div>-->
<!--  <TextField bind:value={fullName} label="Имя и фамилия" required error={errors.fullName} maxlength={100} />-->
<!--  <div style="height:8px;"></div>-->
<!--  <TextField bind:value={birthDate} label="Дата рождения" placeholder="ДД.ММ.ГГГГ" required error={errors.birthDate} />-->
<!--</section>-->


<!--<section class="section-card">-->
<!--    <div class="h2">Профиль</div>-->

<!--    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">-->
<!--        <Avatar size={72} src={avatarPreviewUrl} initials={fullName.split(' ').map(n => n[0]).join('').toUpperCase()} />-->
<!--        <label class="field">-->
<!--            <div class="field-label">Фотография профиля</div>-->
<!--            <input type="file" accept="image/*" on:change={handleAvatarChange} />-->
<!--        </label>-->
<!--    </div>-->

<!--    <TextField-->
<!--            bind:value={fullName}-->
<!--            label="Имя и фамилия"-->
<!--            required-->
<!--            error={errors.fullName}-->
<!--            maxlength={100}-->
<!--    />-->
<!--    <div style="height:8px;"></div>-->
<!--    <TextField-->
<!--            bind:value={birthDate}-->
<!--            label="Дата рождения"-->
<!--            placeholder="ДД.ММ.ГГГГ"-->
<!--            required-->
<!--            error={errors.birthDate}-->
<!--    />-->
<!--</section>-->


<section class="section-card">
    <div class="h2">Профиль</div>

    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <Avatar
                size={72}
                src={avatarPreviewUrl}
                initials={fullName
        ? fullName
          .trim()
          .split(' ')
          .map((n) => n[0])
          .join('')
          .toUpperCase()
        : '??'}
        />
        <label class="field">
            <div class="field-label">Фотография профиля</div>
            <input type="file" accept="image/*" on:change={handleAvatarChange}/>
        </label>
    </div>

    <TextField
            bind:value={fullName}
            label="Имя и фамилия"
            required
            error={errors.fullName}
            maxlength={100}
    />
    <div style="height:8px;"></div>
    <TextField
            bind:value={birthDate}
            label="Дата рождения"
            placeholder="ДД.ММ.ГГГГ"
            required
            error={errors.birthDate}
    />
</section>


<section class="section-card">
    <div class="h2">Приватность</div>
    <Toggle bind:checked={showSubscriptions} label="Показывать мои подписки"/>
</section>

<section class="section-card">
    <div class="h2">Интерфейс</div>
    <label class="field-row">
        <span>Размер текста</span>
        <select bind:value={textSize}>
            <option value="small">Малый</option>
            <option value="medium">Средний</option>
            <option value="large">Большой</option>
        </select>
    </label>
    <label class="field-row">
        <span>Тема</span>
        <select bind:value={theme}>
            <option value="light">Светлая</option>
            <option value="dark">Тёмная</option>
            <option value="system">Как в системе</option>
        </select>
    </label>
</section>

<section class="section-card">
    <div class="h2">Уведомления</div>
    <Toggle bind:checked={notifications.birthdayReminders} label="Напоминания о ДР подписок"/>
    <Toggle bind:checked={notifications.newFollowers} label="Новые подписчики"/>
    <Toggle bind:checked={notifications.postBirthday} label="После моего дня рождения"/>
    <Toggle bind:checked={notifications.wishlistRequests} label="Заявки на доступ к вишлистам"/>
</section>

<section class="section-card">
    <div class="h2">Юридическая информация</div>
    <ul class="links">
        <li><a href="https://telegram.org/privacy" target="_blank" rel="noreferrer">Политика конфиденциальности
            Telegram</a></li>
        <li><a href="https://telegram.org/tos" target="_blank" rel="noreferrer">Условия использования Telegram</a></li>
    </ul>
</section>

<div style="padding:0 16px 12px;">
    <Button full on:click={save}>Сохранить</Button>
</div>

<style>
    .field-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
        gap: 8px;
    }

    .field-row span {
        font-size: 15px;
    }

    select {
        min-width: 130px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 6px 8px;
        font-size: 14px;
    }

    .links {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 4px;
        font-size: 14px;
    }

    .links a {
        color: #2563eb;
        text-decoration: none;
    }
</style>



<!--<script>-->
<!--    import Avatar from '$lib/components/ui/Avatar.svelte';-->
<!--    import TextField from '$lib/components/ui/TextField.svelte';-->
<!--    import Toggle from '$lib/components/ui/Toggle.svelte';-->
<!--    import Button from '$lib/components/ui/Button.svelte';-->
<!--    import { userStore } from '$lib/stores/data.js';-->

<!--    export let user;-->

<!--    let fullName = user.fullName;-->
<!--    let birthDate = user.birthDate;-->
<!--    let showSubscriptions = user.showSubscriptions;-->
<!--    let textSize = user.ui.textSize;-->
<!--    let theme = user.ui.theme;-->
<!--    let notifications = { ...user.notifications };-->

<!--    let avatarPreviewUrl = user.avatarUrl || '';-->

<!--    const handleAvatarChange = (event) => {-->
<!--        const file = event.target.files?.[0];-->
<!--        if (!file) return;-->

<!--        if (avatarPreviewUrl) URL.revokeObjectURL(avatarPreviewUrl);-->
<!--        avatarPreviewUrl = URL.createObjectURL(file);-->
<!--    };-->

<!--    let errors = {-->
<!--        fullName: '',-->
<!--        birthDate: ''-->
<!--    };-->

<!--    const validate = () => {-->
<!--        errors.fullName = '';-->
<!--        errors.birthDate = '';-->

<!--        const trimmed = fullName.trim();-->
<!--        if (!trimmed) {-->
<!--            errors.fullName = 'Имя и фамилия обязательны';-->
<!--        } else if (trimmed.length > 100) {-->
<!--            errors.fullName = 'Максимум 100 символов';-->
<!--        }-->

<!--        if (!birthDate) {-->
<!--            errors.birthDate = 'Дата рождения обязательна';-->
<!--        } else {-->
<!--            const re = /^\d{2}\.\d{2}\.\d{4}$/;-->
<!--            if (!re.test(birthDate)) {-->
<!--                errors.birthDate = 'Формат: ДД.ММ.ГГГГ';-->
<!--            }-->
<!--        }-->

<!--        return !errors.fullName && !errors.birthDate;-->
<!--    };-->

<!--    const save = () => {-->
<!--        if (!validate()) return;-->

<!--        const updated = {-->
<!--            ...user,-->
<!--            fullName: fullName.trim(),-->
<!--            birthDate,-->
<!--            showSubscriptions,-->
<!--            ui: { textSize, theme },-->
<!--            notifications: { ...notifications },-->
<!--            avatarUrl: avatarPreviewUrl-->
<!--        };-->

<!--        // on met à jour le prop local (au cas où)-->
<!--        user = updated;-->
<!--        // et surtout le store global → MainScreen, ShareProfile, etc. se mettent à jour-->
<!--        userStore.set(updated);-->

<!--        alert('Изменения сохранены ✅');-->
<!--    };-->
<!--</script>-->


