from freezegun import freeze_time
from auto_sequence_by_year import Contrato

contador = 0
for i in range(1, 3):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')

freezer = freeze_time("2022-01-14 12:00:01")
freezer.start()
for i in range(1, 3):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')
freezer.stop()

freezer = freeze_time("2014-01-14 12:00:01")
freezer.start()
for i in range(1, 3):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')
freezer.stop()

for i in range(1, 3):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')

freezer = freeze_time("2022-01-14 12:00:01")
freezer.start()
for i in range(1, 4):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')
freezer.stop()

freezer = freeze_time("2014-01-14 12:00:01")
freezer.start()
for i in range(1, 9):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')
freezer.stop()

for i in range(1, 3):
    contador += 1
    Contrato(objeto=f'Contrato {contador}')

Contrato._registros.sort()

for contratos in Contrato._registros:
    print(f'{contratos} cadastrado com sucesso em {contratos.data_criacao}')

print(f'Foram cadastrados {len(Contrato._registros)} contratos no total.')
