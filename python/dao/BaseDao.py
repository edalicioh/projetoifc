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

    def insert_many(self, args):

        print(args)
        lista = list(args.keys())
        itens = ",".join([str(i) for i in lista])
        values = tuple(args.values())
        sainda = ",".join([str('%s') for i in lista])

        sql = f"""INSERT INTO {self._table} ({itens}) VALUES ({sainda})"""
        self.db.execute_many(sql, values)
        self.db.conn.commit()

    def find_all(self):
        sql = f"""SELECT * FROM {self._table}"""
        cursor = self._db.execute_query(sql)
        return cursor.fetchall()

    def find_row(self, row, values=None):
        sql = f"""SELECT * FROM {self._table} {row}"""
        cursor = self._db.execute_query(sql, values)
        return cursor.fetchall()
