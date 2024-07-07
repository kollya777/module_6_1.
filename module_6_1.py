# Вот почему они определены:
# 
# self.alive = True: Этот атрибут указывает на текущее состояние животного. При создании нового экземпляра Animal (и его подклассов) атрибут alive устанавливается в True, что означает, что животное живо.
# 
# self.fed = False: Этот атрибут используется для отслеживания того, было ли животное уже когда-либо покормлено. При создании экземпляра Animal (и его подклассов) атрибут fed устанавливается в False, что означает, что животное еще не было покормлено.
# 
# Эти атрибуты представляют состояние каждого животного, которое можно изменять в процессе его жизни, например, при выполнении методов, таких как eat в классе Animal.

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:

            print(f"{self.name} съел {food.name}")
            self.fed = True

        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)




