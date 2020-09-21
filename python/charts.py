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
    index = 0
    for dado in dados:

        for caso in casos:
            if caso['municipio'].upper() == unidecode(dado['municipio'].upper()):

                populacaoSplit = dado['populacao'].split(".")
                populacao = int(populacaoSplit[0] + populacaoSplit[1])

                incidencia = round((int(caso['total']) / populacao) * 100, 3)
                positivos = caso['total']
                cidade = dado['municipio']

        for obito in obitos:
            if obito['municipio'].upper() == unidecode(dado['municipio'].upper()):
                obitoTotal = obito['total']

        params = (
            dado['codigo'],
            cidade,
            obitoTotal,
            positivos,
            incidencia,
            populacao,
        )
        is_cidade = len(dadosDao.find_by_cidade((cidade,)))
        if is_cidade == 0:
            index += 1
            print(index)
            dadosDao.insert_chart(params)


if __name__ == "__main__":

    from db.create import Create
    from dao.DadosDao import DadosDao
    create = Create()
    dadosDao = DadosDao()
    chart(create, dadosDao)
