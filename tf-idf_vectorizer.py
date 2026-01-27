import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk



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



#list compaharasion para passar texto para a funcao do tf-idf
json_to_text = [item["Resposta"] for item in file]



check_if_stopwords_exist()
from nltk.corpus import stopwords

portuguese_stopwords = stopwords.words("portuguese")


vectorizer = TfidfVectorizer(
    stop_words = portuguese_stopwords,
    lowercase = True,
    token_pattern = r'(?u)\b[a-záàâãéêíóôõúüç]+\b',
    min_df = 1,
    max_df = 0.9
)



X = vectorizer.fit_transform(json_to_text)



feature_names = vectorizer.get_feature_names_out()



print(feature_names)
print(X.shape)
