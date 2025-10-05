#quero um sistema de diario que armazene os pensamentos de um usuario, one contenha login e senha.
import time
art='''
⠀⠀⠀⠀⠀⠀⠀⣀⡠⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠔⢉⡀⡀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠆⠉⠉⠛⠢⣄⠀⠀⠀⠀
⠀⠀⣀⡠⡷⢾⣿⣯⣍⣦⡀⠁⠨⢨⠆⠀⠀⠀⠀⠀⠀⣠⠾⠉⡀⠀⣈⡀⠤⣤⣭⣱⡀⠀⠀
⠀⣾⠉⠀⠀⠀⠈⠉⠙⠿⣿⣦⣤⣑⣯⣄⠀⠀⠀⠀⣰⣋⣶⣯⣁⣼⡷⠶⠟⠛⠿⠿⢧⠀⠀
⢰⣅⢆⠀⠀⠀⠀⠀⠀⠤⡔⠞⢹⣿⣇⣾⣧⡀⠀⢠⣿⣿⣯⡿⠋⠁⠀⠀⠀⠀⠀⠀⠊⢋⡄
⢸⣗⢊⣄⣈⣀⣤⡀⣀⡴⣾⡻⣾⣿⣿⣽⡿⠿⣿⣿⣿⣟⣿⣟⡲⢒⣀⠁⠀⠀⠀⠀⠀⢘⡇
⠘⣿⡿⣿⣿⢍⠙⣛⣻⣿⣿⣷⣾⣿⣿⣿⣿⣶⣾⣿⣿⣛⣳⣭⣿⣏⣥⣴⣦⣤⣤⣤⡀⠇⡇
⠀⠈⠙⠻⠮⠾⠟⠦⠬⣷⡿⠑⡉⡑⡿⡝⠀⠀⠹⣿⣿⣛⣿⣯⠭⢌⡋⣉⢢⣉⣉⣹⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⣰⡾⠙⠀⠀⠀⠀⣟⡊⠃⠕⢻⠇⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡟⠊⠀⢠⡰⣾⢿⠃⠀⠀⠀⠀⠹⡇⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⠆⠀⢰⠠⠉⣰⠄⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠋⠀⡔⢠⡟⠀⡏⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠏⠀⠀⠁⠈⠁⡜⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡀⠀⢰⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣔⠐⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⡀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⣦⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⡬⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
for linha in art.splitlines ():
    print(linha)
    time.sleep(0.1)

usuario_correto = 'Vitoria'
senha_correta = 'ravick123'

usuario=input('Digite o seu usuario:')
senha=input('Digite por favor sua senha')

if usuario == usuario_correto and senha == senha_correta:
 print('Acesso permitido. Bem-vindo ao seu diário!')

#Começo do diario
pensamento=[]
while True:
 print('\n O que deseja acrescentar ao seu diário?')
 print('1-Adicionar um pensamento')
 print('2- Remover um pensamento')
 print('3- Tornar pensamento favorito')
 print('4- Sair do diario')
 
 opção=input('escolha uma opção:')

 if opção=='1':
   novo_pensamento=input('Digite seu pensamento:')
   pensamento.append(novo_pensamento)
   
   print('\n seu pensamento foi registrado no seu diario!')

 elif opção=='2':
   remover_pensamento=input('O que deseja remover?')
   if remover_pensamento in pensamento:
     pensamento.remove(remover_pensamento)
     print('Seu pensamento foi removido!')
   else:
     print('Não foi encontrado esse pensamento no seu diário.\n' \
     'por favor, verifique os seus pensamentos atuais:')

 elif opção=='3':
   favorito-input('Tem um pensamento especial? Qual é?')
 
