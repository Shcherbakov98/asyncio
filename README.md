<h1 align="center">  Asyncio и конкурентное программирование на Python </h1>
<nav class="aa">
  <h2>Оглавление:</h2>
  <ol>
    <li><a href="#welcome">Знакомство с asyncio</a>
    <li><a href="#basis">Основы asyncio</a>
    <li><a href="#bear">Первое приложение asyncio</a>
    <li><a href="#bear">Конкурентные веб-запросы</a>
    <li><a href="#bear">Неблокирующие драйверы баз данных</a>
    <li><a href="#bear">Счетные задачи</a>
    <li><a href="#bear">Решение проблем блокирования с помощью потоков</a>
    <li><a href="#bear">Потоки данных</a>
    <li><a href="#bear">Веб-приложения</a>
    <li><a href="#bear">Микросервисы</a>
    <li><a href="#bear">Синхронизация</a>
    <li><a href="#bear">Асинхронные очереди</a>
    <li><a href="#bear">Управление подпроцессами</a>
    <li><a href="#bear">Продвинутое использование asyncio</a>
  </ol>
</nav>

<h2>Листинги по главам:</h2>
<h4 id="welcome"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1">1) Знакомство с asyncio:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_1.py">Операции, ограниченные производительностью ввода-вывода и быстродействием процессора</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_2.py">Процессы и потоки в простом Python приложении</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_3.py">Создание многопоточного Python приложения</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_4.py">Создание нескольких процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_5.py">Генерирование последовательности Фибоначчи и его хронометраж</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_6.py">Многопоточное вычисление последовательности чисел Фибоначчи</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_7.py">Синхронное чтение кода состояния</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1/listing_1_8.py">Многопоточное чтение кода состояния</a></li>
</ol>

<h4 id="basis"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2">2) Основы asyncio:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_1.py">Использование ключевого слова async</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_2.py">Сравнение сопрограмм с обычными функциями</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_3.py">Выполнение сопрограммы</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_4.py">Использование await для ожидания результата сопрограммы</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_5.py">Первое применение sleep</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_6.py">Повторно используемая сопрограмма delay</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_7.py">Выполнение двух сопрограмм</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_8.py">Создание задачи</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_9.py">Конкурентное выполнение нескольких задач</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_10.py">Выполнение кода, пока другие операции работают в фоне</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_11.py">Снятие задачи</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_12.py">Задание тайм-аута для задачи с помощью wait_for</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_13.py">Защита задачи от снятия (shield)</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_14.py">Основы будущих объектов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_15.py">Ожидание будущего объекта</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_16.py">Декоратор для хронометража сопрограмм</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_17.py">Хронометраж двух конкурентных задач с помощью декоратора</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_18.py">Попытка конкурентного выполнения счетного кода</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_19.py">Счетный код и длительная задача</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_20.py">Неправильное использование блокирующего API как сопрограммы</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_21.py">Создание цикла событий вручную</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_22.py">Получение доступа к циклу событий</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_23.py">Выполнение счетного кода в отладочном режиме</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2/listing_2_24.py">Изменение продолжительности медленного обратного вызова</a></li>
</ol>
<h4 id="basis"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3">3) Первое приложение asyncio:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_1.py">Запуск сервера и прослушивание порта для подключения</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_2.py">Чтение данных из сокета</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_3.py">Подключение нескольких клиентов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_4.py">Создание неблокирующего сокета</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_5.py">Первая попытка создать неблокирующий сокет</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_6.py">Перехват и игнорирование ошибок блокирующего ввода-вывода</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_7.py">Использование селектора для построения неблокирующего сервера</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_8.py">Построение асинхронного эхо-сервера</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_9.py">Добавление обработчика сигнала, снимающего все задачи</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3/listing_3_10.py">Корректная остановка</a></li>
</ol>
<h4 id="basis"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4">4) Конкурентные веб-запросы:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_1.py">Асинхронный контекстный менеджер, ожидающий подключение клиента</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_2.py">Отправка веб-запроса с помощью aiohttp</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_3.py">Задание тайм-аутов в aiohttp</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_4.py">Неправильное использование спискового включения для создания ожидания задач</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_5.py">Использование спискового включения для конкурентного выполнения задач</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_6.py">Конкурентное выполнение запросов с помощью gather</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_7.py">Завершение допускающих ожидания объектов не по порядку</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_8.py">Использование as_completed</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_9.py">Задание тайм-аута для as_completed</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_10.py">Изучение поведения wait по умолчанию</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_11.py">Обработка исключений при использовании wait</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_12.py">Отмена работающих запросов при возникновении исключения</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_13.py">Обработка запросов по мере завершения</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_14.py">Обработка всех результатов по мере поступления</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_15.py">Использование тайм-аутов в wait</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4/listing_4_16.py">Отмена медленного запроса</a></li>
</ol>
<h4 id="basis"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5">5)Неблокирующие драйверы баз данных:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_1.py">Подключение к базе данных Postgres от имени пользователя по умолчанию</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_2.py">Команды создания таблиц в схеме базы данных о товарах</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_3.py">Использование сопрограммы execute для выполнения команд create</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_4.py">Вставка и выборка марок</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_5.py">Вставка случайных марок</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_6.py">Вставка случайных товаров и SKU</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_7.py">Создание пула подключений и конкурентное выполнение запросов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_8.py">Синхронное и конкурентное выполнение запросов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_9.py">Создание транзакции</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_10.py">Обработка ошибки в транзакции</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_11.py">Вложенная транзакция</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_12.py">Ручное управление транзакцией</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_13.py">Синхронный генератор</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_14.py">Простой асинхронный генератор</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_15.py">Потоковая обработка результатов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_16.py">Перемещение по курсору и выборка записей</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5/listing_5_17.py">Получение заданного числа элементов с помощью асинхронного генератора</a></li>
</ol>


