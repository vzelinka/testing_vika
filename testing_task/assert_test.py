number = -1
assert number > 0, "число має бути більшим за нуль!"

a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")
