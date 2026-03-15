usuarios = {}
while True:
 print("1 - cadastrar")
 print("2 - login")
 print("0 - sair")
 opcao = input("escolha uma opção")
 if opcao == "0":
  break
 elif opcao == "1": 
    email = input("digite seu email")
    senha = input("digite sua senha")
    if email in usuarios:
        print("email já cadastrado")
    else:
        usuarios[email] = {
            "senha": senha,
            "saldo": 0
        }
        print("usuario cadastrado com sucesso")
 elif opcao == "2":
            email = input("digite seu email")
            senha = input("digite sua senha")
            
            if email in usuarios:
                if usuarios[email]["senha"] == senha:
                    print("bem vindo!")
                    while True:
                        print("1 - ver saldo")
                        print("2 - depositar")
                        print("3 - sacar")
                        print("0 - sair")
                        
                        opcao_banco = input("escolha: ")
                        if opcao_banco == "1":
                            print("seu saldo é", usuarios[email]["saldo"])
                        
                        elif opcao_banco == "2":
                            valor = float(input("quanto deseja depositar?"))
                            usuarios[email]["saldo"] += valor
                            print("depósito realizado!")
                        elif opcao_banco == "0":
                            break
                        
                        elif opcao_banco == "3":
                            valor = float(input("quanto deseja sacar? "))
                        
                        
                            if valor <= usuarios[email]["saldo"]:
                                usuarios[email]["saldo"]-= valor
                                print("saque realizado!")
                            else:
                                print("saldo insuficiente!")
                else:
                    print("senha incorreta")
            else:
                print("email não encontrado")
                           


                    

   

