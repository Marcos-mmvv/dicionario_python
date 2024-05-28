# Dicionário

print(f'{'-'*20} CADASTR0 GERAL {'-'*20}')

pessoa = {
    'Nome' : input('Digite o seu nome: '),
    'CPF' : int(input('Digite o seu CPF: ')),
    'RG' : int(input(' Digite o seu RG: ')),
    'Data de Nascimento' : input('Digite a data de nascimento: '),
    'Gênero' : input('Informe o seu gênero: '),
    'E-mail' : input('Informe o seu e-mail: '),
    'Telefone' : int(input('Informe o seu telefone: ')),
    'Tipo Sanguíneo' : input('Informe o seu tipo sanguíneo: '),
    'Profissão' : input('Informe a sua profissão: '),
    'Empresa' : input('Informe o nome da empresa que você trabalha: ')
}

for cad in pessoa:
    print()
    print(f'{cad}:{pessoa.get(cad)}')


