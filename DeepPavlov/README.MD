## Тестовое задание от DeepPavlov
1. [Теоретические вопросы.](https://github.com/OshchepkovSA/pet_project/tree/main/DeepPavlov/Task1)
2. [Практическия реализация NLP.](https://github.com/OshchepkovSA/pet_project/tree/main/DeepPavlov/Task2)
3. [Практическая реализация Python.](https://github.com/OshchepkovSA/pet_project/tree/main/DeepPavlov/FastAPI)


## Теоретические вопросы

Ответы на теоретические вопросы необходимо поместить в файл `Answers1`.


1. You roll a biased coin  with p(head)=0.65 seven times. What is the probability of getting more than two heads?


2. Suppose you trained a classifier using a MLP with one output neuron. If the values of the output neuron activation is larger than a threshold $\theta,$ the instance will be classified as positive.
The result on the training set using $\theta=0.5$ is summarized in the table below.

![alt text](https://i.ibb.co/Vxj7WWG/precision-table.png)

Calculate precision and recall for the MLP classifier. What happens as you vary $\theta?$

3. ### Derivative of the vector with respect to the vector:
$$
y = x x^T x , x \in \mathbb{R}^{N}
$$

Derive
$$
\frac{dy}{dx} =
$$


## Практическия реализация NLP

Выполнить тетрадку `Практическия_реализация_NLP.ipynb`

## Практическая реализация Python

Напишите веб-сервер на FastAPI (предпочтительно) / Flask имеющий следующие эндпоинты:

* `/model` - получает через POST-запрос данные вида `{"method": "x", "text": "y"}`, где `x` принимает значения `“upper”` - перевести `у` в верхний регистр, `“lower”` - перевести `у` в нижний регистр и `“swapcase”` - перевести в `y` символы верхнего регистра в нижний, а нижнего - в верхний. `y` - строка произвольной длины. Эндпоинт возвращает строку у преобразованную согласно методу `x`.
* `/stat` - в ответ на GET-запрос возвращает целое число - число запросов пришедших на `/model` с момента запуска сервера
Напишите докерфайл для сборки образа с написанным веб-сервером. При запуске контейнера веб-сервер должен запускаться на 5000 порту.
Решение будет проверяться с помощью следующих команд:

`cd <директория с вашим решением>`
`docker build -t test_task .`
`docker run -p 5000:5000 -d test_task`
`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "upper", "text": "sTrInG"}'`
`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "lower", "text": "sTrInG"}'`
`curl -X 'POST' 'http://0.0.0.0:5000/model' -H 'Content-Type: application/json' -d '{"method": "swapcase", "text": "sTrInG"}'`
`curl -X 'GET' 'http://0.0.0.0:5000/stat'`
