## Document Intelligence Engine

A lightweight AI-powered document classification and extraction system built with Python and Streamlit. It automatically identifies the type of a document (Invoice, Receipt, or Purchase Order) and extracts key structured fields from recognized documents — with a built-in human feedback loop for continuous improvement.

---

##  Features

- ** Document Classification** — Classifies pasted document text into one of three categories:
  - `Invoice`
  - `Receipt`
  - `Purchase Order`
- ** Intelligent Data Extraction** — For Invoice documents, automatically extracts:
  - Total Amount
  - Date
  - Vendor Name
- ** Human-in-the-Loop Feedback** — Users can correct mislabeled predictions; feedback is saved to a CSV file for future retraining.
- ** Fast ML Pipeline** — Uses TF-IDF vectorization + Logistic Regression for efficient, interpretable text classification.
- ** Interactive Web UI** — Clean Streamlit interface — no front-end setup needed.

---

##  Project Structure

```
Document Intelligence Engine/
│
├── app.py               # Streamlit web app (main entry point)
├── classifier.py        # Model training script (TF-IDF + Logistic Regression)
├── extractor.py         # Regex-based field extractor for Invoice documents
├── feedback.py          # Saves user-corrected labels to corrected_labels.csv
│
├── classifier.pkl       # Pre-trained classification model (serialized)
├── vectorizer.pkl       # Pre-trained TF-IDF vectorizer (serialized)
│
├── data/
│   ├── invoices/        # Training text samples for Invoice class
│   ├── receipts/        # Training text samples for Receipt class
│   └── purchase_orders/ # Training text samples for Purchase Order class
│
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

##  Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Swayam234/document-intelligence-engine.git
cd document-intelligence-engine
```

### 2. Create & Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Make sure your training data exists inside the `data/` subfolders, then run:

```bash
python classifier.py
```

This generates `classifier.pkl` and `vectorizer.pkl` in the project root.

### 5. Launch the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## How to Use

1. **Paste** any document text into the text area.
2. Click **"Classify"** — the predicted document type will appear.
3. If the document is classified as an **Invoice**, extracted fields (Amount, Date, Vendor) are shown automatically.
4. If the prediction is **wrong**, type the correct label in the input box and click **"Submit Feedback"**.
   - Corrections are saved to `corrected_labels.csv` for future retraining.

---

##  How It Works

```
Raw Text Input
      │
      ▼
TF-IDF Vectorizer  ──►  Logistic Regression Classifier  ──►  Predicted Label
                                                                    │
                                               ┌────────────────────┘
                                               │
                                    ┌──────────▼──────────┐
                                    │  "Invoice" detected? │
                                    └──────────┬──────────┘
                                               │ Yes
                                               ▼
                                    Regex Extractor (extractor.py)
                                    ► Amount, Date, Vendor
```

| Component         | Technology                        |
|-------------------|-----------------------------------|
| UI Framework      | Streamlit                         |
| ML Model          | Scikit-learn (Logistic Regression)|
| Text Features     | TF-IDF Vectorization              |
| Field Extraction  | Python `re` (Regex)               |
| Feedback Storage  | Pandas + CSV                      |
| Model Persistence | Joblib                            |

---

##  Dependencies

| Package        | Purpose                              |
|----------------|--------------------------------------|
| `streamlit`    | Web application UI                   |
| `scikit-learn` | ML model training & inference        |
| `joblib`       | Model serialization / loading        |
| `pandas`       | Feedback data handling               |
| `pytesseract`  | OCR support (for image-based docs)   |
| `pdf2image`    | PDF to image conversion              |
| `Pillow`       | Image processing                     |

Install all at once:

```bash
pip install -r requirements.txt
```

---

##  Retraining the Model

After collecting enough feedback corrections in `corrected_labels.csv`:

1. Incorporate corrected samples into the appropriate `data/` subfolder.
2. Re-run `python classifier.py` to retrain and overwrite the `.pkl` files.
3. Restart the Streamlit app.


## Author

**Swayam** — [@Swayam234](https://github.com/Swayam234)
