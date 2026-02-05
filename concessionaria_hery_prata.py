# ==========================================
# SISTEMA DE CONCESSIONÁRIA 2.0
# ==========================================

print("--- Iniciando Cadastro Na Concessionária ---")

# Cadastro inicial com validação robusta
nome = input("Digite o seu nome: ")

while True:
    try:
        telefone = input("Digite seu numero de telefone (apenas números): ")
        # Validação manual: Se não for dígito, forçamos um erro
        if not telefone.isdigit():
            raise ValueError 
        
        saldo = float(input("Digite o seu saldo inicial: R$ "))
        
        # O dicionário só é criado se as entradas acima forem válidas
        cliente = {
            "nome": nome,
            "telefone": telefone,
            "saldo": saldo,
        }
        break # Sai do loop de cadastro

    except ValueError:
        print("\n[ERRO] Entrada inválida! Certifique-se de:")
        print("- Digitar apenas números no telefone.")
        print("- Usar números (e ponto para centavos) no saldo.")
        print("Vamos tentar novamente...\n")

# Banco de dados do sistema
tabela_precos = {
    "F40": 2000000.0,
    "Panamera": 1500000.0,
    "X6": 1000000.0,
    "Senna": 3000000.0, 
    "Chiron": 4000000.0
}

carros_aluguel = [
    ("Ferrari", "F40"),
    ("Mclaren", "Senna"),
    ("Bugatti", "Chiron")
]

carros_vendas = [
    ("F40", "Ferrari"),
    ("Panamera","Porsche"),
    ("X6","Bmw"),
    ("Senna","Mclaren"),
    ("Chiron","Bugatti")
]

# --- FUNÇÕES DO SISTEMA ---

def vender_carro():
    print("\n--- VENDA DE VEÍCULOS ---")
    marca = input("Digite a marca do seu carro: ")
    modelo = input("Digite o modelo: ")

    if modelo not in tabela_precos:
        print("[AVISO] Este modelo não consta em nossa tabela FIPE.")
        return
  
    valor_referencia = tabela_precos[modelo]
    proposta = valor_referencia * 0.88 
    
    print(f"Valor de mercado: R$ {valor_referencia:,.2f}")
    print(f"Nossa proposta de compra: R$ {proposta:,.2f}")

    confirmacao = input("Aceita a proposta? (s/n): ").lower()

    if confirmacao == 's':
        cliente["saldo"] += proposta
        carros_vendas.append((modelo, marca))
        print("Venda concluída! O valor foi adicionado ao seu saldo.")
    else:
        print("Venda cancelada.")

def alugar_carro():
    print("\n--- ALUGUEL DE VEÍCULOS ---")
    if not carros_aluguel:
        print("Desculpe, não há veículos disponíveis para aluguel.")
        return
    
    for i, carro in enumerate(carros_aluguel):
        print(f"{i + 1} - {carro[0]} ({carro[1]})")
    
    # Blindagem da escolha do veículo
    while True:
        try:
            escolha = int(input("Escolha o número do carro: ")) - 1 
            if 0 <= escolha < len(carros_aluguel):
                break
            print("[ERRO] Esse número não está na lista.")
        except ValueError:
            print("[ERRO] Digite apenas o número correspondente.")
                 
    # Blindagem da quantidade de dias
    while True:
        try:
            dias = int(input("Quantos dias de aluguel? "))
            if dias > 0:
                break
            print("[ERRO] A quantidade de dias deve ser maior que zero.")
        except ValueError:
            print("[ERRO] Digite um número inteiro para os dias.")
    
    custo_total = dias * 1000.0
    print(f"Custo total: R$ {custo_total:,.2f} | Verificando saldo...")

    if cliente["saldo"] < custo_total:
        print("[NEGADO] Saldo insuficiente para este aluguel.")
        return
    
    if input("Confirmar locação? (s/n): ").lower() == 's':
        cliente["saldo"] -= custo_total
        carro_removido = carros_aluguel.pop(escolha)
        print(f"Sucesso! Você alugou o {carro_removido[1]}. Aproveite!")

def comprar_carro():
    print("\n--- COMPRA DE VEÍCULOS ---")
    if not carros_vendas:
        print("Estoque vazio.")
        return

    for i, carro in enumerate(carros_vendas):
        print(f"{i + 1} - {carro[0]} ({carro[1]})")

    # Blindagem da escolha do veículo
    while True:
        try:
            escolha = int(input("Digite o número do veículo desejado: ")) - 1
            if 0 <= escolha < len(carros_vendas):
                break
            print("[ERRO] Opção fora do intervalo da lista.")
        except ValueError:
            print("[ERRO] Entrada inválida. Use apenas números.")

    modelo_escolhido = carros_vendas[escolha][0]
    preco = tabela_precos[modelo_escolhido] * 1.25 # Margem de lucro da loja

    print(f"Preço de venda: R$ {preco:,.2f}")
    
    if input("Deseja finalizar a compra? (s/n): ").lower() == 's':
        if cliente["saldo"] >= preco:
            cliente["saldo"] -= preco
            carros_vendas.pop(escolha)
            print("Parabéns! Veículo adquirido com sucesso.")
        else:
            print("[NEGADO] Saldo insuficiente.")
    else:
        print("Compra cancelada.")

def exibir_menu():
    print("\n" + "="*30)
    print("      MENU CONCESSIONÁRIA")
    print("="*30)
    print("1. Vender meu carro")
    print("2. Comprar um carro")
    print("3. Alugar um carro")
    print("4. Ver meu saldo")
    print("5. Sair do sistema")
    return input("\nEscolha uma opção: ")

# --- LOOP PRINCIPAL ---
while True:
    opcao = exibir_menu()

    match opcao:
        case "1": vender_carro()
        case "2": comprar_carro()
        case "3": alugar_carro()
        case "4": print(f"\nSaldo Atual: R$ {cliente['saldo']:,.2f}")
        case "5":
            print("Obrigado por utilizar nossos serviços. Até logo!")
            break
        case _:
            print("[AVISO] Opção inválida. Tente novamente.")

