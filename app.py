def load_model():
    import joblib
    model = joblib.load('movie_hit_predictor.pkl')
    return model
def inference():
    model = load_model()
    input = {"budget": 100000000, "runtime": 120, "cast_total_facebook_likes": 10000} # Input data - triggers lambda_handler
    prediction = model.predict(input)[0]
    result = "hit" if prediction == 1 else "flop"
    print{f'The movie will be a {result}'}
    return

if __name__ == "__main__":
    inference()