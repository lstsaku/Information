# Информатика

## Данный репразиторий предназначен для хранения практических работ по Предметам МДК/ОАиП/Разработка ПМ


import customtkinter as ctk
import json
import hashlib
import os

# --- НАСТРОЙКИ ДАННЫХ И ШИФРОВАНИЯ ---
DB_FILE = "users_db.json"

def hash_password(password):
    """Превращает пароль в зашифрованную строку (SHA-256)."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Загружает базу пользователей из JSON файла."""
    if not os.path.exists(DB_FILE):
        return {} # Если файла нет, возвращаем пустой словарь
    with open(DB_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_user(username, password):
    """Сохраняет нового пользователя с зашифрованным паролем."""
    users = load_users()
    users[username] = hash_password(password)
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

# --- ИНТЕРФЕЙС И ЛОГИКА ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x600")
app.title("Защищенное приложение")

is_register_mode = False

# --- ФРЕЙМ 1: АВТОРИЗАЦИЯ И РЕГИСТРАЦИЯ ---
auth_frame = ctk.CTkFrame(master=app)
auth_frame.pack(pady=40, padx=60, fill="both", expand=True)

label_title = ctk.CTkLabel(master=auth_frame, text="Авторизация", font=("Times New Roman", 24, "bold"))
label_title.pack(pady=20)

entry_username = ctk.CTkEntry(master=auth_frame, placeholder_text="Имя пользователя", width=200)
entry_username.pack(pady=12)

entry_password = ctk.CTkEntry(master=auth_frame, placeholder_text="Пароль", show="*", width=200)
entry_password.pack(pady=12)

entry_password_confirm = ctk.CTkEntry(master=auth_frame, placeholder_text="Повторите пароль", show="*", width=200)

label_status = ctk.CTkLabel(master=auth_frame, text="", text_color="red", font=("Times New Roman", 12))
label_status.pack(pady=5)

def toggle_mode():
    global is_register_mode
    is_register_mode = not is_register_mode
    label_status.configure(text="")
    
    if is_register_mode:
        label_title.configure(text="Регистрация")
        button_main.configure(text="Создать аккаунт")
        button_toggle.configure(text="Уже есть аккаунт? Войти")
        
        label_status.pack_forget()
        button_main.pack_forget()
        button_toggle.pack_forget()
        entry_password_confirm.pack(pady=12)
        label_status.pack(pady=5)
        button_main.pack(pady=12)
        button_toggle.pack(pady=12)
    else:
        label_title.configure(text="Авторизация")
        button_main.configure(text="Войти")
        button_toggle.configure(text="Нет аккаунта? Создать")
        
        entry_password_confirm.pack_forget()
        label_status.pack_forget()
        button_main.pack_forget()
        button_toggle.pack_forget()
        label_status.pack(pady=5)
        button_main.pack(pady=12)
        button_toggle.pack(pady=12)

def process_action():
    user = entry_username.get()
    pwd = entry_password.get()

    if not user or not pwd:
        label_status.configure(text="Заполните все поля!", text_color="red")
        return

    if is_register_mode:
        pwd_conf = entry_password_confirm.get()
        if pwd != pwd_conf:
            label_status.configure(text="Пароли не совпадают!", text_color="red")
        elif len(pwd) < 4:
            label_status.configure(text="Пароль слишком короткий!", text_color="red")
        else:
            users_db = load_users()
            if user in users_db:
                label_status.configure(text="Пользователь уже существует!", text_color="red")
            else:
                save_user(user, pwd)
                label_status.configure(text="Успешно! Теперь войдите.", text_color="green")
                app.after(1500, toggle_mode) # Автоматически переключаем на окно входа
    else:
        users_db = load_users()
        # Проверяем, есть ли пользователь и совпадает ли хэш пароля
        if user in users_db and users_db[user] == hash_password(pwd):
            label_status.configure(text="")
            show_loading_screen() # Запускаем красивую анимацию загрузки
        else:
            label_status.configure(text="Неверный логин или пароль!", text_color="red")

button_main = ctk.CTkButton(master=auth_frame, text="Войти", command=process_action, width=200)
button_main.pack(pady=12)

button_toggle = ctk.CTkButton(master=auth_frame, text="Нет аккаунта? Создать", command=toggle_mode, 
                              fg_color="transparent", hover_color=("#gray70", "gray30"), text_color=("black", "white"))
button_toggle.pack(pady=12)

# --- ФРЕЙМ 2: ЭКРАН ЗАГРУЗКИ С АНИМАЦИЕЙ ---
loading_frame = ctk.CTkFrame(master=app, fg_color="transparent")

loading_label = ctk.CTkLabel(master=loading_frame, text="Вход в систему...", font=("Times New Roman", 20))
loading_label.pack(pady=(150, 20))

# Анимированный прогресс-бар
progress_bar = ctk.CTkProgressBar(master=loading_frame, width=250, mode="indeterminate")
progress_bar.pack(pady=10)

def show_loading_screen():
    # Прячем окно авторизации
    auth_frame.pack_forget()
    # Показываем окно загрузки
    loading_frame.pack(fill="both", expand=True)
    # ЗАПУСКАЕМ АНИМАЦИЮ
    progress_bar.start()
    
    # Ждем 2.5 секунды и переходим на главный экран
    app.after(2500, show_main_app_screen)

# --- ФРЕЙМ 3: ГЛАВНЫЙ ЭКРАН (После входа) ---
main_app_frame = ctk.CTkFrame(master=app)

welcome_label = ctk.CTkLabel(master=main_app_frame, text="Добро пожаловать!", font=("Times New Roman", 28, "bold"))
welcome_label.pack(pady=(100, 20))

info_label = ctk.CTkLabel(master=main_app_frame, text="Вы успешно авторизовались в системе.\nВаши данные защищены.", font=("Times New Roman", 14))
info_label.pack(pady=10)

def logout():
    main_app_frame.pack_forget()
    auth_frame.pack(pady=40, padx=60, fill="both", expand=True)
    entry_password.delete(0, 'end') # Очищаем поле пароля

logout_button = ctk.CTkButton(master=main_app_frame, text="Выйти", command=logout, fg_color="red", hover_color="darkred")
logout_button.pack(pady=40)

def show_main_app_screen():
    # Останавливаем анимацию и прячем экран загрузки
    progress_bar.stop()
    loading_frame.pack_forget()
    
    # Обновляем текст приветствия
    welcome_label.configure(text=f"Привет, {entry_username.get()}!")
    # Показываем главный экран
    main_app_frame.pack(pady=20, padx=20, fill="both", expand=True)


app.mainloop()
