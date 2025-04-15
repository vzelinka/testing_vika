class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Вікторія"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Вікторія")
        assert hobby.strip() != "", "Хобі не може бути порожнім!"
        self.name = name
        self.hobby = hobby

# Некоректний приклад (помилки)
# a = Name("Бодько", "фотографувати")  # ім’я не з дозволених
# b = Name("Богдан", "")         # порожнє хобі

# Коректний приклад
c = Name("Вікторія", "фотографувати")
print(f"Ім'я: {c.name}, хобі: {c.hobby}")
