import unittest
import json

from app import app

class PredictionTest(unittest.TestCase):

    def test_predict(self):
        """Tests that the predict function makes the correct prediction for a given input."""

        input_data = {
            "number":100
        }

        expected_prediction = 100

        response = app.test_client().post("/", json=input_data)
        print(response)
        actual_prediction = json.loads(response.data)["prediction"]

        self.assertEqual(actual_prediction, expected_prediction)

if __name__ == "__main__":
    unittest.main()