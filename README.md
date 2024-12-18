<h1 align="center">  Asyncio и конкурентное программирование на Python </h1>
<nav class="aa">
  <h2>Оглавление:</h2>
  <ol>
    <li><a href="#chapter_1">Знакомство с asyncio</a>
    <li><a href="#chapter_2">Основы asyncio</a>
    <li><a href="#chapter_3">Первое приложение asyncio</a>
    <li><a href="#chapter_4">Конкурентные веб-запросы</a>
    <li><a href="#chapter_5">Неблокирующие драйверы баз данных</a>
    <li><a href="#chapter_6">Счетные задачи</a>
    <li><a href="#chapter_7">Решение проблем блокирования с помощью потоков</a>
    <li><a href="#chapter_8">Потоки данных</a>
    <li><a href="#chapter_9">Веб-приложения</a>
    <li><a href="#chapter_10">Микросервисы</a>
    <li><a href="#chapter_11">Синхронизация</a>
    <li><a href="#chapter_12">Асинхронные очереди</a>
    <li><a href="#chapter_13">Управление подпроцессами</a>
    <li><a href="#chapter_14">Продвинутое использование asyncio</a>
  </ol>
</nav>

<h2>Листинги по главам:</h2>
<h4 id="chapter_1"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1">1) Знакомство с asyncio:</a></h4>
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

<h4 id="chapter_2"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_2">2) Основы asyncio:</a></h4>
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
<h4 id="chapter_3"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_3">3) Первое приложение asyncio:</a></h4>
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
<h4 id="chapter_4"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_4">4) Конкурентные веб-запросы:</a></h4>
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
<h4 id="chapter_5"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_5">5) Неблокирующие драйверы баз данных:</a></h4>
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
<h4 id="chapter_6"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6">6) Счетные задачи:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_01.py">Два параллельных процесса</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_02.py">Создание пула процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_03.py">Асинхронное получение результатов от пула процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_04.py">Исполнители пула процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_05.py">Исполнители пула процессов в сочетании с asyncio</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_06.py">Однопоточная модель MapReduce</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_07.py">Подсчет частот слов, начинающихся буквой 'a'</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_08.py">Распараллеливание с помощью MapReduce и пула процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_09.py">Распараллеливание операции reduce</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_10.py">Разделяемые значения и массивы</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_11.py">Параллельное инкрементирование разделяемого счетчика</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_12.py">Захват и освобождение блокировки</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_13.py">Инициализация пулла процессов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_14.py">Наблюдение за ходом отображения</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_6/listing_6_15.py">Цикл событий в каждом процессе</a></li>
</ol>
<h4 id="chapter_7"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7">7) Решения проблем блокирования с помощью потоков:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_01.py">Многопоточный эхо-сервер</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_02.py">Создание подкласса Thread для чистой остановки</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_03.py">Базовое использование requests</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_04.py">Выполнение запросов с помощью пула потоков</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_05.py">Использование исполнителя пула потоков совместно с asyncio</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_06.py">Использование исполнителя по умолчанию</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_07.py">Использование сопрограммы to_thread</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_08.py">Печать информации о состоянии отправки запросов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_09.py">Блокировки и рекурсия</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_10.py">Класс потокобезопасного списка</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_11.py">Взаимоблокировка</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_12.py">Приложение 'hello, world' на Tkinter</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_13.py">Класс нагрузочного тестирования</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_14.py">Tkinter GUI</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_15.py">Приложение для нагрузочного тестирования</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_16.py">Хеширование паролей с помощью алгоритма scrypt</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_17.py">Хеширование с применением многопоточности и asyncio</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_18.py">Вычисление средних в большой матрице с помощью NumPy</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_7/listing_7_19.py">Многопоточность с NumPy</a></li>
</ol>
<h4 id="chapter_8"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8">8) Потоки данных:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_01.py">Выполнение HTTP запроса с помощью транспортного механизма и протокола</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_02.py">Использование протокола</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_03.py">Отправка HTTP запроса с помощью потоковых писателей и читателей</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_04.py">Попытка выполнения задач в фоновом режиме</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_05.py">Асинхронный читатель стандартного ввода</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_06.py">Использование потоковых читателей для ввода данных</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_07.py">Вспомогательные функции для вывода управляющих последовательностей</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_08.py">Чтение из стандартного ввода по одному символу</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_09.py">Хранилище сообщений</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_10.py">Приложение для асинхронной задержки</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_11.py">Асинхронный командный SQL-клиент</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_12.py">Создание эхо-сервера с помощью серверных объектов</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_13.py">Чат сервер</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_8/listing_8_14.py">Клиент чат-сервера</a></li>
</ol>
<h4 id="chapter_9"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9">9) Потоки данных:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_01.py">Оконечная точка для возврата текущего времени</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_02.py">Подключение к базе данных о товарах</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_03.py">Получение конкретного товара</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_04.py">Оконечная точка для создания товара</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_05.py">Приложение Flask для выборки торговых марок</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_06.py">WSGI-приложение</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_07.py">Простое ASGI-приложение</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_08.py">Оконечная точка brands в приложении Starlette</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_09.py">Оконечная точка типа WebSocket в Starlette</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_10.py">Использование оконечной точки для типа WebSocket</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_11.py">Асинхронное представление Django</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_12.py">Представление requests</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_13.py">Файл async_api/url.py</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_14.py">Представление sync_to_async_view</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_9/listing_9_15.py">Вызов асинхронного кода из синхронного представления</a></li>
</ol>
<h4 id="chapter_10"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10">10) Микросервисы:</a></h4>
<ol>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_01.py">Сервис наличия на складе</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_02.py">Таблица корзины user_cart</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_03.py">Таблица избранных товаров пользователя</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_04.py">Создание, уничтожение пула подключений к базе данных</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_05.py">Сервис избранного</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_06.py">Сервис корзины</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_07.py">Сервис товаров</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_08.py">Сервис backend_for_frontend для товаров</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_09.py">Сопрограмма retry</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_10.py">Тестирование сопрограммы retry</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_11.py">Простой прерыватель</a></li>
<li><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_10/listing_10_12.py">Прерыватель в действии</a></li>
</ol>