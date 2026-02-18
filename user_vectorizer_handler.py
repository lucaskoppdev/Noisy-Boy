#Abstracao para testar como vai funcionar a deteccao das perguntas do usuario e afins
from sklearn.metrics.pairwise import cosine_similarity
import joblib


#carregar o "payload" vindo do tf_idf_vectorizer
data =  joblib.load("faq_pipeline.pkl")
vectorizer = data["vectorizer"]
X = data["matrix"]
respostas = data["respostas"]


def get_user_question():
    return input("Digite a sua pergunta -> ").strip()



def answers_user_question(
        user_question,
        vectorizer,
        matrix_X,
        faq_answers
):

    vectorized_question = vectorizer.transform([user_question.strip()])

    question_answer_similarity = cosine_similarity(vectorized_question, matrix_X)

    scores = question_answer_similarity[0]

    best_index = scores.argmax()

    best_score = scores[best_index]

    if best_score >= 0.8:
        return faq_answers[best_index]
    else:
        print(best_score)
        print(best_index)
        return None



#loop de teste gambiarra
print("==>Digite sair para encerrar<==")
while True:
    user_input = get_user_question()

    if user_input in ['sair', 'exit', 'encerrar']:
        print("Encerrado")
        break

    resposta = answers_user_question(
        user_question=user_input,
        vectorizer=vectorizer,
        matrix_X=X,
        faq_answers=respostas
    )

    print("Resposta: ", resposta)

