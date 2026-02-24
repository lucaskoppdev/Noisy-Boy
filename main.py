from user_vectorizer_handler import find_best_answer_for_user_input
from agent import agent_refinery

def main_function(user_input):
    vector_output = find_best_answer_for_user_input(user_input)

    final_answer = agent_refinery(vector_output)

    return final_answer
    
