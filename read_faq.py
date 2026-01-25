#A Ideia e, nesse projeto, tentar NAO usar um RAG, e sim algum outro tipo de ferramenta pra transforamr o excel num FAQ pra IA
import pandas as pd



df = pd.read_excel('perguntas_faq.xlsx', sheet_name = 'Planilha1')


#Aqui ja retorna o Json como uma lista de dicionarios
df.to_json('faq_json.json', indent = 4, orient = 'records', force_ascii = True)


print("Json salvo com sucesso")

