import streamlit as st
import joblib
from extractor import extract_invoice
from feedback import save_feedback

model = joblib.load("classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Document Intelligence Engine")

text = st.text_area("Paste document text")

if st.button("Classify"):

    X = vectorizer.transform([text])

    prediction = model.predict(X)[0]

    st.success(f"Predicted Type: {prediction}")

    if prediction == "Invoice":
        st.write(extract_invoice(text))

    corrected = st.text_input(
        "Correct label if wrong"
    )

    if st.button("Submit Feedback"):
        save_feedback(
            "manual",
            prediction,
            corrected
        )
        st.success("Feedback Saved")