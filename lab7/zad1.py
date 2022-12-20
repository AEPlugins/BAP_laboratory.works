class Cat():
 def __init__(self, okras, areal, weight, est, name, uwu):
  self.name = name
  self.uwu = uwu
  self.est = est
  self.okras = okras
  self.areal = areal
  self.weight = weight
 def describe_cat(self):
  print("Окрас "+self.okras)
  print("Ареал " + self.areal)
  print("Вес " + self.weight)
 def est_cat(self):
  print(self.name + " ест " + self.est)
 def uwu_cat(self):
  print(self.name + " " + self.uwu)

koshka=Cat("Рыжий","Дом","3,5 кг","мясо","Кошка","мяукает")
koshka.describe_cat()
koshka.est_cat()
koshka.uwu_cat()

class Tiger(Cat):
 def est_Tiger(self):
  super().est_cat()
 def uwu_cat(self):
  print(self.name + " " + self.uwu)

Tiger=Cat("Полосатый","Есть","57 кг","оленя","Тигр","рычит")
Tiger.est_cat()
Tiger.uwu_cat()