import mysql.connector
import os
import pandas as pd

# Set the CORENLP_HOME environment variable
os.environ['CORENLP_HOME'] = '/home/smitesh22/.stanfordnlp_resources/stanford-corenlp-4.5.3'

#connection object
connection = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Admin",
    database="name_entity_recognition"
)

cursor = connection.cursor()

#check database connection
if connection.is_connected():
    print('Connected Successfully')
else:
    print('Failed to connect')
    exit()

df = pd.read_csv("pretrained_predictions_cleaned.csv")

for index, row in df.iterrows():
    cursor.execute(f"UPDATE SENTENCE_PREDICTION SET pretrained_prediction_cleaned = %s WHERE id = %s", (row["predefined_cleaned_prediction"], row['id']))

connection.commit()

query = "SELECT * FROM SENTENCE_PREDICTION;"
cursor.execute(query)

rows = cursor.fetchall()

column_names = [desc[0] for desc in cursor.description]

df = pd.DataFrame(rows, columns=column_names)

print("Finetune Accuracy: ",df.finetune_accuracy.sum()/len(df))

df.to_csv("temp.csv")
cursor.close()
connection.close()

