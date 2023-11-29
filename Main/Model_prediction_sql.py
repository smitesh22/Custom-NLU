import mysql.connector
from class_predefined import OpenIEExtractor
import pandas as pd
import os

# Set the CORENLP_HOME environment variable
os.environ['CORENLP_HOME'] = '/home/smitesh22/.stanfordnlp_resources/stanford-corenlp-4.5.3'

connection = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Admin",
    database="name_entity_recognition"
)

cursor = connection.cursor()

if connection.is_connected():
    print('Connected Successfully')
else:
    print('Failed to connect')
    exit()

table_exists_query = "SHOW TABLES LIKE 'SENTENCE_PREDICTION'"
cursor.execute(table_exists_query)

if not cursor.fetchone():
    table_creation_query = """
       CREATE TABLE SENTENCE_PREDICTION (
            id INT AUTO_INCREMENT PRIMARY KEY,
            input_text TEXT,
            finetune_prediction VARCHAR(255),
            predefined_prediction VARCHAR(255),
            sentence_labels TEXT
        );
        """
    
    cursor.execute(table_creation_query)
    cursor.fetchall()
    
    print("Predictions Table created")
    connection.commit()
else:
    print("Table exists")


obj = OpenIEExtractor()

df = pd.read_csv("combination_spin.csv")
for sentence in df.head(50).iterrows():

    prediction = obj.extract_relations(sentence[1].sentences)
    print(f"Predicted Relation: {prediction}")

    
    insert_query = '''
            INSERT INTO SENTENCE_PREDICTION (input_text, predefined_prediction, sentence_labels)
            VALUES (%s, %s, %s)
        '''
    values = (sentence[1].sentences, prediction, sentence[1].relations)

    cursor.execute(insert_query, values)

    connection.commit()
    print(f"Data for sentence '{sentence[1].sentences}' inserted successfully.")
    
connection.close()
