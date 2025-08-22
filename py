import joblib
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Load the trained ML model once
model_path = os.path.join(os.path.dirname(__file__), "crop_recommendation_model.pkl")
model = joblib.load(model_path)

@csrf_exempt
def predict_crop(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            N = data.get("N")
            P = data.get("P")
            K = data.get("K")
            temperature = data.get("temperature")
            humidity = data.get("humidity")
            ph = data.get("ph")
            rainfall = data.get("rainfall")

            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            prediction = model.predict(features)[0]

            return JsonResponse({"recommended_crop": prediction}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Send a POST request with soil & climate data."}, status=405)
