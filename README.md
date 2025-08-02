
# 🧠 ATS Resume Score

**ATS Resume Score** is a simple web application that analyzes how well a candidate's resume matches a job description using AI. It helps users optimize their resumes for Applicant Tracking Systems (ATS) by computing a semantic similarity score.

Built with **Flask**, **Sentence Transformers**, and **PyMuPDF**, this tool is ideal for job seekers who want to tailor their resumes more effectively.

---

## 🚀 Features

- ✅ Upload resume in **PDF** format
- ✅ Paste job description text
- ✅ Calculates similarity using **AI (NLP model)**
- ✅ Displays a **match score** as a percentage
- ✅ Lightweight and easy to run locally



## 🛠️ Technologies Used

| Purpose               | Tool/Library             |
|-----------------------|--------------------------|
| Web Framework         | Flask                    |
| NLP Model             | SentenceTransformers     |
| Text Similarity       | Scikit-learn (Cosine)    |
| PDF Text Extraction   | PyMuPDF (`fitz`)         |
| Frontend              | HTML + Jinja2            |

---


---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https:https://github.com/hemanathansuriya/ATS-RESUME-SCORE.git
cd ATS-Resume-Score

 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

If you don’t have a requirements.txt, use this:
pip install flask sentence-transformers pymupdf scikit-learn

▶️ Run the App
python app.py

Open your browser and visit: http://127.0.0.1:5000

🧪 How It Works
Upload a PDF resume.

Paste the job description.

The system uses a transformer model to generate embeddings.

It calculates the cosine similarity between resume and job text.

You get a score (0–100%) indicating how well the resume fits the job.

💡 Future Enhancements
Support for .docx resumes

Highlight missing keywords or skills

Mobile-friendly UI

ATS optimization tips

🤝 Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to open an issue.

                        THANKYOU
