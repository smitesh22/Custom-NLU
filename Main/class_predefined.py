from openie import StanfordOpenIE

class OpenIEExtractor:
    def __init__(self):
        self.properties = {
            'openie.affinity_probability_cap': 2 / 3,
            # 'openie.server_url': 'http://corenlp.run:80/process',
        }
        self.client = StanfordOpenIE(properties=self.properties)

    def extract_relations(self, text):
        print('Text: %s.' % text)
        for triple in self.client.annotate(text):
            # Extract only the relation value
            relation_value = triple['relation']
            #print('relation:', relation_value)
            return relation_value

# Example usage
obj1 = OpenIEExtractor()
text = '[E1]Rocky Subramanian[/E1], SVP & MD of [E2]SAP[/E2], talks us through the benefits of human and tech augmentation in the manufacturing industry   .'
#text='Amazon CEO Jeff Bezos stepped down from his position.'
#obj1.extract_relations(text)
prediction1=obj1.extract_relations(text)
print(f"Predicted Relation: {prediction1}")
