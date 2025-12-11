import { writable } from 'svelte/store';

// ВИШЛИСТЫ
export const wishlistsStore = writable([
    {
        id: 1,
        title: 'День рождения',
        description: 'Идеи подарков к 25-летию',
        privacy: 'public',      // public | restricted | private
        coverUrl: '',
        count: 3
    },

    {
        id: 3,
        title: '8-ого марта ',
        description: 'Идеи подарков на 8-ого ммарта',
        privacy: 'public',
        count: 3
        // rUrl: '/icons/gift2.svg'
    },

    {
        id: 4,
        title: '18-ого мая  ',
        description: 'Flag day',
        privacy: 'public',
        count: 3

    },

    {
        id: 6,
        title: 'Marriage',
        description: 'Shopping du siecle',
        privacy: 'public',
        count: 3


    },

]);

// ЖЕЛАНИЯ
export const wishesStore = writable([
    {
        id: 1,
        title: 'Наушники с шумоподавлением',
        price: 15000,
        currency: '₽',
        // imageUrl: 'static/icons/gitf1.svg',
        pinned: true,
        wishlistIds: [1]
        // массив id вишлистов, где лежит желание
    },
    {
        id: 2,
        title: 'Книга по продуктовому дизайну',
        price: 2500,
        currency: '₽',
        // imageUrl: 'https://www.ozon.ru/product/dizayn-myshlenie-kanvasy-i-uprazhneniya-polnyy-nabor-instrumentov-levrik-mihael-link-patrik-408869625/?at=K8tZpNMkWtVKlv39TERBRQZURXNE2zSG9p4mCyjNwWn',
        pinned: false,
        wishlistIds: [3]
    },
    {
        id: 101,
        title: 'Новые наушники',
        wishlistIds: [4]
    },
    {
        id: 102,
        title: 'Книга по фотографии',
        // wishlistIds: [6]
    },

]);

// Анкета: интересы / что не дарить, по пользователю
export const questionnaireStore = writable({
    interests: [],
    noGifts: []
});

// Подписки (на кого я подписан)
export const subscriptionsStore = writable([
    // structure пример, потом подменишь реальными данными
    {
      id: 'user-2',
      fullName: 'Иван Иванов',
      birthDate: '05.04.1995',
      avatarUrl: '',
      wishlistTitle: 'Новый год'
    },

    {
        id: 'u-ivan',
        fullName: 'Иван Иванов',
        birthDate: '05.04.1995',
        mainWishlistTitle: 'Новый год'
    },


    {
        id: 'sub-1',
        fullName: 'Ива нов',
        birthDate: '05.04.2005',
        mainOccasion: 'Новый год'
    },
    {
        id: 'sub-2',
        fullName: 'Катя Петрова',
        birthDate: '11.01.1998',
        mainOccasion: 'День рождения'
    },

    {
        id: 'f-1',
        fullName: 'Мари Марква',
        birthDate: '10.09.1990',
        mainOccasion: 'День рождения'
    },
    {
        id: 'f-2',
        fullName: 'Кирилл',
        birthDate: '10.10.2000',
        mainOccasion: 'Новый год'
    },

    {
        id: 'sub-4',
        fullName: 'Кат Перва',
        birthDate: '11.04.1998',
        mainOccasion: 'День рождения'
    },

    {
        id: 'u-maria',
        fullName: 'Мария Маркова',
        birthDate: '10.09.1990',
        mainWishlistTitle: 'День рождения'
    },



]);

// Подписчики (кто подписан на меня)
export const subscribersStore = writable([
    {
      id: 'user-3',
      fullName: 'Мария Маркова',
      birthDate: '10.09.1990',
      avatarUrl: '',
      wishlistTitle: 'День рождения'
    },
    {
        id: 'sub-4',
        fullName: 'Кат Перва',
        birthDate: '11.01.1999',
        mainOccasion: 'День рождения'
    },
    {
        id: 'sub-8',
        fullName: 'Ив нов',
        birthDate: '05.04.1999',
        mainOccasion: 'Новый год'
    },

    {
        id: 'f-1',
        fullName: 'Мари Марка',
        birthDate: '10.09.2009',
        mainOccasion: 'День рождения'
    },

    {
        id: 'u-maria',
        fullName: 'Мария Маркова',
        birthDate: '10.09.1990',
        avatarUrl: '',
        isSubscribed: false,
        publicWishlists: [
            {
                id: 'wl-birthday',
                title: 'День рождения',
                visibility: 'public',
                wishesCount: 4,
                iconUrl: '/icons/wishlist-card.png'
            }
        ],
        subscriptions: [
            {
                id: 'sub-ivan',
                fullName: 'Иван Иванов',
                birthDate: '05.04.1995',
                wishlistTitle: 'Новый год',
                avatarUrl: ''
            }
        ],
        questionnaire: {
            interests: ['книги', 'фотография', 'путешествия'],
            noGifts: ['мягкие игрушки', 'алкоголь']
        }
    },

    {
        id: 'u-maria',
        fullName: 'Мария Маркова',
        birthDate: '10.09.1990',
        avatarUrl: '',
        isSubscribed: false,
        publicWishlists: [
            {
                id: 'wl-birthday',
                title: 'День рождения',
                visibility: 'public',
                wishesCount: 4,
                iconUrl: '/icons/wishlist-card.png'
            }
        ],
        subscriptions: [
            {
                id: 'sub-ivan',
                fullName: 'Иван Иванов',
                birthDate: '05.04.1995',
                wishlistTitle: 'Новый год',
                avatarUrl: ''
            }
        ],
        questionnaire: {
            interests: ['книги', 'фотография', 'путешествия'],
            noGifts: ['мягкие игрушки', 'алкоголь']
        },






    }



]);



export const demoAnnaProfile = {
    id: 'u-anna',
    fullName: 'Анна Подаркова',
    birthDate: '12.03.1998',
    avatarUrl: '',
    isSubscribed: false,

    publicWishlists: [
        {
            id: 1,
            title: 'День рождения',
            visibility: 'private',
            wishesCount: 1,
            iconUrl: '/icons/wishlist-card.png'
        },
        {
            id: 2,
            title: '8-ого марта',
            visibility: 'public',
            wishesCount: 1,
            iconUrl: '/icons/wishlist-card.png'
        }
    ],

    subscriptions: [
        {
            id: 'u-ivan',
            fullName: 'Иван Иванов',
            birthDate: '05.04.1995',
            wishlistTitle: 'Новый год',
            avatarUrl: ''
        }
    ],

    questionnaire: {
        interests: ['Книги по дизайну', 'Украшения', 'Сертификаты в спа'],
        noGifts: ['Алкоголь', 'Сладости с орехами']
    }
};




// --- Config partage / liens Telegram ---

// TON username de bot sans @
export const BOT_USERNAME = 'padari_minyebot';

// Nom de l’app pour le texte de partage
export const APP_NAME = 'Подари мне';

// URL deep-link vers le profil dans la mini-app
export const makeProfileUrl = (userId) =>
    `https://t.me/${BOT_USERNAME}/app?startapp=profile_${encodeURIComponent(
        userId
    )}`;

// URL de partage Telegram (ouvre la fenêtre "choisir un chat")
export const makeProfileShareUrl = (userId) => {
    const profileUrl = makeProfileUrl(userId);
    const text = `Мой профиль в «${APP_NAME}»`;

    return `https://t.me/share/url?url=${encodeURIComponent(
        profileUrl
    )}&text=${encodeURIComponent(text)}`;
};

// --- Мок-данные профилей других пользователей для экрана OtherProfileScreen ---

export const otherProfilesMock = {
    // пример: Мария Маркова
    'u-maria': {
        id: 'u-maria',
        fullName: 'Мария Маркова',
        birthDate: '10.09.1990',
        avatarUrl: '',
        isSubscribed: false,

        // Публичные вишлисты пользователя
        publicWishlists: [
            {
                id: 201,
                title: 'День рождения',
                visibility: 'public',
                wishesCount: 1,
                iconUrl: '/icons/wishlist-card.png'
            },
            {
                id: 202,
                title: 'Новый год',
                visibility: 'public',
                wishesCount: 3,
                iconUrl: '/icons/wishlist-card.png'
            }
        ],

        // На кого он сам подписан
        subscriptions: [
            {
                id: 'u-ivan',
                fullName: 'Иван Иванов',
                birthDate: '05.04.1995',
                wishlistTitle: 'Новый год',
                avatarUrl: ''
            },
            {
                id: 'u-katya',
                fullName: 'Катя Петрова',
                birthDate: '11.01.1998',
                wishlistTitle: 'День рождения',
                avatarUrl: ''
            }
        ],

        // Краткое содержание анкеты
        questionnaire: {
            interests: ['Книги', 'Путешествия', 'Аксессуары', 'Декор для дома'],
            noGifts: ['Сладкое', 'Домашние животные']
        }
    }
};

//  TEST SETTINGS



export const userStore = writable({
    id: 'demo-user-1',
    fullName: 'Анна Подаркова',
    birthDate: '12.03.1998',
    avatarUrl: '',
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
});



//
// // --- Config partage / liens Telegram ---
//
// // Mets ici TON vrai username de bot sans @
// export const BOT_USERNAME = 'padari_minyebot';
//
// // Nom de l’app, pour le texte de partage
// export const APP_NAME = 'Подари мне';
//
// // URL deep-link vers le profil dans la mini-app
// export const makeProfileUrl = (userId) =>
//     `https://t.me/${BOT_USERNAME}/app?startapp=profile_${userId}`;
//
// // URL de partage Telegram (ouvre la fenêtre "choisir un chat")
// export const makeProfileShareUrl = (userId) => {
//     const profileUrl = makeProfileUrl(userId);
//     const text = `Мой профиль в «${APP_NAME}»`;
//
//     return `https://t.me/share/url?url=${encodeURIComponent(
//         profileUrl
//     )}&text=${encodeURIComponent(text)}`;
//
//
//
// };


