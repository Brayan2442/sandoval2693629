"""class pila:
    def __init__(self): # se vuelve privado encapsulacion 
        self.__pila_list=[]

pila_objet=pila()
print(len(pila_objet.__pila_list))"""

"""class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())"""

class Pila:
    def __init__(self):
        self.__pila_list = []

    def push(self, val):
        self.__pila_list.append(val)

    def pop(self):
        val = self.__pila_list[-1]
        del self.__pila_list[-1]
        return val


little_pila = Pila()
another_pila = Pila()
funny_pila = Pila()

little_pila.push(1)
another_pila.push(little_pila.pop() + 1)
funny_pila.push(another_pila.pop() - 2)

print(funny_pila.pop())


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

