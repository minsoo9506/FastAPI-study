import os
from typing import List, Tuple

import joblib
from sklearn.pipeline import Pipeline

# Load the model
model_file_path = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file_path)
model, target_names = loaded_model

# prediction
p = model.predict(["computer cpu memory ram"])
print(target_names[p[0]])

# 결과
# comp.sys.mac.hardware
