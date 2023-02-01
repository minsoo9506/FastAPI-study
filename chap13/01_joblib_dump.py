import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load some categories of newsgroups dataset
categories = [
    "soc.religion.christian",
    "talk.religion.misc",
    "comp.sys.mac.hardware",
    "sci.crypt",
]
newsgroups_training = fetch_20newsgroups(
    subset="train", categories=categories, random_state=0
)
newsgroups_testing = fetch_20newsgroups(
    subset="test", categories=categories, random_state=0
)

# Make the pipeline
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB(),
)

# Train the model
model.fit(newsgroups_training.data, newsgroups_training.target)

# Serialize the model and the target names
model_file_path = "chap13/newsgroups_model.joblib"
model_targets_tuple = (model, newsgroups_training.target_names)  # 모델과 타겟이름
joblib.dump(model_targets_tuple, model_file_path)  # dumping할 object와 저장경로
