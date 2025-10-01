class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.quantidade})"

class Carrinho:
    def __init__(self, estoque):
        self.estoque = estoque
        self.itens = []

    def listarProdutos(self):
        for i, produto in enumerate(self.estoque, 1):
            print(f"{i} - {produto}")

    def adicionar(self):
        self.listarProdutos()
        escolha = int(input("Escolha um produto para adicionar: ")) - 1
        if 0 <= escolha < len(self.estoque):
            produto = self.estoque[escolha]
            qtd = int(input(f"Quantos '{produto.nome}'? "))
            if qtd <= produto.quantidade:
                produto.quantidade -= qtd
                self.itens.append((produto, qtd))
                print(f"{qtd}x {produto.nome} adicionado!")
            else:
                print("Quantidade indisponível!")
        else:
            print("Produto inválido!")

    def remover(self):
        if not self.itens:
            print("Carrinho vazio!")
            return
        for i, (produto, qtd) in enumerate(self.itens, 1):
            print(f"{i} - {produto.nome} (x{qtd})")
        escolha = int(input("Escolha um item para remover: ")) - 1
        if 0 <= escolha < len(self.itens):
            produto, qtd = self.itens.pop(escolha)
            produto.quantidade += qtd
            print(f"{qtd}x {produto.nome} removido!")
        else:
            print("Produto inválido!")

    def verificarCarrinho(self):
        if not self.itens:
            print("Carrinho vazio!")
        else:
            for produto, qtd in self.itens:
                print(f"{produto.nome} - {qtd}x - R${produto.preco:.2f}")

    def finalizarCompra(self):
        if len(self.itens) < 3:
            print("Adicione pelo menos 3 itens diferentes!")
            return
        total = sum(produto.preco * qtd for produto, qtd in self.itens)
        print("Compra finalizada:")
        for produto, qtd in self.itens:
            print(f"{qtd}x {produto.nome} - R${produto.preco * qtd:.2f}")
        print(f"TOTAL: R${total:.2f}")
        self.itens.clear()

def menu():
    estoque = [
        Produto("Arroz - 5k", 25.00, 100),
        Produto("Feijão - 1k", 8.47, 80),
        Produto("Macarrão - 1k", 5.99, 50),
        Produto("Miojo - 200g", 2.25, 600),
        Produto("Leite - 1l", 4.99, 42),
        Produto("Cerveja - 300ml", 2.39, 200)
    ]
    carrinho = Carrinho(estoque)

    print("\nBem-vindo à loja!")
    while True:
        print("\n1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra")
        print("5 - Ver produtos")
        print("6 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            carrinho.adicionar()
        elif opcao == 2:
            carrinho.remover()
        elif opcao == 3:
            carrinho.verificarCarrinho()
        elif opcao == 4:
            carrinho.finalizarCompra()
        elif opcao == 5:
            carrinho.listarProdutos()
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()