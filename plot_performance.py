import matplotlib.pyplot as plt
import numpy as np
import json

def create_radar_chart(metrics, values, name='chatbot_performance.png'):
    # Number of variables
    num_vars = len(metrics)

    # Split the circle into even parts and save the angles
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Close the polygon by appending the start value to the end
    values += values[:1]
    angles += angles[:1]

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))

    # Draw the shape
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)

    # Set the labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics)

    # Add title
    plt.title("Chatbot Performance Metrics", size=20, y=1.1)

    # Add legend to show the scale
    plt.text(0.95, 0.95, "Scale: 0-100%", transform=ax.transAxes, ha='right', va='top')

    # Adjust the layout and save the figure
    plt.tight_layout()
    plt.savefig(name)
    print(f"Graph saved as {name}")

def plot_from_json(json_file='chatbot_results.json', output_file='chatbot_performance.png'):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    metrics = list(data['metrics'].keys())
    values = list(data['metrics'].values())
    
    create_radar_chart(metrics, values, output_file)

if __name__ == "__main__":
    plot_from_json()