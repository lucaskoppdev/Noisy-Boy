#Abstracao para testar como vai funcionar a deteccao das perguntas do usuario e afins
from sklearn.metrics.pairwise import cosine_similarity
import joblib


#carregar o "payload" vindo do tf_idf_vectorizer
data =  joblib.load("faq_pipeline.pkl")
vectorizer = data["vectorizer"]
X = data["matrix"]
respostas = data["respostas"]



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
        return "não foi encontrada uma resposta satisfatória para sua pergunta, tente falar de outro jeito pra eu te ajudar !"



def main_function():
    print("==>Digite sair para encerrar<==")
    user_input = input("Digite a sua pergunta ->")

    if user_input in ['sair', 'exit', 'encerrar']:
        print("Encerrado")
        return 0

    resposta = answers_user_question(
        user_question=user_input,
        vectorizer=vectorizer,
        matrix_X=X,
        faq_answers=respostas
    )
    
    return resposta
