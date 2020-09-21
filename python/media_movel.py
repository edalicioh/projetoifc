import datetime as DT


def media(create, dadosModel):
    create.create_table_media_movel()
    casos = dadosModel.find_by_obito_all()

    index = 0

    for caso in casos:

        var = (
            caso['codigo_ibge_municipio'],
            caso['data_obito'] - DT.timedelta(days=7),
            caso['data_obito'],
        )

        pe = dadosModel.find_periudo(var)

        params = (
            caso['municipio'],
            caso['codigo_ibge_municipio'],
            caso['data_obito'],
            len(pe),
            len(pe) / 7,
        )
        index += 1
        print(index)
        dadosModel.insert_media_movel(params)


if __name__ == "__main__":

    from db.create import Create
    from dao.DadosDao import DadosDao
    create = Create()
    dadosModel = DadosDao()
    media(create, dadosModel)
