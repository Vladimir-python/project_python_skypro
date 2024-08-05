# Проект по работе с банковскими операциями клиентов

## Описание: 
В проекте реализуем функции сортировки, маскировки, преобразований банковских данных клиентов

```
2. устанавливайте зависимости из 
```
pyproject.toml
```

## Использование:
В пакете src реализованы модули для работы нашего приложения, а именно: 
1. find_directory ищет директорию и возвращает кол-во папок и файлов в директории
2. generators итерирует банковские операции по параметрам, также генерирует номер банковских карт
3. masks маскирует номера карт и счетов
4. processing возвращает и сортирует списки словарей по параметрам
5. the_contents_of_the_file читает исходный файл и преобразует его
    в список с правильно оформленными именами, без символов и пробелов
6. widget маскирует карты\счета, преобразует дату в определнный формат, и тд)))
7. добавлен модуль decorators для декорирования функций
8. Реализована функция в модуле external_api Функция принимает транзакцию вида dict и возвращает сумму транзакции,
    в случае валюты EUR или USD конвертирует сумму в RUB по актуальному курсу
9. реализована функция в модуле utils.py Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict], также читает форматы csv и xlsx и json
10. В проекте в пакете src добавлены логи, для логгирования работы приложения

## Тестирование:
Функционал проекта тестируется в пакете tests




