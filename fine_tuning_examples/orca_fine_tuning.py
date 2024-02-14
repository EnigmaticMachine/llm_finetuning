import logging
import pandas as pd
import yaml
from ludwig.api import LudwigModel
import matplotlib.pyplot as plt

# Load the question-answer pairs from the CSV file
csv_file_path = 'data/freebase_qa.csv'  # Update the path to your CSV file
df = pd.read_csv(csv_file_path)

def plot_sequence_lengths(df):
    sequence_lengths = df['Question'].str.len() + df['Answer'].str.len()
    plt.hist(sequence_lengths, bins=30)
    plt.xlabel('Sequence Length')
    plt.ylabel('Count')
    plt.title('Distribution of Text Sequence Lengths')
    plt.savefig('plot_sequence_lengths.png')
    too_long = sequence_lengths[sequence_lengths > 512].index.tolist()  # adjust threshold as needed
    return too_long

too_long_indices = plot_sequence_lengths(df)
print(f"Entries longer than the threshold: {too_long_indices}")

config = yaml.safe_load(
    """
    input_features:
        - name: Question
          type: text
    output_features:
        - name: Answer
          type: text
    model_type: llm
    preprocessing:
        max_sequence_length: 18
    generation:
        temperature: 0.1
        top_p: 0.75
        top_k: 40
        num_beams: 4
        max_new_tokens: 5
    base_model: microsoft/Orca-2-7b  # Update the base model if needed
    quantization:
        bits: 4
    adapter:
        type: lora
    trainer:
        type: finetune
        learning_rate: 0.0001
        batch_size: 1
        gradient_accumulation_steps: 16
        epochs: 3
        learning_rate_scheduler:
            warmup_fraction: 0.01
    """
)

model = LudwigModel(config, logging_level=logging.INFO)

# Train the model
train_stats, preprocessed_data, output_directory = model.train(
    dataset=df, experiment_name="simple_experiment", model_name="simple_model", skip_save_processed_input=True
)

model.save("results")

# Assuming you want to predict after training
# You would need to split your data into training and test sets for this part
# preds = model.predict(test_dataframe)
