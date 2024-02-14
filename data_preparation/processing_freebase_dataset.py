import json
import pandas as pd

def process_json_to_csv(json_file_path, csv_file_path):
    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extract 'Questions' part from the data
    questions = data['Questions']

    # Extract 'RawQuestion' and the first 'AnswersName' for each question
    qa_pairs = []
    for item in questions:
        if 'Parses' in item and item['Parses']:
            first_parse = item['Parses'][0]  # Assuming the first parse contains the desired answer
            if 'Answers' in first_parse and first_parse['Answers']:
                answer = first_parse['Answers'][0]['AnswersName'][0]  # Taking the first answer name
                qa_pairs.append({"Question": item['RawQuestion'], "Answer": answer})

    # Convert to DataFrame
    df = pd.DataFrame(qa_pairs)

    # Save to CSV
    df.to_csv(csv_file_path, index=False)

# Define file paths
json_file_path = 'FreebaseQA-train.json'  # Update this path
csv_file_path = 'data/freebase_qa.csv'  # Update this path

# Call the function
process_json_to_csv(json_file_path, csv_file_path)

print(f"Dataset has been processed and saved to {csv_file_path}")
