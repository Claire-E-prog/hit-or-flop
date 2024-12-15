import json
import joblib
import os
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "movie_hit_predictor.pkl")
logger.info(f"Loading model from {model_path}")
model = joblib.load(model_path)
logger.info("Model successfully loaded")

def lambda_handler(event, context):
    """
    AWS Lambda handler function that predicts whether a movie will be a "hit" or a "flop"
    based on input features: budget, rating, and popularity.
    
    Args:
        event (dict): Event data passed to the Lambda function.
        context: AWS Lambda runtime context object (not used here).

    Returns:
        dict: Response containing the prediction result or an error message.
    """
    # Log the incoming event
    logger.info(f"Received event: {event}")

    # Parse the input data from the event body
    input_data = json.loads(event["body"])
    logger.info(f"Parsed input data: {input_data}")

    # Extract features
    features = [
        input_data["budget"],
        input_data["rating"],
        input_data["popularity"],
    ]
    logger.info(f"Extracted features: {features}")

    # Perform prediction
    prediction = model.predict([features])[0]
    result = "hit" if prediction == 1 else "flop"
    logger.info(f"Prediction result: {result}")

    # Return the response
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": result}),
    }