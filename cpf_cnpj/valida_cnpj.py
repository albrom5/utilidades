from random import randint


def valida_cnpj(cnpj):
    """
    Validador de CNPJ, conforme regras da Receita Federal
    :param cnpj: CPF informado pelo usuário, pode conter pontos e traços, que serão ignorados.
    :return: boolean que informa se o CPF é válido
    """
    cnpj = cnpj.replace('.', '')  # Elimina os pontos
    cnpj = cnpj.replace('-', '')  # Elimina os traços
    cnpj = cnpj.replace('/', '')  # Elimina a barra

    # Verifica se o CNPJ possui todos os digitos iguais, se tem menos dígitos que o necessário
    # ou se algum dígito não é numérico
    for i in range(0, 14):
        if cnpj == str(i) * 14 or len(cnpj) != 14 or not cnpj[i].isnumeric():
            return False
    # Calcula o primeiro dígito de validação.
    soma = 0
    for d in range(0, 4):
        soma += int(cnpj[d]) * (5 - d)
    for d in range(4, 12):
        soma += int(cnpj[d]) * (13 - d)
    resto = 11 - (soma % 11)
    if resto > 9:
        resto = 0
    # Verifica se o primeiro dígito calculado é diferente do informado
    if str(resto) != cnpj[12]:
        return False
    else:
        # Calcula o segundo dígito de validação.
        soma = 0
        for d in range(0, 5):
            soma += int(cnpj[d]) * (6 - d)
        for d in range(5, 13):
            soma += int(cnpj[d]) * (14 - d)
        resto = 11 - (soma % 11)
        if resto > 9:
            resto = 0
        # Verifica se o segundo dígito calculado é diferente do informado
        if str(resto) != cnpj[13]:
            return False
        else:
            return True


def geracnpj(formatado=True):
    """
    Gera um CNPJ válido conforme regras da Receita Federal
    :param formatado: inclui pontos, traço e barra, padrão: True
    :return: cnpj gerado aleatoriamente
    """
    cnpj = '11111111111111'
    # Verifica se todos os dígitos são iguais
    while cnpj == cnpj[0] * 14:
        # Gera os primeiros 8 dígitos aleatoriamente
        cnpj = [str(randint(0, 8)) for i in range(8)]
        cnpj = ''.join(cnpj)
        cnpj += '0001'
        # Calcula o primeiro dígito de validação
        soma = 0
        for d in range(0, 4):
            soma += int(cnpj[d]) * (5 - d)
        for d in range(4, 12):
            soma += int(cnpj[d]) * (13 - d)
        resto = 11 - (soma % 11)
        if resto > 9:
            resto = 0
        cnpj += str(resto)
        # Calcula o segundo dígito de validação
        soma = 0
        for d in range(0, 5):
            soma += int(cnpj[d]) * (6 - d)
        for d in range(5, 13):
            soma += int(cnpj[d]) * (14 - d)
        resto = 11 - (soma % 11)
        if resto > 9:
            resto = 0
        cnpj += str(resto)
    if formatado:
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    else:
        return cnpj


user_cnpj = str(input('Digite seu CNPJ: '))
cnpjisvalid = valida_cnpj(user_cnpj)
if cnpjisvalid:
    print('CNPJ é válido!')
else:
    print('CNPJ INVÁLIDO!')
random_cnpj = geracnpj()
if valida_cnpj(random_cnpj):
    print(f'O CNPJ {random_cnpj} é válido!')
else:
    print(f'O CNPJ {random_cnpj} é INVÁLIDO!')
