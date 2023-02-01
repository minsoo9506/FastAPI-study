import os
from typing import List, Optional, Tuple

import joblib
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


class PredictionInput(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    text: str


class NewsgroupsModel:
    model: Optional[Pipeline]
    targets: Optional[List[str]]

    def load_model(self):
        model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
        loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file)
        self.model, self.targets = loaded_model

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        if not self.model or not self.targets:
            raise RuntimeError("model is not loaded")
        prediction = self.model.predict([input.text])
        category = self.targets[prediction[0]]
        return PredictionOutput(category=category)


app = FastAPI()
newgroups_model = NewsgroupsModel()


@app.post("/prediction")
async def prediction(
    output: PredictionOutput = Depends(newgroups_model.predict),
) -> PredictionOutput:
    return output


@app.on_event("startup")
async def startup():
    newgroups_model.load_model()