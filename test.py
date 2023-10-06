import unittest
import json

from app import app

class PredictionTest(unittest.TestCase):

    def test_predict1(self):
        """Tests that the predict function returns a value equal to the input if less than threshold (441) """

        input_data = {
            "number":200
        }

        expected_prediction = 200

        response = app.test_client().post("/", json=input_data)
        print(response)
        actual_prediction = json.loads(response.data)["prediction"]

        self.assertEqual(actual_prediction, expected_prediction)
        
    def test_predict2(self):
        """Tests that the predict function makes the correct predictions for values greater than threshold (441)"""

        input_data = {
            "number":1000
        }

        expected_prediction = 589

        response = app.test_client().post("/", json=input_data)
        print(response)
        actual_prediction = json.loads(response.data)["prediction"]

        self.assertEqual(actual_prediction, expected_prediction)

if __name__ == "__main__":
    unittest.main()