from dao.Dao import Dao


class DadosDao(Dao):

    def insert(self, params):
        sql = """
            INSERT INTO dados (
                data_publicacao,
                recuperados,
                data_inicio_sintomas,
                data_coleta,
                sintomas,
                comorbidades,
                gestante,
                internacao,
                internacao_uti,
                sexo,
                municipio,
                obito,
                data_obito,
                idade,
                regional,
                raca,
                data_resultado,
                codigo_ibge_municipio,
                latitude,
                longitude,
                estado,
                criterio_confirmacao,
                tipo_teste,
                municipio_notificacao,
                codigo_ibge_municipio_notificacao,
                latitude_notificacao,
                longitude_notificacao,
                classificacao,
                origem_esus,
                origem_sivep,
                origem_lacen,
                origem_laboratorio_privado,
                nom_laboratorio,
                fez_teste_rapido,
                fez_pcr,
                data_internacao,
                data_entrada_uti,
                regional_saude,
                data_evolucao_caso,
                data_saida_uti,
                bairro
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
        """

        self.db.execute_query(sql, params)
        self.db.conn.commit()

    def find_by_obito(self):

        sql = """
            SELECT
            municipio,
            COUNT(*)
            FROM dados
            WHERE obito = 'SIM'
            GROUP BY municipio
        """
        cursor = self.db.execute_query(sql)
        return cursor.fetchall()

    def find_by_caso(self):

        sql = """
            SELECT
            municipio,
            COUNT(*)
            FROM dados
            WHERE classificacao = 'CONFIRMADO'
            GROUP BY municipio
        """
        cursor = self.db.execute_query(sql)
        return cursor.fetchall()

    def insert_chart(self, params):
        sql = """
            INSERT INTO dados_chart (
                codigo_ibge_municipio,
                cidade,
                obitos,
                positivos ,
                incidencia,
                populacao
            ) VALUES (%s,%s, %s, %s, %s,%s)
        """

        self.db.execute_query(sql, params)
        self.db.conn.commit()

    def find_by_cidade(self, param):
        sql = """
            SELECT * FROM dados_chart WHERE cidade = %s
        """
        cursor = self.db.execute_query(sql, param)
        return cursor.fetchall()

    def find_all(self):
        sql = """
            SELECT
            *
            FROM dados
            where obito = 'SIM'
        """
        cursor = self.db.execute_query(sql)
        return cursor.fetchall()

    def find_periudo(self, params):
        sql = """
            SELECT   
            *
            FROM dados 
            WHERE codigo_ibge_municipio = %s
            AND data_obito >=  %s
            AND data_obito <=  %s
        """
        cursor = self.db.execute_query(sql, params)
        return cursor.fetchall()

    def insert_media_movel(self, params):
        sql = """
            INSERT INTO media_movel (
                cidade,
                codigo_ibge_municipio,
                data_obito ,
                quantidade_periudo ,
                media
            ) VALUES (%s, %s, %s, %s,%s)
        """

        self.db.execute_query(sql, params)
        self.db.conn.commit()
