from random import randint


def valida_cpf(cpf):
    """
    Validador de CPF, conforme regras da Receita Federal
    :param cpf: CPF informado pelo usuário, pode conter pontos e traços, que serão ignorados.
    :return: boolean que informa se o CPF é válido
    """
    cpf = cpf.replace('.', '')  # Elimina os pontos
    cpf = cpf.replace('-', '')  # Elimina os traços

    # Verifica se o CPF possui todos os digitos iguais, se tem menos dígitos que o necessário
    # ou se algum dígito não é numérico
    for i in range(0, 10):
        if cpf == str(i) * 11 or len(cpf) != 11 or not cpf[i].isnumeric():
            return False
    # Calcula o primeiro dígito de validação.
    lista_mult = [int(cpf[d]) * (10 - d) for d in range(0, 9)]
    resto = 11 - (sum(lista_mult) % 11)
    if resto > 9:
        resto = 0
    # Verifica se o primeiro dígito calculado é diferente do informado
    if str(resto) != cpf[9]:
        return False
    else:
        # Calcula o segundo dígito de validação.
        lista_mult.clear()
        lista_mult = [int(cpf[d]) * (11 - d) for d in range(0, 10)]
        resto = 11 - (sum(lista_mult) % 11)
        if resto > 9:
            resto = 0
        # Verifica se o segundo dígito calculado é diferente do informado
        if str(resto) != cpf[10]:
            return False
        else:
            return True


def geracpf(formatado=True):
    """
    Gera um CPF válido conforme regras da Receita Federal
    :param formatado: inclui pontos e traço, padrão: True
    :return: cpf gerado aleatoriamente
    """
    cpf = '11111111111'
    # Verifica se todos os dígitos são iguais
    while cpf == cpf[0] * 11:
        # Gera os primeiros 9 dígitos aleatoriamente
        cpf = [str(randint(0, 9)) for i in range(9)]
        cpf = ''.join(cpf)
        # Calcula o primeiro dígito de validação
        lista_mult = [int(cpf[d]) * (10 - d) for d in range(0, 9)]
        resto = 11 - (sum(lista_mult) % 11)
        if resto > 9:
            resto = 0
        cpf += str(resto)
        lista_mult.clear()
        # Calcula o segundo dígito de validação
        lista_mult = [int(cpf[d]) * (11 - d) for d in range(0, 10)]
        resto = 11 - (sum(lista_mult) % 11)
        if resto > 9:
            resto = 0
        cpf += str(resto)
    if formatado:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    else:
        return cpf


user_cpf = str(input('Digite seu CPF: '))
cpfisvalid = valida_cpf(user_cpf)
if cpfisvalid:
    print('CPF é válido!')
else:
    print('CPF INVÁLIDO!')
random_cpf = geracpf()
if valida_cpf(random_cpf):
    print(f'O CPF {random_cpf} é válido!')
else:
    print(f'O CPF {random_cpf} é INVÁLIDO!')
