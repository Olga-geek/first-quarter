from abc import ABC,abstractmethod

class Clothes(ABC):
    def __init__(self,title):
        self.title = title

    @abstractmethod
    def textile(self):
        pass

class Coat(Clothes):
    def __init__(self, title, V):
        super().__init__(title)
        self.V = V
    @property
    def textile(self):
        return self.V / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, title, H):
        super().__init__(title)
        self.H = H
    @property
    def textile(self):
        return 2 * self.H + 0.3

coat = Coat("my cout", 5)
print(f'textile for my coat = {coat.textile}')
suit = Suit("my suit", 2)
print(f'textile for my suit = {suit.textile}')
print(f'Total textile for cloth {coat.textile + suit.textile}')