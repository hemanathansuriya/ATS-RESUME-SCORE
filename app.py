import os
import fitz
from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
from werkzeug.utils import secure_filename
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config["upload_folder"] = "uploads"
os.makedirs(app.config["upload_folder"],exist_ok=True)

model = SentenceTransformer( "all-mpnet-base-v2")

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = text+page.get_text()
    return text.strip()

def cosines_similarity_score(resume_text, job_description_text):
    embeddings = model.encode([resume_text, job_description_text])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    return round(similarity[0][0]*100, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "resume" not in request.files:
            return "No file uploaded", 400
        file = request.files["resume"]
        job_desc = request.form.get("job_doc")

        if file.filename == "" or not job_desc:
            return "No file or job description provided", 400
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["upload_folder"], filename)
        file.save(file_path)

        resume_text = extract_text_from_pdf(file_path)
        score = cosines_similarity_score(resume_text, job_desc)
        return render_template("index.html", score=score)
    return render_template("index.html", score=None)
    
if __name__ == "__main__":
    app.run(debug=True) 
    