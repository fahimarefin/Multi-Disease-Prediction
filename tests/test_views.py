from django.test import TestCase
from django.urls import reverse
from project412.views import diabetes_prediction

class DiabetesPredictionTests(TestCase):
    def test_diabetes_prediction_view_get(self):
        response = self.client.get(reverse('project412:diabetes_prediction'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'predict_diabetes.html')

    def test_diabetes_prediction_view_post(self):
        data = {
            'age': 30,
            'hypertension': 'yes',
            'heart_disease': 'no',
            'bmi': 25.0,
            'hba1c': 6.5,
            'bloodGlucose': 120.0,
            'gender': 'male',
            'smoking_history': 'never'
        }

        response = self.client.post(reverse('project412:diabetes_prediction'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'predict_diabetes_result.html')
        self.assertIn('prediction_result', response.context)

    def test_diabetes_prediction_view_invalid_post(self):
        data = {
            'age': 30,
            'hypertension': 'yes',
            'heart_disease': 'no',
            'bmi': 25.0,
            'hba1c': 6.5,
            'bloodGlucose': 120.0,
            'gender': 'male',
            'smoking_history': 'never'
        }

        
        with self.assertRaises(ValueError):
            response = self.client.post(reverse('project412:diabetes_prediction'), data)

        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'predict_diabetes.html')
       
        self.assertNotIn('Prompt', response.context)
