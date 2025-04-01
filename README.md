# Doctor Survey Predictor

## Overview

The **Doctor Survey Predictor** is an AI-powered web application that predicts which doctors (NPIs) are most likely to attend a survey at a given time based on their activity data. The application provides an interactive user interface where users can select a time slot in AM/PM format and download a CSV file containing the predicted NPIs.

## Features

- **Time-based Prediction**: Predicts doctor participation based on given time input.
- **User-friendly Interface**: Allows time selection in AM/PM format with only '00' and '30' minute intervals.
- **Downloadable Predictions**: Users can download the predictions as a CSV file.
- **FastAPI Backend**: Ensures efficient and scalable model inference.
- **Interactive HTML UI**: Engaging frontend for easy interaction.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML, JavaScript
- **Machine Learning**: TensorFlow/PyTorch Model
- **Data Storage**: CSV/Database

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- FastAPI
- Uvicorn
- Pandas
- TensorFlow 2.12.0

1. Clone the repository:
   ```bash
   git clone https://github.com/tech5s5/doctor-survey-predictor.git
   cd doctor-survey-predictor
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open the app in a browser:
   ```
   http://127.0.0.1:8000
   ```

## Usage

1. Select a time slot from the dropdown (e.g., 3:00 PM, 3:30 PM, etc.).
2. Click the **Predict** button.
3. If predictions are successful, download the CSV file.

## Deployment

You can deploy the app using **Render, Fly.io, Railway, or Streamlit**.

### Live Demo

Check out the deployed app here: [Doctor Survey Predictor](https://doctorsurveypredictor.onrender.com)

You can deploy the app using **Render, Fly.io, Railway, or Streamlit**.

## Folder Structure

```
doctor-survey-predictor/
│── models/  # Directory for storing ML models
│── templates/  # Contains HTML files for the UI
│── main.py  # FastAPI application
│── requirements.txt  # Dependencies file
│── README.md  # Project documentation
```

## Future Improvements

- Improve model accuracy with more training data.
- Add authentication for secured access.
- Deploy on cloud platforms like AWS/GCP.

## Contributing

Feel free to fork the repository and submit pull requests!

## License

This project is licensed under the MIT License.

---

Made with ❤️ by Sumit

