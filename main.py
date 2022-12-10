# se o nome da pasta for 'email' o python vai importar uma biblioteca própria
from emaill.enviarEmail import EnviarEmail
from emaill.readData import ReadData
from cracha.gerarCracha import GerarCracha

# salva inscritos na pasta InscritosPresentes
df = ReadData().link(
    'https://docs.google.com/spreadsheets/d/1IQq62C_GPqEou536OyfRQXyB9KpVyMLsUKbXrYVYmA8/edit?usp=sharing',
    nome_evento='workshopPython2022',
    registrar_inscricao=True)

print(df)
print('\n\n')

# enviar emails
email = EnviarEmail()
for i in range(df.shape[0]):
    email.enviar(i, df['email'][i], df['nome'][i], df['cpf'][i],
                 cracha=True,
                 path_arquivo_anexo=None)
