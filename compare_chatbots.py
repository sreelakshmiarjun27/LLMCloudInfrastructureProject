import app as rag_chatbot  # Your existing RAG-based chatbot
import importlib
non_rag_chatbot = importlib.import_module("without RAG")  # The new non-RAG chatbot
from nltk.translate.bleu_score import sentence_bleu
import time
import json

def compare_chatbots(questions):
    results = []

    for question in questions:
        # RAG-based chatbot
        rag_start_time = time.time()
        rag_answer, rag_context = rag_chatbot.get_answer(question)
        rag_end_time = time.time()
        rag_response_time = rag_end_time - rag_start_time

        # Non-RAG chatbot
        non_rag_start_time = time.time()
        non_rag_answer, _ = non_rag_chatbot.get_answer(question)
        non_rag_end_time = time.time()
        non_rag_response_time = non_rag_end_time - non_rag_start_time

        # Calculate BLEU score (assuming RAG answer as reference)
        bleu_score = sentence_bleu([rag_answer.split()], non_rag_answer.split())

        results.append({
            'question': question,
            'rag_answer': rag_answer,
            'non_rag_answer': non_rag_answer,
            'rag_context': rag_context,
            'rag_response_time': rag_response_time,
            'non_rag_response_time': non_rag_response_time,
            'bleu_score': bleu_score
        })

    return results

def print_comparison(results):
    for result in results:
        print(f"Question: {result['question']}")
        print(f"RAG Answer: {result['rag_answer']}")
        print(f"Non-RAG Answer: {result['non_rag_answer']}")
        print(f"RAG Context: {result['rag_context'][:200]}...")  # Print first 200 characters
        print(f"RAG Response Time: {result['rag_response_time']:.2f} seconds")
        print(f"Non-RAG Response Time: {result['non_rag_response_time']:.2f} seconds")
        print(f"BLEU Score: {result['bleu_score']:.4f}")
        print("\n" + "="*50 + "\n")

def save_results_to_file(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    questions = [
        "What is cloud computing?",
        "How can I optimize my cloud costs?",
        "What are the summary of all resources being utilized under this billing account?",
        # Add more questions here
    ]

    results = compare_chatbots(questions)
    print_comparison(results)

    # Save results to a file
    save_results_to_file(results, 'chatbot_comparison_results.json')
    print("Results saved to chatbot_comparison_results.json")