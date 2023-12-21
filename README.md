# 2023 CS Python

## Начальная настройка

Установите пакеты:
```bash
pip install hatch, pytest
```

Проверьте что у вас все запускается:
```bash
hatch env create
hatch shell
```

## Тестирование задач

Для тестирования задач, достаточно воспользоваться командами:

Для тестирования **1. Calculator**:
```bash
hatch run test1
```

Для тестирования **2. Group**:
```bash
hatch run test2
```

## Как сделать коммит с помощью терминала

1. удостовериться что код не содержит стилистических ошибок:
    ```bash
    hatch run lint:fmt
    ```
2. Удостовериться что код проходит все тесты:
    ```bash
    hatch run test
    ```
3. Зафиксировать изменения в файлах:
    ```bash
    git add ./src/01_Calculator/calculator.py
    ```
4. Сохранить код в локальном гите с комментарием:
    ```bash
    git commit -m "Add calculator task"
    ```
5. Отправить код в удаленный репозиторий:
    ```bash
    git push
    ```
