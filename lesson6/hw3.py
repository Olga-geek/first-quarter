class Worker():
    name = str
    surname = str
    position = str
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"]= wage
        self._income["bonus"] =bonus


class Position(Worker):
    # объясни пжл, почему когда для наследника задаю init родителя и super у меня выходит ошибка(подсвечивается бонус в super)
    # когда мы создаем класс с наследником всегда должны указывать init и super. Ниже закомитила. И в словареб когда ссылаемся на словарь, всегда ставить None?
    # def __init__(self, name, surname, position, wage, bonus):
        # super().__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return (f' полное имя {self.name} {self.surname}')

    def get_total_income(self):
        return sum(self._income.values())

pst = Position('Igor', 'Petrov', 'DV', 100000, 200000)
print(pst.get_full_name(), pst.get_total_income())

