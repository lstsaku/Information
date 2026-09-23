# Информатика

## Данный репразиторий предназначен для хранения практических работ по Предметам МДК/ОАиП/Разработка ПМ


import customtkinter as ctk

# Базовая настройка
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x550")
app.title("Стильное приложение 2.0")

# Глобальная переменная для отслеживания текущего режима (Вход / Регистрация)
is_register_mode = False

# Фрейм-контейнер
frame = ctk.CTkFrame(master=app)
frame.pack(pady=40, padx=60, fill="both", expand=True)

label_title = ctk.CTkLabel(master=frame, text="Авторизация", font=("Times New Roman", 24, "bold"))
label_title.pack(pady=20, padx=10)

entry_username = ctk.CTkEntry(master=frame, placeholder_text="Имя пользователя", width=200)
entry_username.pack(pady=12, padx=10)

entry_password = ctk.CTkEntry(master=frame, placeholder_text="Пароль", show="*", width=200)
entry_password.pack(pady=12, padx=10)

# Поле подтверждения пароля (Скрыто по умолчанию)
entry_password_confirm = ctk.CTkEntry(master=frame, placeholder_text="Повторите пароль", show="*", width=200)

# Текстовое поле для вывода ошибок и статусов (Изначально пустое)
label_status = ctk.CTkLabel(master=frame, text="", text_color="red", font=("Times New Roman", 12))
label_status.pack(pady=5)

# --- ЛОГИКА И АНИМАЦИИ ИНТЕРФЕЙСА ---

def toggle_mode():
    """Переключает интерфейс между Входом и Регистрацией, скрывая и показывая элементы."""
    global is_register_mode
    is_register_mode = not is_register_mode
    
    # Сбрасываем текст ошибок
    label_status.configure(text="")
    
    if is_register_mode:
        label_title.configure(text="Регистрация")
        button_main.configure(text="Создать аккаунт")
        button_toggle.configure(text="Уже есть аккаунт? Войти")
        
        # Динамически перерисовываем интерфейс: убираем кнопки, вставляем новое поле, возвращаем кнопки
        label_status.pack_forget()
        button_main.pack_forget()
        button_toggle.pack_forget()
        
        entry_password_confirm.pack(pady=12, padx=10) # Показываем подтверждение пароля
        
        label_status.pack(pady=5)
        button_main.pack(pady=12, padx=10)
        button_toggle.pack(pady=12)
    else:
        label_title.configure(text="Авторизация")
        button_main.configure(text="Войти")
        button_toggle.configure(text="Нет аккаунта? Создать")
        
        entry_password_confirm.pack_forget() # Скрываем подтверждение пароля
        
        label_status.pack_forget()
        button_main.pack_forget()
        button_toggle.pack_forget()
        
        label_status.pack(pady=5)
        button_main.pack(pady=12, padx=10)
        button_toggle.pack(pady=12)

def process_action():
    """Анимация загрузки: блокирует кнопку на время 'проверки'."""
    button_main.configure(state="disabled", text="Обработка...")
    label_status.configure(text="")
    
    # Имитация задержки сервера в 1 секунду (1000 мс). 
    # Это позволяет избежать зависания окна по сравнению с time.sleep()
    app.after(1000, validate_data)

def validate_data():
    """Логика проверки паролей и авторизации."""
    button_main.configure(state="normal")
    user = entry_username.get()
    pwd = entry_password.get()

    # Проверка на пустые поля
    if not user or not pwd:
        label_status.configure(text="Заполните все поля!", text_color="red")
        restore_button_text()
        return

    if is_register_mode:
        pwd_conf = entry_password_confirm.get()
        # Проверка регистрации
        if pwd != pwd_conf:
            label_status.configure(text="Пароли не совпадают!", text_color="red")
        elif len(pwd) < 6:
            label_status.configure(text="Пароль должен быть от 6 символов!", text_color="red")
        else:
            label_status.configure(text="Аккаунт успешно создан!", text_color="green")
            # Здесь можно добавить логику сохранения пользователя в базу данных
    else:
        # Проверка авторизации (Тестовые данные)
        if user == "admin" and pwd == "123456":
            label_status.configure(text="Успешный вход!", text_color="green")
        else:
            label_status.configure(text="Неверный логин или пароль!", text_color="red")
            
    restore_button_text()

def restore_button_text():
    if is_register_mode:
        button_main.configure(text="Создать аккаунт")
    else:
        button_main.configure(text="Войти")

# --- КНОПКИ ---

button_main = ctk.CTkButton(master=frame, text="Войти", command=process_action, width=200)
button_main.pack(pady=12, padx=10)

# Прозрачная кнопка для переключения режимов
button_toggle = ctk.CTkButton(master=frame, text="Нет аккаунта? Создать", command=toggle_mode, 
                              fg_color="transparent", hover_color=("#gray70", "gray30"), text_color=("black", "white"))
button_toggle.pack(pady=12)

app.mainloop()
