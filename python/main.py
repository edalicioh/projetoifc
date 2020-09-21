import csv
import os
import shutil
import urllib.request as request
from contextlib import closing
from datetime import datetime

import charts
import media_movel

from db.create import Create
from dao.DadosDao import DadosDao
from Utils import Utils


def main():
    index = 0
    path_ftp = "ftp://boavista:dados_abertos@ftp2.ciasc.gov.br/boavista_covid_dados_abertos.csv"
    file_name = "python/csv/boavista_covid_dados_abertos.csv"

    inicio = datetime.now()
    create = Create()
    dadosDao = DadosDao()

    create.create_table()
    values = []

    def req():
        with closing(request.urlopen(path_ftp)) as r:
            with open(file_name, 'wb') as f:
                print("Download")
                shutil.copyfileobj(r, f)

    with open(file_name, 'r') as arquivo:

        dados = csv.DictReader(arquivo, delimiter=";")
        for value in dados:
            index = index + 1
            data_obito = None
            data_entrada_uti = None
            data_internacao = None
            data_evolucao_caso = None
            data_saida_uti = None
            data_coleta = None

            data_publicacao = Utils.datetime_format(value['data_publicacao'])
            data_inicio_sintomas = Utils.date_format(
                value['data_inicio_sintomas'])

            idade = value['idade']
            if idade == 'NULL':
                idade = None

            if value['data_coleta'] != 'IGNORADO':
                data_coleta = Utils.date_format(value['data_coleta'])

            if value['data_obito'] != 'NULL':
                data_obito = Utils.date_format(value['data_obito'])

            if value['data_internacao'] != 'NULL':
                data_internacao = Utils.date_format(value['data_internacao'])

            if value['data_entrada_uti'] != 'NULL':
                data_entrada_uti = Utils.date_format(value['data_entrada_uti'])

            if value['data_evolucao_caso'] != 'NULL':
                data_evolucao_caso = Utils.date_format(
                    value['data_evolucao_caso'])

            data_resultado = Utils.datetime_format(value['data_resultado'])

            val = (
                data_publicacao,
                value['recuperados'],
                data_inicio_sintomas,
                data_coleta,
                value['sintomas'],
                value['comorbidades'],
                value['gestante'],
                value['internacao'],
                value['internacao_uti'],
                value['sexo'],
                value['municipio'],
                value['obito'],
                data_obito,
                idade,
                value['regional'],
                value['raca'],
                data_resultado,
                value['codigo_ibge_municipio'],
                value['latitude'],
                value['longitude'],
                value['estado'],
                value['criterio_confirmacao'],
                value['tipo_teste'],
                value['municipio_notificacao'],
                value['codigo_ibge_municipio_notificacao'],
                value['latitude_notificacao'],
                value['longitude_notificacao'],
                value['classificacao'],
                value['origem_esus'],
                value['origem_sivep'],
                value['origem_lacen'],
                value['origem_laboratorio_privado'],
                value['nom_laboratorio'],
                value['fez_teste_rapido'],
                value['fez_pcr'],
                data_internacao,
                data_entrada_uti,
                value['regional_saude'],
                data_evolucao_caso,
                data_saida_uti,
                value['bairro'],

            )
            values.append(val)
            if len(values) % 5000 == 0:
                dadosDao.insert_many(values)
                print("---------------------------------")
                print(index)
                print("---------------------------------")
                values = []
        dadosDao.insert_many(values)

    charts.chart(create, dadosDao)
    media_movel.media(create, dadosDao)

    # os.remove(file_name)
    print(inicio)
    print(datetime.now())
    print("Finall")


if __name__ == "__main__":
    main()
