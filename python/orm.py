

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
