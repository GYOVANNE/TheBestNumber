import math
import time

class GoodNumber:
    def __init__(self):
        super().__init__()

    @classmethod
    def firstCheck(cls,number):
            time.sleep(1)
            count = 0
            for i in range(1,number+1):
                if number % i == 0: count+=1

            if(count==2):
                print(number,'é um número primo!')
                GoodNumber.secondCheck(number)
            else:
                print(number,'não é um número primo :(')
                return 0

    @staticmethod
    def secondCheck(number):
            time.sleep(1)
            x = 1
            reverse = 0
            while( x < number):
                reverse = reverse * 10
                reverse = reverse + ((number % ( x * 10 )) - (number % x)) / x
                x *= 10
            print(number,'invertido é',math.floor(reverse))
            GoodNumber.thirdCheck(reverse, number)

    @staticmethod
    def thirdCheck(cousin, number):
            time.sleep(1)

            count = 0
            cousin = math.floor(cousin)
            position = GoodNumber.convert(cousin)
            for i in range(1, cousin+1):
                if cousin % i == 0:
                    count += 1
            if count == 2:
                position += 1
                print(cousin,'é um número primo!')
                time.sleep(1)
                print(cousin," é o ",position,"º número primo.",sep="")
                GoodNumber.fourthCheck(position, number)
            else:
                print(cousin, "Não é um número primo :(")

    @staticmethod
    def convert(reverse):
            x = 1
            y = count = w = 0
            z = 2
            position = 0
            while(1):
                while( x < z):
                    if(z % x == 0):
                        y = 1
                        break
                    x = x + 1
                x = 2
                if( y == 0):
                    if (count % 10 == 0):
                        count += 1
                    w = z - 2
                    position += 1
                    if( z == reverse):
                        return position
                y = 0
                z += 1
            return 0

    @staticmethod
    def fourthCheck(position,number):
            time.sleep(1)

            reverse = 0
            y = 1
            while( y <= position):
                reverse = reverse * 10
                reverse = reverse + ((position % (y * 10)) - (position % y)) / y
                y *= 10
            print(position," Invertido é ",math.floor(reverse))
            GoodNumber.fifthCheck(number, reverse)
            return 0

    @staticmethod
    def fifthCheck(number, reverse):
            time.sleep(1)

            mult = 1
            vinc = 0
            stop = number
            v1 = [0]*3
            while(stop > 0):
                v1[vinc] = number % 10
                vinc += 1
                v1[vinc] = math.floor(number/10)
                stop = math.floor(stop / 10)
                v1[vinc] = v1[vinc]

            print("O produto dos numeros: ",end="")
            for i in range(vinc,0,-1):
                print(v1[i], end="")
                mult *= v1[i]
                if(i==2):print(' e ',end="")

            print(" =",mult)
            if(mult == reverse):
                time.sleep(1)
                print('**Portanto, ',number,"é um Numero Primo Especial**")
            else:
                time.sleep(1)
                print("O produto dos numeros", number," é diferente de",  math.floor(reverse),":(","\nPortanto o número ",number," não é um primo especial :(\n");
            vinc=0