nome = input (" Qual é o seu nome? ")
idade = input (" Quantos anos você tem? ")
idade = int(idade)
ja_fez = input("Você ja fez aniversário esse ano? (sim/nao): ")
ano_nascimento = 2026 - idade
if ja_fez == "nao": 
    ano_nascimento = ano_nascimento - 1
print(f"Fala {nome}! Se você ja fez aniversário este ano, você nasceu em {ano_nascimento}.")