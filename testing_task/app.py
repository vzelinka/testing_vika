class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length  # тут ми вже виправляємо попередню помилку

@property
def get_angles(self):
    if self.type in ["квадрат", "прямокутник"]:
        return 4
    if self.type == "трикутник":
        return 3
