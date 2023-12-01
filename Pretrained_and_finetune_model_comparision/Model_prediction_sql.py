import mysql.connector
from class_predefined import OpenIEExtractor
from class_custom_train1 import CustomBertModel
import pandas as pd
import os
import json

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


pretrained_model = OpenIEExtractor()
finetuned_model = CustomBertModel(model_name="bert-base-uncased", num_labels=4, checkpoint_path='version_0/version_0/checkpoints/epoch=1-step=356.ckpt')

with open('tweets.json', 'r') as file:
    tweets = json.load(file)

for sentence in tweets:

    prediction_pretrained = pretrained_model.extract_relations(sentence)
    prediciton_finetune = finetuned_model.predict_relation(sentence)

    print(f"Predicted Relation for pretrained model: {prediction_pretrained}")
    print(f"Predicted Relation for finetune model: {prediciton_finetune}")

    insert_query = '''
            INSERT INTO SENTENCE_PREDICTION (input_text, finetune_prediction, predefined_prediction, sentence_labels)
            VALUES (%s, %s, %s, %s)
        '''
    values = (sentence, 
              prediciton_finetune, 
              prediction_pretrained, 
              "temp")

    cursor.execute(insert_query, values)

    connection.commit()
    
    
connection.close()

