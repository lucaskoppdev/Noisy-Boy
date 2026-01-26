import json
from sklearn.feature_extraction.text import TfidfVectorizer


with open('faq_json.json', 'r', encoding = 'utf-8') as corpus:
    file = json.load(corpus)


#list compaharasion para passar texto para a funcao do tf-idf
json_to_text = [item["Resposta"] for item in file]


vectorizer = TfidfVectorizer()


X = vectorizer.fit_transform(json_to_text)


feature_names = vectorizer.get_feature_names_out()


print(feature_names)
print(X.shape)