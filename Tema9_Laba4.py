class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'
    tail_length = 'long'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
    tail_length = 'short'

dog = Dog()
print(f'Dog is {dog.className}, but they say {dog.sounds}. Tail length: {dog.tail_length}')

cat = Cat()
print(f'Cat is {cat.className}, but they say {cat.sounds}. Tail length: {cat.tail_length}')
