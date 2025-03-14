# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.

print('Nubank: ')
for pessoa in nubank:
    print(pessoa)

print('\nC6: ')
for pessoa in c6:
    print(pessoa)

print('\nInter: ')
for pessoa in inter:
    print(pessoa)
