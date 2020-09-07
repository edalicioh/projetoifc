import datetime


class Utils:

    @staticmethod
    def datetime_format(date):
        saida = date

        if len(date) > 16:
            exp = date.split('.')
            saida = exp[0][:-3]
            saida_exp = saida.split('-')
            if len(saida_exp) > 2:
                return datetime.datetime.strptime(saida, '%Y-%m-%d %H:%M')

        return datetime.datetime.strptime(saida, '%d/%m/%Y %H:%M').strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def date_format(date):
        exp = date.split(' ')
        saida_exp = exp[0].split('-')
        saida_time = exp[0].split(':')

        if len(saida_time) > 2:
            return datetime.datetime.strptime("1970-01-01", '%Y-%m-%d')

        if len(saida_exp) > 2:
            return datetime.datetime.strptime(exp[0], '%Y-%m-%d')

        return datetime.datetime.strptime(exp[0], '%d/%m/%Y').strftime("%Y-%m-%d")
