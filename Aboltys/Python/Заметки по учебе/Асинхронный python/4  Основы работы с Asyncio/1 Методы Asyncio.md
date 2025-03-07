В предыдущих уроках мы познакомились с некоторыми методами библиотеки `asyncio`. В данном модуле рассмотрим их более подробно, а также рассмотрим новые методы `asyncio`. 

**Asyncio** предоставляет функциональность для управления событийным циклом (event loop). Т.к. центральной концепцией в asyncio является цикл событий, все методы, реализованные в модуле `asyncio`, так или иначе влияют на него.

Например, метод `asyncio.run(coro)` запустит указанную корутину в цикле событий, а метод `asyncio.sleep()` укажет циклу событий на то, что конкретная корутина будет заблокирована на указанное время, в течение которого могут выполнятся другие задачи. Таким же образом перечисленные ниже методы будут взаимодействовать с циклом событий.

**Напомню**: цикл событий – это такая конструкция, которая не только ожидает и отправляет события или задачи на выполнение, но и следит за ходом выполнения каждой задачи и их статуcом. Каждая корутина, запущенная в цикле событий, общается "сообщениями" под капотом, передавая информацию о своём статусе для эффективного управления ею. Когда ваша программа включает в себя множество асинхронных операций, цикл событий может управлять их выполнением, переключаясь между задачами в оптимальном порядке.

Вот короткое описание основных функций и методов, которые предоставляет этот модуль, детальное описание которых с примерами кода будет в следующих уроках:   
 

**Общие методы `asyncio`:**

-  `asyncio.**run**()` — функция создаёт цикл событий и запускает указанную корутину в нём. После завершения выполнения корутины автоматически закрывает цикл событий. Эта функция является основным методом для запуска и управления `asyncio` приложениями.
- `asyncio.**sleep**()` — функция приостанавливает выполнение текущей корутины на указанное количество секунд.  
     
    

**Методы для создания, запуска и ожидания задач:** 

- `asyncio.**create_task**()`— функция оборачивает корутину в объект `Task`, т.е. она будет запланирована для выполнения в цикле событий.
    
- `asyncio.**ensure_future**()` — функция обеспечивает обертывание корутин и других awaitable объектов в объект `Task`, который можно использовать для отслеживания состояния асинхронной операции.
    
- `asyncio.**gather**()`— функция запускает awaitable объекты, переданные в функцию и собирает результаты их работы.
    
- `asyncio.**wait_for**()` — функция ожидает завершения одного awaitable объекта, позволяет устанавливать `timeout` на время ожидания и, если выполнение не завершено в течение `timeout` секунд, вызывается `TimeoutError`.
    
- `asyncio.**wait**()` — функция запускает задачи (`Task` или `Future`), переданные в функцию, и блокирует текущую корутину до выполнения переданного в функцию условия, возвращает кортеж из двух множеств завершенных и не завершенных `Task`/`Future` (`done`, `pending`). Это позволяет вам узнать, какие задачи были выполнены и какие еще ожидают выполнения.
    
- `asyncio.**shield**()` — функция защищает awaitable объект от отмены.  
     
    

**Методы для работы с циклом событий:** 

- `asyncio.**new_event_loop**()` — функция создает и возвращает новый объект цикла событий.
    
- `asyncio.**set_event_loop**(loop)` — функция устанавливает `loop` в качестве текущего цикла событий для текущего потока ОС, если в нем нет уже запущенного цикла событий.
    
- `loop.**run_until_complete**(**future**)` — метод позволяет запустить выполнение корутины или объекта `Future` внутри цикла событий. Актуален, когда требуется явное управление запуском и завершением асинхронных операций в определённых точках синхронного потока выполнения.
- `asyncio.**get_event_loop**()` — функция возвращает текущий цикл событий, создает новый цикл событий, если текущего цикла нет.
    
- `asyncio.**get_running**_**loop**()` — функция возвращает текущий запущенный цикл событий в текущем потоке ОС. Вызывает исключение `RuntimeError`, если нет запущенного цикла событий.  
     
    

**Методы для работы асинхронных приложений в нескольких потоках:**

- `asyncio.**run_coroutine_threadsafe**()` — используется для отправки корутины в заданный цикл событий (event loop) таким образом, чтобы это было безопасно в условиях многопоточности.
- `asyncio.**to_thread**()`— используется для запуска корутины в отдельном потоке. 

_* В данном уроке представлена только часть функций библиотеки `asyncio`, наиболее актуальных для работы с модулем и для понимания принципов его работы._  

Прежде чем перейти к детальному изучению функций `asyncio` и особенностей их работы, предлагаю ответить на несколько вопросов по функциям, которые уже встречались в курсе.