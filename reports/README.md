# Звіт до роботи

## Мета

Навчитися створювати тести, обробляти помилки, перевіряти правильність виконання коду за допомогою бібліотек `unittest`, `pytest`, а також створювати класи з валідацією.

---

## Крок 1: Створення класу `Figure`

У `figure_test.py` був створений клас `Figure`, що обробляє тип фігури та її довжину. Реалізовано валідацію типу та довжини.

```python
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length
```



---

## Крок 2: Тестування класу `Name`

Створено клас `Name` з фільтрацією імен та хобі. При некоректних даних спрацьовує `ValueError`.

```python
class Name:
    def __init__(self, name, hobby) -> None:
        assert name in ["Богдан", "Анонім", "Соломія"], "Дозволені імена: Богдан, Анонім, Соломія"
        assert hobby != "", "Хобі не може бути порожнім"
        self.name = name
        self.hobby = hobby
```

![Помилка ValueError](https://github.com/vzelinka/testing_vika/blob/main/image/nametest1(ValueError).png?raw=true)


![Коректне виконання](https://github.com/vzelinka/testing_vika/blob/main/image/nametest1(%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9).png?raw=true)


---

## Крок 3: `pytest`

Написано тест з використанням `pytest` для перевірки кількості кутів:

```python
def test_get_angles():
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles() == 3, f"У {fig} має бути 3 кути!"
```

![pytest passed](https://github.com/vzelinka/testing_vika/blob/main/image/testapp(passed).png?raw=true)


---

## Крок 4: `unittest`

Створено `unittest` тести для класу `Figure`:

- вірність типу;
- вірність довжини;
- некоректні дані (викликають `AssertionError`).

![unittest успішно](https://github.com/vzelinka/testing_vika/blob/main/image/testfigure.png?raw=true)


---

## Висновки

- створювати класи з перевірками вхідних параметрів;

- генерувати помилки при некоректних значеннях;

- використовувати pytest і unittest для тестування коду;

- документувати результати тестів за допомогою скріншотів;

- структурувати проєкт і звіт відповідно до GitHub-стандартів.
