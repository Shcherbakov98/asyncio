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

<h4 id="basis"><a href="https://github.com/Shcherbakov98/async_book/blob/dev/chapter_1">2) Основы asyncio:</a></h4>
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



