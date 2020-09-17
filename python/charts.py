import csv
from unidecode import unidecode


def chart(create, dadosDao):
    obitoTotal = 0
    incidencia = 0
    positivos = 0
    cidade = ''
    file_name = "python/csv/populacao.csv"

    create.create_table_chart()

    casos = dadosDao.find_by_caso()
    obitos = dadosDao.find_by_obito()

    with open(file_name, 'r') as arquivo:
        dados = [x for x in csv.DictReader(arquivo)]

    for dado in dados:
        for caso in casos:
            if caso[0].upper() == unidecode(dado['municipio'].upper()):

                populacaoSplit = dado['populacao'].split(".")
                populacao = int(populacaoSplit[0] + populacaoSplit[1])

                incidencia = round((int(caso[1]) / populacao) * 100, 3)
                positivos = caso[1]
                cidade = dado['municipio']

        for obito in obitos:
            if obito[0].upper() == unidecode(dado['municipio'].upper()):
                obitoTotal = obito[1]

        var = (
            dado['codigo'],
            cidade,
            obitoTotal,
            positivos,
            incidencia,
            populacao,
        )
        is_cidade = len(dadosDao.find_by_cidade((cidade,)))
        print(cidade)
        if is_cidade == 0:
            dadosDao.insert_chart(var)
