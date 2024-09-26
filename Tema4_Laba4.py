#Tema4_Laba4

def main (a, *args):
    one = a
    two = sum(args)
    three = (len(args))

    print(f'one = {one} \ntwo = {two} \nthree = {three}')
    print('sum = ', one + two + three)

if __name__ == '__main__':
    main(12, 0, 1, 2, 3, 4)
