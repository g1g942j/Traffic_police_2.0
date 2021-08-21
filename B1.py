class Cat:
    def __init__(self):
        self.name = 'Снежок'
        self.color = 'Светло-буро-малиновый'
        self.weight = 7
    def meow(self):
        print('МЯУ?')
    def getName(self):
        return self.name
    def __set_name__(self , ARG):
        self.name = ARG
    def getColor(self):
        return self.color
    def __set_color__(self ,colour):
        self.color = colour
    def getweight(self):
        return self.weight
    def __set_weight__(self , wei):
        self.weight = wei
cat = Cat()
print(cat.getName())
print(cat.getColor())
print(cat.getweight())
cat.__set_name__('Новая кличка')
cat.__set_color__('Светлый окрас')
cat.__set_weight__(8)
cat.meow()
print(cat.name)
print(cat.color)
print(cat.weight)