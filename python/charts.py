import csv
from dao.DadosDao import DadosDao
from db.create import Create

dadosDao = DadosDao()
create = Create()

create.create_table_chart()

casos = dadosDao.find_by_caso()
obitos = dadosDao.find_by_obito()

file_name = "csv/populacao.csv"

with open(file_name, 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

obitoTotal = 0
incidencia = 0
positivos = 0
cidade = ''


for dado in dados:
    for caso in casos:
        if caso[0].upper() == dado['municipio'].upper():

            populacaoSplit = dado['populacao'].split(".")
            populacao = int(populacaoSplit[0] + populacaoSplit[1])

            incidencia = round((int(caso[1]) / populacao) * 100, 3)
            positivos = caso[1]
            cidade = dado['municipio']

    for obito in obitos:
        if obito[0].upper() == dado['municipio'].upper():
            obitoTotal = obito[1]

    var = (
        cidade,
        obitoTotal,
        positivos,
        incidencia,
    )
    is_cidade = len(dadosDao.find_by_cidade((cidade,)))
    print(is_cidade)
    if is_cidade == 0:
        dadosDao.insert_chart(var)
