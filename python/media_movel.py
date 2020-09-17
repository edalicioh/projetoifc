import datetime as DT


def media(create, dadosDao):

    create.create_table_media_movel()
    casos = dadosDao.find_all()

    for caso in casos:

        var = (
            caso[17],
            caso[12] - DT.timedelta(days=7),
            caso[12],
        )

        pe = dadosDao.find_periudo(var)

        print(caso[17])
        params = (
            caso[23],
            caso[17],
            caso[12],
            len(pe),
            len(pe) / 7,
        )

        dadosDao.insert_media_movel(params)
