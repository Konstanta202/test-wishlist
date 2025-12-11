# 🎁 Подари мне — Frontend Telegram Mini App

**Полное описание проекта (Frontend)**

Этот проект представляет собой фронтенд для Telegram Mini App «Подари мне». Он разработан на **SvelteKit + Vite** и обеспечивает весь пользовательский интерфейс:
профиль, анкета, желания, вишлисты, подписки, подписчики и просмотр других профилей.

---

## 📦 1. Структура проекта

```
src/
  app.html
  routes/
    +layout.svelte
    +page.svelte
  lib/
    components/
      screens/
      ui/
    stores/
svelte.config.js
vite.config.js
package.json
```

---

## 📘 2. Описание файлов

### **vite.config.js**

Конфигурация Vite:

* подключает SvelteKit
* задаёт host = 0.0.0.0 (необходимо для Telegram, Docker, ngrok)
* указывает порт 5173

---

### **svelte.config.js**

* конфигурация SvelteKit
* подключение `adapter-node`, если используется продакшн-билд
* препроцессоры

---

### **src/app.html**

Основной HTML-шаблон, куда SvelteKit вставляет приложение.

---

### **src/routes/+layout.svelte**

Главный layout:

* инициализация Telegram WebApp API
* общие контейнеры и стили
* обёртка для всех страниц

---

### **src/routes/+page.svelte**

Точка входа интерфейса.
Здесь происходит:

* импорт всех экранов
* хранение текущего экрана (`currentScreen`)
* логика навигации
* открытие профилей других пользователей
* привязка к stores

---

# 🧠 3. Stores (глобальное состояние)

Файл: `src/lib/stores/data.js`

Содержит:

* данные пользователя
* желания (wishes)
* вишлисты (wishlists)
* подписки
* подписчиков
* состояние интерфейса

Stores автоматически обновляют UI при изменении.

---

# 🖥️ 4. Экраны (screens)

Все экраны находятся в `src/lib/components/screens/`.

### **StartScreen.svelte**

Стартовое окно, загрузка данных.

### **MainScreen.svelte**

Профиль пользователя + основные разделы.

### **SettingsScreen.svelte**

Настройки профиля, темы, уведомлений, приватности.

### **QuestionnaireScreen.svelte**

Анкета: интересы, «что не дарить», валидация.

### **WishesScreen.svelte**

Все желания:

* создание
* редактирование
* удаление
* закрепление
* исполнение

### **WishlistsScreen.svelte**

Управление вишлистами:

* создание / удаление
* приватность
* доступ
* добавление желаний

### **SubscriptionsScreen.svelte**

Список подписок.

### **SubscribersScreen.svelte**

Список подписчиков с возможностью блокировки.

### **ShareProfileScreen.svelte**

Экран генерации и отправки ссылки на профиль.

### **OtherProfileScreen.svelte**

Просмотр чужого профиля.

---

# 🎨 UI-компоненты (ui/)

### **Button.svelte**

Кнопка.

### **Avatar.svelte**

Аватар пользователя.

### **TextField.svelte**

Поле ввода.


---

# 🔄 5. Как работает приложение

1. Telegram передает данные пользователя в WebApp.
2. Приложение запрашивает профиль и данные через backend API.
3. Store обновляется и UI перерисовывается.
4. Навигация управляется переменной `currentScreen`.
5. Все изменения (анкета, желания, вишлисты) уходят через API.

---

# ▶️ 6. Запуск

### Dev-режим:

```
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

### Docker (dev):

```
docker build -t sveltekit-frontend .
docker run -p 5173:5173 sveltekit-frontend
```

---

# 🎁 Podari Mne — Frontend Telegram Mini App

**Complete Project Description (Frontend)**

This repository contains the frontend of the Telegram Mini App “Podari Mne”.
It is built with **SvelteKit + Vite** and provides all user-facing UI:
profile, questionnaire, wishes, wishlists, subscriptions, subscribers, and viewing other users’ profiles.

---

## 📦 1. Project Structure

```
src/
  app.html
  routes/
    +layout.svelte
    +page.svelte
  lib/
    components/
      screens/
      ui/
    stores/
svelte.config.js
vite.config.js
package.json
```

---

## 📘 2. File Descriptions

### **vite.config.js**

Vite configuration:

* integrates SvelteKit
* sets host = 0.0.0.0 (required for Telegram, Docker, ngrok)
* exposes port 5173

---

### **svelte.config.js**

* SvelteKit configuration
* adapter configuration (`adapter-node` for production builds)
* preprocessors

---

### **src/app.html**

Base HTML template.
SvelteKit injects the app here.

---

### **src/routes/+layout.svelte**

Main layout:

* initializes Telegram WebApp API
* provides global styling/wrappers
* wraps all screens

---

### **src/routes/+page.svelte**

Main UI entry point.
Handles:

* importing all screens
* `currentScreen` navigation logic
* opening other users’ profiles
* binding to stores

---

# 🧠 3. Stores (global state)

File: `src/lib/stores/data.js`

Contains:

* user data
* wishes
* wishlists
* subscriptions
* subscribers
* UI state

Stores automatically update UI when modified.

---

# 🖥️ 4. Screens

Located in `src/lib/components/screens/`.

### **StartScreen.svelte**

App startup, initialization.

### **MainScreen.svelte**

User profile + main sections.

### **SettingsScreen.svelte**

Profile settings, theme, notifications, privacy.

### **QuestionnaireScreen.svelte**

Questionnaire: interests, restrictions, validation.

### **WishesScreen.svelte**

Wish management:
create, edit, delete, pin, mark as completed.

### **WishlistsScreen.svelte**

Wishlist management:
create, edit, privacy, access, add wishes.

### **SubscriptionsScreen.svelte**

List of subscriptions.

### **SubscribersScreen.svelte**

List of subscribers with blocking option.

### **ShareProfileScreen.svelte**

Profile link generation and sharing.

### **OtherProfileScreen.svelte**

Viewing another user’s public profile.

---

# 🎨 UI Components

### **Button.svelte**

Universal button.

### **Avatar.svelte**

User avatar with fallback.

### **TextField.svelte**

Reusable input field.


---

# 🔄 5. How the App Works

1. Telegram WebApp API sends user data.
2. Frontend fetches user profile & wishlists from backend API.
3. Stores are updated → UI re-renders automatically.
4. Navigation is controlled via `currentScreen`.
5. All changes (questionnaire, wishes, wishlists) are sent to backend API.

---

# ▶️ 6. Running the App

### Dev mode:

```
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

### Docker (dev):

```
docker build -t sveltekit-frontend .
docker run -p 5173:5173 sveltekit-frontend
```

---
