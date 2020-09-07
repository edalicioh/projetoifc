
from Database import Database


class Create:

    def __init__(self):
        self.db = Database.get_instance()

    def create_table(self):
        sql = "drop table dados"

        self.db.execute_query(sql)

        sql = """
            CREATE TABLE dados (                
                data_publicacao TIMESTAMP,
                recuperados varchar(20),
                data_inicio_sintomas date,
                data_coleta date,
                sintomas varchar(255),
                comorbidades varchar(255),
                gestante varchar(50),
                internacao varchar(50),
                internacao_uti varchar(50),
                sexo varchar(50),
                municipio varchar(255),
                obito varchar(20),
                data_obito date,
                idade int(11),
                regional varchar(255),
                raca varchar(100),
                data_resultado varchar(50),
                codigo_ibge_municipio varchar(100),
                latitude varchar(100),
                longitude varchar(100),
                estado varchar(255),
                criterio_confirmacao varchar(255),
                tipo_teste varchar(255),
                municipio_notificacao varchar(255),
                codigo_ibge_municipio_notificacao varchar(255),
                latitude_notificacao varchar(100),
                longitude_notificacao varchar(100),
                classificacao varchar(100),
                origem_esus varchar(100),
                origem_sivep varchar(100),
                origem_lacen varchar(100),
                origem_laboratorio_privado varchar(100),
                nom_laboratorio varchar(100),
                fez_teste_rapido varchar(100),
                fez_pcr varchar(100),
                data_internacao date,
                data_entrada_uti date,
                regional_saude varchar(100),
                data_evolucao_caso date,
                data_saida_uti date,
                bairro varchar(100)

            )
        """
        self.db.execute_query(sql)
        print("Create table")

    def create_table_chart(self):
        sql = "drop table dados_chart"
        self.db.execute_query(sql)
        sql = """
            CREATE TABLE dados_chart (
                cidade varchar(200),
                obitos varchar(20),
                positivos varchar(50),
                incidencia varchar(50)
            )
        """
        self.db.execute_query(sql)
        print("Create table Incidência/100mil habitantes")
