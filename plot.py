import json
import matplotlib.pyplot as plt

def load_results(file_name='results.json'):
    """Load results from a JSON file."""
    with open(file_name, 'r') as f:
        return json.load(f)

def plot_metrics(results):
    """Plot average metrics for each model based on results."""
    models = list(results.keys())
    metrics = ['response_time', 'tokens_used', 'response_length']
    
    avg_metrics = {metric: [] for metric in metrics}

    for model in models:
        # Aggregate metrics
        avg_time = sum(r["response_time"] for r in results[model]) / len(results[model])
        avg_tokens = sum(r["tokens_used"] for r in results[model]) / len(results[model])
        avg_length = sum(r["response_length"] for r in results[model]) / len(results[model])

        # Store averages in the dictionary
        avg_metrics['response_time'].append(avg_time)
        avg_metrics['tokens_used'].append(avg_tokens)
        avg_metrics['response_length'].append(avg_length)

    # Define a list of colors for the plots
    colors = ['blue', 'orange', 'green']

    # Creating separate bar graphs for each metric
    for i, metric in enumerate(metrics):
        plt.figure(figsize=(10, 6))
        plt.bar(models, avg_metrics[metric], color=colors[i % len(colors)], alpha=0.7, label=f'Average {metric.replace("_", " ").title()}')
        plt.title(f'Average {metric.replace("_", " ").title()} by Model')
        plt.xlabel('Models')
        plt.ylabel(metric.replace("_", " ").title())
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=15)  # Rotate model names if necessary
        plt.legend()
        plt.tight_layout()
        
        # Save the figure
        plt.savefig(f'{metric}_by_model.png')  # Save each metric plot as a separate file
        plt.close()  # Close the figure to free up memory

if __name__ == "__main__":
    results = load_results()  # Load results from JSON
    plot_metrics(results)  # Plot the metrics