import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

docs = []
labels = []

folders = {
    "invoices": "Invoice",
    "receipts": "Receipt",
    "purchase_orders": "PurchaseOrder"
}

for folder, label in folders.items():

    path = os.path.join("data", folder)

    for file in os.listdir(path):

        with open(
            os.path.join(path, file),
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        docs.append(text)
        labels.append(label)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(docs)

model = LogisticRegression(max_iter=1000)

model.fit(X, labels)

joblib.dump(model, "classifier.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Training completed.")