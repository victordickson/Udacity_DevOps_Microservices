from flask import Flask, request, jsonify
import logging
import pandas as pd
import joblib


app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger()


@app.route("/")
def home():
    html = "<h3>Model Prediction Home</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ 1 ] }
        
        """
    
    # Logging the input payload
    try:
        clf = joblib.load("model.joblib")
    except Exception as e:
        logger.error(e)
        return "Model not loaded"

    json_payload = request.json
    logger.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    prediction = list(clf.predict(inference_payload))
    prediction = [int(x) for x in prediction]
    logger.info(f"prediction: {prediction}")
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) # specify port=80
