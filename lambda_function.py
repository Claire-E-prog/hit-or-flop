import json
import joblib

def lambda_handler(event, context):
    model = joblib.load('movie_hit_predictor.pkl')
    input = event["body"]
    

    # Perform prediction
    prediction = model.predict(input)[0]
    result = "hit" if prediction == 1 else "flop"

    # Return the response
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": result}),
    }