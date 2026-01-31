#Abstracao para testar como vai funcionar a deteccao das perguntas do usuario e afins
from sklearn.metrics.pairwise import cosine_similarity
from tf_idf_vectorizer import X, vectorizer, faq_respostas



def get_user_question():
    return input("Digite a sua pergunta -> ").strip()



def answers_user_question(
        user_question,
        vectorizer,
        question_vectors,
        faq_answers
):

    vectorized_question = vectorizer.transform([user_question.strip()])

    similarity = cosine_similarity(vectorized_question, question_vectors)

    scores = similarity[0]

    better_index = scores.argmax()

    better_score = scores[better_index]

    if better_score >= 0.5:
        answer = faq_answers[better_index]
    else:
        print(better_score)
        print(better_index)
        answer = "Nao foi encontrada uma resposta satisfatoria para essa pergunta, pergunte novamente de outra forma!"
    

    return answer


#loop de teste gambiarra
print("==>Digite sair para encerrar<==")
while True:
    pergunta = get_user_question()

    if pergunta in ['sair', 'exit', 'encerrar']:
        print("Encerrado")
        break

    resposta = answers_user_question(
        user_question=pergunta,
        vectorizer=vectorizer,
        question_vectors=X,
        faq_answers=faq_respostas
    )

    print("Resposta: ", resposta)

