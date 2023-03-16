def some_function():
    for i in range(4):
        yield i
for i in some_function():
    print(i)

####################################################################

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)

# Создание курсора
cur = conn.cursor()

# Выполнение запроса
cur.execute("SELECT * FROM table_name")

# Получение результатов
rows = cur.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие соединения с базой данных
cur.close()
conn.close()

################################################################

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)

# Создание курсора
cur = conn.cursor()

# Открытие файла изображения в двоичном режиме
with open("image.jpg", "rb") as f:
    # Чтение содержимого файла
    image_data = f.read()
    
    # Подготовка запроса на добавление данных
    insert_query = "INSERT INTO images (data) VALUES (%s)"
    
    # Выполнение запроса на добавление данных
    cur.execute(insert_query, (psycopg2.Binary(image_data),))
    
    # Фиксация изменений в базе данных
    conn.commit()

# Закрытие соединения с базой данных
cur.close()
conn.close()

