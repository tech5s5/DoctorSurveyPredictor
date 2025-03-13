from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from mangum import Mangum
app = FastAPI()

# Load the trained model and encoders from the 'models' folder
model_path = "models/npi_model.pkl"
encoder_path = "models/label_encoders.pkl"

try:
    model = joblib.load(model_path)
    label_encoders = joblib.load(encoder_path)  # Dictionary of encoders
except Exception as e:
    print(f"Error loading model or encoders: {e}")


# The input format from the user
class TimeInput(BaseModel):
    time: str  # Example: "15:30" for 3:30 PM


# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        with open("templates/index.html", "r") as file:
            return file.read()
    except Exception as e:
        return HTMLResponse(f"<h1>Error loading HTML file: {e}</h1>")


# Prediction Endpoint
@app.post("/predict")
def predict_active_npis(input: TimeInput):
    try:
        # Read the uploaded dataset
        data = pd.read_excel("models/dummy_npi_data.xlsx")

        # Convert 'Login Time' to just the hour (0 to 23)
        data['Login Time'] = pd.to_datetime(data['Login Time']).dt.hour

        # Extract the hour from the input time (Example: "15:30" -> 15)
        user_time = int(input.time.split(":")[0])

        # Filter dataset to match user input time
        filtered_data = data[data['Login Time'] == user_time].copy()

        if filtered_data.empty:
            return {"message": "No doctors found at this time.", "success": False}

        # Apply the same encoding as used during training
        for column in ['State', 'Region', 'Speciality']:
            if column in filtered_data.columns:
                encoder = label_encoders.get(column)
                if encoder:
                    filtered_data.loc[:, column] = encoder.transform(filtered_data[column])

        # Prepare features for prediction (Ensure correct column order)
        required_columns = ['State', 'Login Time', 'Usage Time (mins)', 'Region', 'Speciality']
        if not all(col in filtered_data.columns for col in required_columns):
            return {"message": "Some required columns are missing.", "success": False}

        X_new = filtered_data.loc[:, required_columns]

        # Make predictions
        filtered_data['Prediction'] = model.predict(X_new)

        # Get NPIs where prediction = 1 (likely to attend)
        active_npis = filtered_data[filtered_data['Prediction'] == 1][['NPI']]

        if active_npis.empty:
            return {"message": "No active NPIs found at this time.", "success": False}

        # Save to CSV
        file_name = "models/predicted_npis.csv"
        active_npis.to_csv(file_name, index=False)

        return {"message": "Prediction saved successfully!", "success": True}

    except Exception as e:
        print(f"Error during prediction: {e}")
        return {"message": f"Something went wrong: {str(e)}", "success": False}


# Download Endpoint
@app.get("/download")
def download_file():
    file_path = "models/predicted_npis.csv"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='text/csv', filename='predicted_npis.csv')
    return {"message": "File not found."}
