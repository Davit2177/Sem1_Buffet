import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

with open("./Buffet_Poole26/Python/001_Final/intents.json") as file:
    data = json.load(file)["intents"]
    
x = [] # patterns
y = [] # tags

for intent in data: 
    for pattern in intent["patterns"]:
        x.append(pattern)
        y.append(intent["tag"])
        
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("clasifier", MultinomialNB())
])

model.fit(x,y)

joblib.dump(model,"./Buffet_Poole26/Python/001_Final/intents.pkl")

print("Job don!")




