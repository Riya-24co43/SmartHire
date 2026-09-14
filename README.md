# SmartHire — Resume-to-Job Matching & Career Guidance Engine

SmartHire is a machine learning-based career guidance system that analyzes a user's resume and provides relevant career and job recommendations.

The system combines **Natural Language Processing (NLP), supervised learning, unsupervised learning, TF-IDF, cosine similarity, K-Means clustering, NMF topic modeling, and skill-gap analysis** to help users understand their career category and identify suitable job opportunities.

## Features

* Resume upload in PDF format
* Automatic resume text extraction
* Resume career category prediction
* Top 10 job recommendations
* Resume-to-job similarity matching
* Job match score
* Job clustering using K-Means
* Job topic identification using NMF topic modeling
* Job fit prediction
* Skill-gap analysis
* Interactive Streamlit interface

## System Workflow

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Preprocessing
    ↓
TF-IDF
    ↓
Career Classification
    ↓
Job Recommendation
    ↓
Similarity Matching
    ↓
┌───────────────────┬───────────────────┬───────────────────┐
│                   │                   │                   │
Job Clustering   Topic Modeling    Fit Prediction
│                   │                   │                   │
└───────────────────┴───────────────────┴───────────────────┘
                         ↓
                  Skill Gap Analysis
```

## Machine Learning Components

### 1. Resume Classification

A **TF-IDF vectorizer** and **Logistic Regression** classifier are used to predict the career category of a resume.

The resume dataset contains multiple professional categories.

Model evaluation includes:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

The current classifier achieved approximately **65.59% test accuracy**.

### 2. Job Recommendation

Job listings are converted into TF-IDF vectors.

**Cosine similarity** is used to compare the uploaded resume with available job listings and identify the most similar jobs.

The system displays the **Top 10 recommended jobs** along with their similarity-based match scores.

### 3. Job Clustering

**K-Means clustering** is used to group jobs based on their textual characteristics.

**Truncated SVD** is used for dimensionality reduction before clustering, and **PCA** is used to visualize the resulting clusters.

### 4. Topic Modeling

**Non-Negative Matrix Factorization (NMF)** is used to identify major topics within job descriptions.

The system identifies eight job topics:

1. Sales & Business Development
2. Management & Operations
3. BPO & Customer Support
4. SAP & Enterprise Consulting
5. Software Development
6. Data Science & Analytics
7. Digital Marketing & Media
8. Software Testing & Quality Engineering

### 5. Fit Prediction

A **Random Forest classifier** predicts whether a recommended job is a suitable fit for the uploaded resume.

The predictor uses two main features:

* Text similarity
* Skill match

### 6. Skill Gap Analysis

The system compares the skills mentioned in the resume with the skills required by recommended jobs.

It displays:

* Skills found in the resume
* Skills that can be improved

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* PyPDF2
* Joblib
* Matplotlib
* Streamlit
* Jupyter Notebook
* Anaconda

## Project Structure

```text
SmartHire/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│       ├── cleaned_resumes.csv
│       └── README.md
│
├── models/
│   ├── resume_classifier.pkl
│   ├── resume_tfidf.pkl
│   ├── job_tfidf.pkl
│   ├── job_matrix.pkl
│   ├── job_svd.pkl
│   ├── job_kmeans.pkl
│   ├── fit_predictor.pkl
│   ├── topic_tfidf.pkl
│   └── nmf_topic_model.pkl
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_job_recommendation.ipynb
│   ├── 03_job_clustering.ipynb
│   ├── 04_fit_predictor.ipynb
│   ├── 05_topic_modeling.ipynb
│   └── README.md
│
├── .gitignore
└── README.md
```

> **Note:** The large `cleaned_jobs.csv` file is not included in the repository because it is approximately 80 MB.

## Datasets

The project uses:

* Resume dataset for resume classification
* Job listing dataset for job recommendation, clustering, and topic modeling

The original raw datasets are not included in this repository because of their large size and the number of individual resume files.

The processed job dataset is also excluded because of its large file size.

To run the application locally, place the processed job dataset at:

```text
data/processed/cleaned_jobs.csv
```

The processed job dataset can be reproduced using:

```text
notebooks/01_data_preparation.ipynb
```

## Installation

Install the required Python libraries using Anaconda Prompt:

```bash
pip install pandas numpy scikit-learn streamlit PyPDF2 joblib matplotlib openpyxl
```

The project can also be run using an Anaconda environment with the required packages installed.

## Running the Application

Open **Anaconda Prompt** and navigate to the application folder:

```bash
cd Desktop\Smarthire\app
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

Upload a resume in **PDF format** to view the predictions and recommendations.

## Application Output

After uploading a resume, SmartHire provides:

```text
Predicted Career Category
        ↓
Top 10 Recommended Jobs
        ↓
Match Score
        ↓
Job Cluster
        ↓
Job Topic
        ↓
Fit Prediction
        ↓
Skill Gap Analysis
```

## Project Goal

The goal of SmartHire is to provide an accessible machine learning-based career guidance system that helps users:

* Understand their career category
* Discover relevant job opportunities
* Compare their resume with job requirements
* Identify missing or improvable skills
* Understand different job domains

## Future Scope

Possible future improvements include:

* Multilingual resume support
* More advanced skill extraction
* Personalized learning recommendations
* Real-time job data integration through permitted APIs
* Improved job clustering
* Deep learning-based resume embeddings
* User profile and recommendation history
* Deployment as a cloud-based application

## License

This project is developed for academic and educational purposes.
# SmartHire — Resume-to-Job Matching & Career Guidance Engine

SmartHire is a machine learning-based career guidance system that analyzes a user's resume and provides relevant career and job recommendations.

The system combines **Natural Language Processing (NLP), supervised learning, unsupervised learning, TF-IDF, cosine similarity, K-Means clustering, NMF topic modeling, and skill-gap analysis** to help users understand their career category and identify suitable job opportunities.

## Features

* Resume upload in PDF format
* Automatic resume text extraction
* Resume career category prediction
* Top 10 job recommendations
* Resume-to-job similarity matching
* Job match score
* Job clustering using K-Means
* Job topic identification using NMF topic modeling
* Job fit prediction
* Skill-gap analysis
* Interactive Streamlit interface

## System Workflow

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Preprocessing
    ↓
TF-IDF
    ↓
Career Classification
    ↓
Job Recommendation
    ↓
Similarity Matching
    ↓
┌───────────────────┬───────────────────┬───────────────────┐
│                   │                   │                   │
Job Clustering   Topic Modeling    Fit Prediction
│                   │                   │                   │
└───────────────────┴───────────────────┴───────────────────┘
                         ↓
                  Skill Gap Analysis
```

## Machine Learning Components

### 1. Resume Classification

A **TF-IDF vectorizer** and **Logistic Regression** classifier are used to predict the career category of a resume.

The resume dataset contains multiple professional categories.

Model evaluation includes:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

The current classifier achieved approximately **65.59% test accuracy**.

### 2. Job Recommendation

Job listings are converted into TF-IDF vectors.

**Cosine similarity** is used to compare the uploaded resume with available job listings and identify the most similar jobs.

The system displays the **Top 10 recommended jobs** along with their similarity-based match scores.

### 3. Job Clustering

**K-Means clustering** is used to group jobs based on their textual characteristics.

**Truncated SVD** is used for dimensionality reduction before clustering, and **PCA** is used to visualize the resulting clusters.

### 4. Topic Modeling

**Non-Negative Matrix Factorization (NMF)** is used to identify major topics within job descriptions.

The system identifies eight job topics:

1. Sales & Business Development
2. Management & Operations
3. BPO & Customer Support
4. SAP & Enterprise Consulting
5. Software Development
6. Data Science & Analytics
7. Digital Marketing & Media
8. Software Testing & Quality Engineering

### 5. Fit Prediction

A **Random Forest classifier** predicts whether a recommended job is a suitable fit for the uploaded resume.

The predictor uses two main features:

* Text similarity
* Skill match

### 6. Skill Gap Analysis

The system compares the skills mentioned in the resume with the skills required by recommended jobs.

It displays:

* Skills found in the resume
* Skills that can be improved

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* PyPDF2
* Joblib
* Matplotlib
* Streamlit
* Jupyter Notebook
* Anaconda

## Project Structure

```text
SmartHire/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│       ├── cleaned_resumes.csv
│       └── README.md
│
├── models/
│   ├── resume_classifier.pkl
│   ├── resume_tfidf.pkl
│   ├── job_tfidf.pkl
│   ├── job_matrix.pkl
│   ├── job_svd.pkl
│   ├── job_kmeans.pkl
│   ├── fit_predictor.pkl
│   ├── topic_tfidf.pkl
│   └── nmf_topic_model.pkl
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_job_recommendation.ipynb
│   ├── 03_job_clustering.ipynb
│   ├── 04_fit_predictor.ipynb
│   ├── 05_topic_modeling.ipynb
│   └── README.md
│
├── .gitignore
└── README.md
```

> **Note:** The large `cleaned_jobs.csv` file is not included in the repository because it is approximately 80 MB.

## Datasets

The project uses:

* Resume dataset for resume classification
* Job listing dataset for job recommendation, clustering, and topic modeling

The original raw datasets are not included in this repository because of their large size and the number of individual resume files.

The processed job dataset is also excluded because of its large file size.

To run the application locally, place the processed job dataset at:

```text
data/processed/cleaned_jobs.csv
```

The processed job dataset can be reproduced using:

```text
notebooks/01_data_preparation.ipynb
```

## Installation

Install the required Python libraries using Anaconda Prompt:

```bash
pip install pandas numpy scikit-learn streamlit PyPDF2 joblib matplotlib openpyxl
```

The project can also be run using an Anaconda environment with the required packages installed.

## Running the Application

Open **Anaconda Prompt** and navigate to the application folder:

```bash
cd Desktop\Smarthire\app
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

Upload a resume in **PDF format** to view the predictions and recommendations.

## Application Output

After uploading a resume, SmartHire provides:

```text
Predicted Career Category
        ↓
Top 10 Recommended Jobs
        ↓
Match Score
        ↓
Job Cluster
        ↓
Job Topic
        ↓
Fit Prediction
        ↓
Skill Gap Analysis
```

## Project Goal

The goal of SmartHire is to provide an accessible machine learning-based career guidance system that helps users:

* Understand their career category
* Discover relevant job opportunities
* Compare their resume with job requirements
* Identify missing or improvable skills
* Understand different job domains

## Future Scope

Possible future improvements include:

* Multilingual resume support
* More advanced skill extraction
* Personalized learning recommendations
* Real-time job data integration through permitted APIs
* Improved job clustering
* Deep learning-based resume embeddings
* User profile and recommendation history
* Deployment as a cloud-based application

## License

This project is developed for academic and educational purposes.
