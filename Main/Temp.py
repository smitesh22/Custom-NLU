from class_custom_train1 import CustomBertModel

obj2 = CustomBertModel(model_name="bert-base-uncased", num_labels=4, checkpoint_path='version_0/version_0/checkpoints/epoch=1-step=356.ckpt')
sentence = 'The Colosseum is an ancient amphitheater in Rome.'
predicted_relation = obj2.predict_relation(sentence)
print(f"Predicted Relation: {predicted_relation}")