from fastapi import FastAPI, File , UploadFile, HTTPException
import numpy as np
import pandas as pd
from typing import Dict
import joblib
import uvicorn

app = FastAPI(title="Sepsis prediction api", 
              description=' this will predict sepsis'
)



MODEL_PATH = {
    'logistic_regression':'models/Logistic Regression_pipline.pkl',
    'random_forest':'models/Random Forest_pipline.pkl',
    'knn':'models/K-Nearest Neighbors_pipline.pkl'

}

#load the models
models = {}
for model, path in MODEL_PATH.items():
    try:
        models[model] = joblib.load(path)
    except Exception as e:
        raise RuntimeError(f'Failed to load model {model} from {path}.error{e}' )
    

@app.get('/')
async def st_endpoint():
    return{'message':"Welcome to Sepsis Prediction app"}


@app.post('/predict')
async def predicter(model : str, file: UploadFile = File(...)):
    '''Accept a model
       loads a file
       
       return a json with predictions for each row'''
    
    if model not in models:
        raise HTTPException(status_code=400, detail=f'Model not found')
    

    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading the file:{e}")
    
    required_features = models[model].n_features_in_
    if len(df.columns) != required_features:
        raise HTTPException(status_code=400, detail=f'the model expects{required_features} but file has {len(df.columns)}columns')
    

    #features = df.values
    selected_model = models[model]
    #predictions = model.predict(features)
    try:
        predictions = selected_model.predict(df)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error during predictions')


    results = {
        'model_used': model,
        'predictions': predictions.tolist()
    }

    return results


if __name__ == '__main__':
    uvicorn.run('mainapi:app', reload=True)