import streamlit as st
import pandas as pd
import joblib
import re
import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity

st.markdown("""
<style>
.stApp {
    background: #faf8ff;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #6d28d9;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #7c6f91;
    margin-bottom: 30px;
}

h1, h2, h3 {
    color: #5b21b6;
}

[data-testid="stFileUploader"] {
    background: #ffffff;
    padding: 25px;
    border-radius: 18px;
    border: 2px dashed #a78bfa;
    box-shadow: 0px 4px 15px rgba(109, 40, 217, 0.10);
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

.stButton > button {
    background: #7c3aed;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #6d28d9;
    color: white;
}

hr {
    border: none;
    height: 2px;
    background: #e9d5ff;
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">SmartHire</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Resume-to-Job Matching & Career Guidance Engine</div>',
    unsafe_allow_html=True
)

st.divider()

classifier = joblib.load("../models/resume_classifier.pkl")
resume_tfidf = joblib.load("../models/resume_tfidf.pkl")
job_tfidf = joblib.load("../models/job_tfidf.pkl")
job_matrix = joblib.load("../models/job_matrix.pkl")
fit_predictor = joblib.load("../models/fit_predictor.pkl")
job_svd = joblib.load("../models/job_svd.pkl")
job_kmeans = joblib.load("../models/job_kmeans.pkl")
topic_tfidf = joblib.load("../models/topic_tfidf.pkl")
nmf_model = joblib.load("../models/nmf_topic_model.pkl")

jobs = pd.read_csv("../data/processed/cleaned_jobs.csv")

cluster_names = {
    0: "Sales & Business Development",
    1: "Technology & IT Consulting",
    2: "General & Other Professional Roles"
}

topic_names = {
    1: "Sales & Business Development",
    2: "Management & Operations",
    3: "BPO & Customer Support",
    4: "SAP & Enterprise Consulting",
    5: "Software Development",
    6: "Data Science & Analytics",
    7: "Digital Marketing & Media",
    8: "Software Testing & Quality Engineering"
}

def extract_resume_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9+#]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_skills_from_job(job_skills):
    skills = str(job_skills).split(",")
    skills = [clean_text(skill) for skill in skills]
    skills = [skill for skill in skills if skill]
    skills = list(dict.fromkeys(skills))
    return skills

def calculate_skill_match(resume_text, job_skills):
    resume_text = clean_text(resume_text)
    required_skills = get_skills_from_job(job_skills)

    if len(required_skills) == 0:
        return 0

    matched_skills = 0

    for skill in required_skills:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, resume_text):
            matched_skills += 1

    skill_match = matched_skills / len(required_skills)

    return skill_match

def find_skill_gap(resume_text, job_skills):
    resume_text = clean_text(resume_text)

    required_skills = get_skills_from_job(job_skills)

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, resume_text):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills

def predict_job_topic(job_text):
    topic_vector = topic_tfidf.transform([job_text])

    topic_scores = nmf_model.transform(topic_vector)[0]

    topic_number = topic_scores.argmax() + 1

    topic_name = topic_names.get(
        topic_number,
        "Other Professional Roles"
    )

    return topic_number, topic_name

st.header("Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume in PDF format",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_resume_text(uploaded_file)

    if resume_text.strip() == "":
        st.error("Could not extract text from the resume.")

    else:

        st.header("Career Prediction")

        resume_vector = resume_tfidf.transform([resume_text])

        predicted_category = classifier.predict(
            resume_vector
        )[0]

        st.success(
            "Predicted Career Category: "
            + predicted_category
        )

        st.header("Recommended Jobs")

        job_vector = job_tfidf.transform([resume_text])

        similarity_scores = cosine_similarity(
            job_vector,
            job_matrix
        )[0]

        top_10_indices = similarity_scores.argsort()[-10:][::-1]

        recommendations = jobs.iloc[top_10_indices].copy()

        recommendations["match_score"] = (
            similarity_scores[top_10_indices] * 100
        )

        recommendations = recommendations.reset_index(drop=True)

        recommendations.index = recommendations.index + 1

        for index, row in recommendations.iterrows():

            st.subheader(
                str(index)
                + ". "
                + str(row["job_role"])
            )

            company = row["company"]

            if pd.isna(company):
                company = "Not Available"

            location = row["location"]

            if pd.isna(location):
                location = "Not Available"

            st.write(
                "**Company:** "
                + str(company)
            )

            st.write(
                "**Location:** "
                + str(location)
            )

            st.write(
                "**Match Score:** "
                + str(round(row["match_score"], 2))
                + "%"
            )

            st.write(
                "**Required Skills:** "
                + str(row["key_skills"])
            )

            job_index = top_10_indices[index - 1]

            job_vector_for_cluster = job_matrix[job_index]

            job_reduced = job_svd.transform(
                job_vector_for_cluster
            )

            cluster = job_kmeans.predict(
                job_reduced
            )[0]

            cluster_name = cluster_names.get(
                cluster,
                "Other"
            )

            st.write(
                "**Job Cluster:** "
                + cluster_name
            )

            job_text = str(row["job_text"])

            topic_number, topic_name = predict_job_topic(
                job_text
            )

            st.write(
                "**Job Topic:** "
                + topic_name
            )

            text_similarity = similarity_scores[job_index]

            skill_match = calculate_skill_match(
                resume_text,
                row["key_skills"]
            )

            fit_input = [
                [
                    text_similarity,
                    skill_match
                ]
            ]

            fit_prediction = fit_predictor.predict(
                fit_input
            )[0]

            if fit_prediction == 1:

                st.success(
                    "Fit Prediction: Suitable"
                )

            else:

                st.warning(
                    "Fit Prediction: Not Suitable"
                )

            st.divider()

        st.header("Skill Gap Analysis")

        all_matched_skills = []

        all_missing_skills = []

        for _, row in recommendations.iterrows():

            matched_skills, missing_skills = find_skill_gap(
                resume_text,
                row["key_skills"]
            )

            all_matched_skills.extend(
                matched_skills
            )

            all_missing_skills.extend(
                missing_skills
            )

        all_matched_skills = list(
            dict.fromkeys(
                all_matched_skills
            )
        )

        all_missing_skills = list(
            dict.fromkeys(
                all_missing_skills
            )
        )

        st.subheader(
            "Skills Found in Your Resume"
        )

        if all_matched_skills:

            st.write(
                ", ".join(
                    all_matched_skills[:20]
                )
            )

        else:

            st.write(
                "No matching skills found."
            )

        st.subheader(
            "Skills to Improve"
        )

        if all_missing_skills:

            st.write(
                ", ".join(
                    all_missing_skills[:20]
                )
            )

        else:

            st.write(
                "No major skill gaps found."
            )
