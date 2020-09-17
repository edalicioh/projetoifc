from Database import Database


class BaseDao:
    _db = None
    _table = ''

    def __init__(self):
        self._db = Database.get_instance()

    def insert(self, args):
        lista = list(args.keys())
        itens = ",".join([str(i) for i in lista])
        values = tuple(args.values())
        sainda = ",".join([str('%s') for i in lista])

        sql = f"""INSERT INTO {self._table} ({itens}) VALUES ({sainda})"""
        self._db.execute_query(sql, values)
        self._db.conn.commit()

    def find_all(self):
        sql = f"""SELECT * FROM {self._table}"""
        cursor = self._db.execute_query(sql)
        return cursor.fetchall()


class BaseModel(BaseDao):

    def __init__(self, table):
        super().__init__()
        self._table = table


class TestModel(BaseModel):

    def __init__(self):
        super().__init__("dados_chart")


args = {
    'codigo_ibge_municipio': '4200051',
    'cidade': 'Anchieta',
    'obitos': '10',
    'positivos ': '10',
    'incidencia': '21',
    'populacao': '100'
}

test = TestModel()

ass = test.find_all()

print(ass)
