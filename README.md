# Electronic Component Fault Detection

A beginner-friendly Machine Learning project that predicts whether an electronic component is **Normal** or **Faulty** from electrical and operating measurements.

## Technologies
- Python
- Pandas
- Scikit-learn
- Random Forest
- Flask
- HTML/CSS

## Input Features
1. Voltage
2. Current
3. Resistance
4. Temperature
5. Frequency
6. Vibration

## Project Structure

```text
Electronic_Component_Fault_Detection/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── electronic_components.csv
├── models/
│   └── fault_detector.pkl
├── src/
│   └── train_model.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run in VS Code

### 1. Open the project
Open this folder in VS Code.

### 2. Create virtual environment
Windows PowerShell:
```powershell
python -m venv venv
```

### 3. Activate it
```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then activate again.

### 4. Install packages
```powershell
pip install -r requirements.txt
```

### 5. Train the model
```powershell
python src/train_model.py
```

The trained model is saved in:
`models/fault_detector.pkl`

### 6. Start the web application
```powershell
python app.py
```

### 7. Open in browser
Go to:
`http://127.0.0.1:5000`

## Example Test Values

### Normal
- Voltage: 7
- Current: 1
- Resistance: 7
- Temperature: 35
- Frequency: 500
- Vibration: 1

### Potential Fault
- Voltage: 11.5
- Current: 2.3
- Resistance: 2
- Temperature: 90
- Frequency: 700
- Vibration: 4

## Important Note
The included dataset is synthetic and is intended for learning/demo purposes. For a real engineering project, replace it with measurements from actual components or a validated public dataset.

## Resume Description
Developed a machine learning-based Electronic Component Fault Detection system using Random Forest classification. Built a Flask web interface to predict component health from voltage, current, resistance, temperature, frequency, and vibration measurements.
