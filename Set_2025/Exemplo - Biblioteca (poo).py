class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel is True:
            self.disponivel = False
        else:
            print("O livro não está disponível para ser emprestado.")

    def devolver(self):
        self.disponivel = True

    def exibir_info(self):
        print(self.titulo, self.autor, self.ano_publicacao)

livro1 = Livro("Livro 1", "Pedro I ", 2019)
livro2 = Livro("Livro 2", "Pedro II ", 2020)
livro3 = Livro("Livro 3", "Pedro III ", 2021)

livro1.emprestar()
print(livro1.exibir_info())
livro1.emprestar()
print(livro1.exibir_info())
livro1.devolver()