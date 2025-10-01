from Agencia import Agencia, AgenciaVirtual, AgenciaComum, Agencia_premium
from banco import ContaCorrente, CartaoCredito

conta_pessoa = ContaCorrente("Maria", "111.111.111-2", "3333-2", "5555-8")
cartao_pessoa = CartaoCredito("maria", conta_pessoa)

#print(cartao_pessoa. __dict__)

cartao_pessoa.senha = "1239"
#print(cartao_pessoa.senha)

agencia1 = Agencia(1234, 119887877666, 56827938197232)

agencia1.verificar_caixa()
agencia1.emprestar_dinhero(5000000, 657397290829, 0.1)

agencia1.adicionar_cliente("Mariano", 12345395824, 870500)
agencia1.adicionar_cliente("Julio", 12345395824, 8500)
# print(agencia1.clientes)

conta_teste = ContaCorrente("Teste", 16579836728, agencia1, 12352)
conta_teste.consultar_saldo()
agencia1.verificar_caixa()
conta_teste.pedir_emprestimos(5000)
print(agencia1.emprestimos)
conta_teste.consultar_saldo()
agencia1.verificar_caixa()