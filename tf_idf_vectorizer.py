import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import joblib


def check_if_stopwords_exist():
    stopwords_confirm = Path("stopwords_exist.txt")

    if stopwords_confirm.is_file():
        return True
    
    else:
        nltk.download("stopwords")

        with open("stopwords_exist.txt", "x") as file:
            file.write("melhorando o runtime e a logica do codigo, esse arquivo so serve pra passar pela logica de instalar as stopwords toda vez que o script do TF-IDF RODAR =)")
            return False



with open('faq_json.json', 'r', encoding = 'utf-8') as corpus:
    file = json.load(corpus)



#list comprehesion para passar texto para a funcao do tf-idf
faq_perguntas = [item["pergunta"].strip('"') for item in file]

faq_respostas = [item["resposta"] for item in file]


check_if_stopwords_exist()
from nltk.corpus import stopwords

portuguese_stopwords = stopwords.words("portuguese")


vectorizer = TfidfVectorizer(
    stop_words = portuguese_stopwords,
    lowercase = True,
    token_pattern = r'(?u)\b[a-záàâãéêíóôõúüç]+\b',
    min_df = 1,
    max_df = 1
)



X = vectorizer.fit_transform(faq_perguntas)



feature_names = vectorizer.get_feature_names_out()



#Persistindo o vectorizer ja treinado, a matriz de perguntas/respostas e afins dentro de um arquivo .pkl
joblib.dump({
    "vectorizer":vectorizer,
    "matrix": X,
    "respostas": faq_respostas
},"faq_pipeline.pkl")



print(feature_names)
print(X.shape)
