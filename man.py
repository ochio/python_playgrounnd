class Man:
    def __init__(self, name):
        self.name = name
        print('Initialize')
    
    def hello(self):
        print('Hello' + self.name + '!')

    def goodbye(self):
      print('Goodbye' + self.name)
        

m = Man('Dav')
m.hello()
m.goodbye()