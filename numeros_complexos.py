class n_complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def printar(self):
        if self.imag < 0:
            print(f'{self.real}{self.imag}i')
            print(f'Parte real: {self.real} e parte imaginária: {self.imag}')
        else:
            print(f'{self.real}+{self.imag}i')
            print(f'Parte real: {self.real} e parte imaginária: {self.imag}')

    def soma(self, comp2, comp3):
        num = n_complexo(self.real+comp2.real+comp3.real, self.imag+comp2.imag+comp3.imag)
        print('\n(((Resultado da Soma)))')
        num.printar()

    def subtracao(self, comp2, comp3):
        num = n_complexo(self.real-comp2.real-comp3.real, self.imag-comp2.imag-comp3.imag)
        print('\n(((Resultado da Subtração)))')
        num.printar()

    def multiplicacao(self, comp2, comp3):
        num1 = n_complexo(self.real*comp2.real-self.imag*comp2.imag, self.real*comp2.imag+self.imag*comp2.real)
        print('\n(((Resultado da Multiplicação)))')
        num2 = n_complexo(num1.real*comp3.real-num1.imag*comp3.imag, num1.real*comp3.imag+num1.imag*comp3.real)
        num2.printar()

    def divisao(self, comp2, comp3):
        sr, si, c2r, c2i, c3r, c3i = self.real, self.imag, comp2.real, comp2.imag, comp3.real, comp3.imag
        r = c2r**2 + c2i**2
        num1 = n_complexo((sr*c2r+si*c2i)/r, (si*c2r-sr*c2i)/r)
        print('\n(((Resultado da Divisão)))')
        d = c3r**2 + c3i**2
        num2 = n_complexo((num1.real*c3r+num1.imag*c3i)/d, (num1.imag*c3r-num1.real*c3i)/d)
        num2.printar()
       
n1 = int(input('Digite um número para a 1ª parte do 1º número complexo: '))
n2 = int(input('Digite um número para a 2ª parte do 1º número complexo: '))
n3 = int(input('Digite um número para a 1ª parte do 2º número complexo: '))
n4 = int(input('Digite um número para a 2ª parte do 2º número complexo: '))
n5 = int(input('Digite um número para a 1ª parte do 3º número complexo: '))
n6 = int(input('Digite um número para a 2ª parte do 3º número complexo: '))

z1 = n_complexo(n1, n2)
z2 = n_complexo(n3, n4)
z3 = n_complexo(n5, n6)

z1.soma(z2, z3)
z1.subtracao(z2, z3)
z1.multiplicacao(z2, z3)
z1.divisao(z2, z3)
