from sklearn.model_selection import train_test_split
from preprocessing import *
import json

# reading the JSON data using json.load()
file = 'train-v2.0.json'
# Load the dataset from a json file
with open(file, 'r') as f:
    dataset = json.load(f)

questions = []
answers = []
# Access the data in the dataset
for example in dataset['data']:
    # Each example consists of a context (the article text) and a list of questions and answers
    context = example['paragraphs']
    for paragraph in example['paragraphs']:
        context = paragraph['context']
        for qa in paragraph['qas']:
            question = qa['question']
            if qa['answers']:  # Check if the answers list is not empty
                answer = qa['answers'][0]['text']  # There may be multiple answers, but we'll just use the first one
            else:
                answer = None
            questions.append(question)
            answers.append(answer)
#Tokenize the text
questions_tokens, answers_tokens = Preprocessing.tokenize_text(questions, answers)    

#Create the vocabulary       
questions_numerical = Preprocessing.create_vocab(questions_tokens, answers_tokens)

# Split the data into a training set and a testing set
questions_train, questions_test, answers_train, answers_test = train_test_split(questions_numerical, answers_numerical, test_size=0.2)

