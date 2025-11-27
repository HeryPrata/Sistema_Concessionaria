#CADASTRO DO CLIENTE

print("Iniciando cadastro na concessioária.")

cliente = {

"nome": input("Digite o seu nome: "),
"telefone": input("Digite o seu telefone: "),
"saldo": float(input("Digite o seu saldo inicial: ")),

}

#Dicionario com os modelos e o valor fipe
tabela_precos = {
"F40": 2000000.0,
"Panamera": 1500000.0,
"X6": 1000000.0,
"Sennna": 3000000.0,
}

#lista de tuplas
carros_aluguel = [
("Ferrari", "F40"),
("Mclaren", "Senna"),
]

carros_vendas = [
("F40", "Ferrari"),
("Panamera","Porche"),
("X6","Bmw"),
("Senna","Mclaren")

]

#Copia e cola: veículo, Automóveis, Você, Disponíveis.
def vender_carro():
    print("--- VENDA DE VEÍCULOS ---")
    
    marca = input("Digite a marca que você deseja: ")
    modelo = input("Digite o modelo da marca que você escolheu: ")
    

    if modelo not in tabela_precos:
          print("A marca não esta presente em nossa lista")
          return
  
    #escolha = modelo
    valor_referencia = tabela_precos[modelo]
    proposta = valor_referencia*0.88 #paga 12 a menos do valor de referência
    
    print(f"Valor referencial: {valor_referencia:.2f}")
    print(f"Prosposta da concessionaria: {proposta:.2f}")


    confirmacao = input("Você aceita a prosposta? (s) ou (n): ")

    if confirmacao == "s":
        cliente ["saldo"] += proposta
        print("Venda realizada com sucesso!")

        carros_vendas.append((modelo, marca))
    elif cliente["saldo"] < proposta:
        print("Valor em saldo insuficiente. Tente buscar por outro modelo.")
        return
    else:
        print("Venda cancelada. Retornando para o menu.")

def alugar_carro():
    print("--- ALUGUE DE VEÍCULOS ---")
    if not carros_aluguel:
        print("Não a veículo disponivel para aluguel.")
        return
    
    print("\n--- Veículos Disponíveis ---")
    print("\ncarros disponíveis:")
    for i, carro in enumerate(carros_aluguel):
     print(f"{i + 1} - {carro[0]} ({carro[1]})")
    
    escolha = int(input("Escolha o numero correspondente ao carrro do seu interrese: ")) -1 
    
    if escolha < 0 or escolha >= len(carros_aluguel):
        print("Opção invalida.")
    
    dias = int(input("Quantos dias você gostaria de alugar o carro? "))
    
    valor_final = dias*5

    print(f"O valor total do aluguel é: R$ {valor_final:.2f}")

    print("Verificando seu saldo...")

    if cliente["saldo"] < valor_final:
        print("Valor insuficiente. Tente buscar outro modelo ou diminuir a quantidade dias.")
        return
    
    confimarcao = input("Saldo suficientel, gostaria de alugar o Automóvel: (s) ou (n): ")
    if confimarcao == "s":
        cliente["saldo"] -= valor_final
        print(f"Transação concluida. Você escolheu: {carro[escolha]}")
        carro = carros_aluguel.pop(escolha)#O pop é a ação de remover o item com a ação de obter o item em uma única linha.
    else:
        print("Transação cancelada.")
        return
    

def comprar_carro():
    print("--- COMPRAR DE VEÍCULOS ---")
    print("Automóveis disponiveis.")

    for i, carro in enumerate(carros_vendas):
     print(f"{i + 1} - {carro[0]} ({carro[1]})")
    
    escolha = int(input("Digite o numero do veículo de seu interrese: ")) - 1

    if escolha < 0 or escolha >= len(carros_vendas):
        print("Opção inválida.")
        return

    modelo = carros_vendas[escolha][0]

    if modelo not in tabela_precos:
        print("Preço não encontrado para este modelo.")
        return

    preco_base = tabela_precos[modelo]
    valor_proposta = preco_base * 1.25 

    aceita_compra = input(f"A valor do veículo é: {valor_proposta}. Gostaria de finalizar a compra? (s)/(n): ")

    if aceita_compra == "s":
        print("Verificando o seu saldo...")
        
        if cliente["saldo"] < valor_proposta:
            print("Saldo insuficiente.")
            return
        else:
         print("Saldo Suficiente, compra realizada com sucesso.")
         return
    else:
        print("Compra canceladada.")
        return
    
#Menu Principal
def menu():
    print("--- SEJA BEM VINDO, A NOSSA CONCESSIONARIA. ---")
    print("1 - Vender Carro")
    print("2 - Compra Carro")
    print("3 - Alugar Carro")
    print("4 - Ver saldo")
    print("5 - sair")

while True:
    menu()

    opcao = input("Escolha um opção: ")

    match opcao:
        case "1":
            vender_carro()
        case "2":
            comprar_carro()
        case "3":
            alugar_carro()
        case "4":
            print(f"O saldo disponivel: R${cliente['saldo']:.2f}")
        case "5":
            print("Encerrando sistema.")
            break
        case _:
            print("Opção invalida. Tente novamente.")
