class PrimeiraClasse:
    pass

objeto1 = PrimeiraClasse()
objeto2 = PrimeiraClasse()
type(objeto1) # Descobrindo o tipo do objeto


class SegundaClasse:
    def metodo1(self):
        print('metodo1')
    def metodo2(self, nome):
        print(nome)

objeto3 = SegundaClasse()
objeto3.metodo2('Oi mundo')
objeto3.metodo1()
objeto3.metodo2([1,2,3,4])
objeto3.metodo2((1,2,3,4))
objeto3.nome = 'Orlando Saraiva'
objeto3.nome 
objeto4 = SegundaClasse()