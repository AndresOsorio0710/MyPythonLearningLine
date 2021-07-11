from os import system


class Lamp():
    is_on = False
    ESTATUS = [
        '''
        .
    .   |   .
     \  .  /
       .-.
   ---(^*^)---
       \*/ 
       |=|
     |¯   ¯|
      ¯¯¯¯¯ ''',
        '''



       .-.
      (^ ^)
       \ / 
       |=|
     |¯   ¯|
      ¯¯¯¯¯ '''
    ]

    def __init__(self, is_on):
        self.is_on = is_on

    def show_lamp(self):
        if self.is_on:
            print(self.ESTATUS[0])
        else:
            print(self.ESTATUS[1])

    def on(self):
        self.is_on = True
        # self.show_lamp()

    def off(self):
        self.is_on = False
        # self.show_lamp()


def main():
    lamp = Lamp(False)
    menu = '''
    Menu:
    0 > Lamp OFF
    1 > Lamp ON
    x > Excit'''
    while True:
        system('clear')
        lamp.show_lamp()
        print(menu)
        option = input("\n\t>>> ")
        if option == '0':
            lamp.off()
        elif option == '1':
            lamp.on()
        else:
            break


if __name__ == "__main__":
    main()
