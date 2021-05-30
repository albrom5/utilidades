from datetime import date


class Contrato:
    _counter = 0 
    _registros = [] # Armazena lista de registros

    def __init__(self, objeto) -> None:
        Contrato._counter += 1
        self.objeto = objeto
        self.data_criacao = data_criacao=date.today()
        self.id = Contrato._counter
        self.numero = ''
        self._registros.append(self)
        self.numero = self.gera_sequencial()
        
    def gera_sequencial(self):
        registros_ordenados = sorted(self._registros)
        last_register = '0000/0000'
        ano_criacao = str(self.data_criacao.year)
        seq_novo = ''
        # Obtém a lista de registros com o mesmo ano de criação do registro atual
        registros_filtrados_ano = [
            registro for registro in registros_ordenados if str(registro.data_criacao.year) == ano_criacao
        ]
        if len(registros_filtrados_ano) <=1: # Verifica se é o primeiro registro da lista
            last_register = f'0001/0000'
        else:
            if registros_filtrados_ano[-2].numero == '': # Verifica se o último registro cadastrado está com o número vazio 
                last_register = f'0001/{ano_criacao}'
            else:
                last_register = registros_filtrados_ano[-2].numero
        last_register = last_register.split('/')
        ano_last_register = last_register[1]
        if ano_last_register == ano_criacao:
            seq_novo = int(last_register[0]) + 1
        else:
            seq_novo = 1     
        seq_novo = str(seq_novo).zfill(4)
        sequencial = f'{seq_novo}/{ano_criacao}'
        return sequencial

    def __lt__(self, other):
        return self.data_criacao < other.data_criacao

    def __str__(self) -> str:
        return f'{self.numero} - {self.objeto}'
