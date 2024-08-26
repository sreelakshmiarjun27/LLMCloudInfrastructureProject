import time
import json
from app import get_answer, preprocess_text

def get_model_response(model, question):
    start_time = time.time()
    answer, _ = get_answer(question)  # Assuming get_answer returns the answer and context
    end_time = time.time()
    response_time = end_time - start_time
    return answer, response_time

def compare_models(questions, models):
    results = {model: [] for model in models}

    for question in questions:
        for model in models:
            answer, response_time = get_model_response(model, question)
            results[model].append({
                "question": question,
                "answer": answer,
                "response_time": response_time,
                "tokens_used": len(answer.split()),  # Tokens are the words in the answer
                "response_length": len(answer.split()),  # Response length in words
            })

    return results

if __name__ == "__main__":
    models = ["gpt-4o","text-davinci-003","text-davinci-002"]
    questions = [
        "What is the meter name for the service being charged?",
        "In which region is the meter located?",
        "What is the  price for the service period?"
    ]
    
    results = compare_models(questions, models)

    for model in models:
        avg_time = sum(r["response_time"] for r in results[model]) / len(results[model])
        avg_tokens_used = sum(r["tokens_used"] for r in results[model]) / len(results[model])
        avg_response_length = sum(r["response_length"] for r in results[model]) / len(results[model])

        print(f"\nModel: {model}")
        print(f"Average response time: {avg_time:.2f} seconds")
        print(f"Average tokens used: {avg_tokens_used:.2f}")
        print(f"Average response length: {avg_response_length:.2f} words")

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)