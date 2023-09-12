Algoritmo "semnome"

Var
numeroA, numeroB, resultado:real
opcao:inteiro


Inicio
escreval("Digite um numero: ")
escreval("********************")
leia(numeroA)
escreval("Digite outro numero: ")
escreval("********************")
leia(numeroB)

escreval("escolha uma Opção: ")
escreval("=====================")
escreval("[1]Soma")
escreval("[2]Subtracao")
escreval("[3]Divisao")
escreval("[4]Multiplicacao")
escreval("[5]Resto da Divisao")
leia(opcao)

escolha opcao
        caso 1
             resultado <- numeroA + numeroB
        caso 2
             resultado <- numeroA - numeroB
        caso 3
             resultado <- numeroA / numeroB
        caso 4
             resultado <- numeroA * numeroB
        caso 5
             resultado <- numeroA % numeroB
        outrocaso
                 escreval("opção Invalida...")
        fimescolha
        escreval("________________")
        escreval(resultado)


Fimalgoritmo