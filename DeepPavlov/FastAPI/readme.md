### **Task #3**

Напишите веб-сервер на FastAPI (предпочтительно) / Flask имеющий следующие эндпоинты:

`/model `- получает через POST-запрос данные вида {"method": "x", "text": "y"}, где x принимает значения “upper” - перевести у в верхний регистр, “lower” - перевести у в нижний регистр и “swapcase” - перевести в y символы верхнего регистра в нижний, а нижнего - в верхний. y - строка произвольной длины. Эндпоинт возвращает строку у преобразованную согласно методу x.

`/stat` - в ответ на GET-запрос возвращает целое число - число запросов пришедших на /model с момента запуска сервера Напишите докерфайл для сборки образа с написанным веб-сервером. При запуске контейнера веб-сервер должен запускаться на 5000 порту.

**Решение будет проверяться с помощью следующих команд:**

`cd <директория с вашим решением> `

`docker build -t test_task . `

`docker run -p 5000:5000 -d test_task`

`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "upper", "text": "sTrInG"}'` 

`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "lower", "text": "sTrInG"}'` 

`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "swapcase", "text": "sTrInG"}'` 

`curl -X 'GET' 'http://0.0.0.0:5000/stat'`