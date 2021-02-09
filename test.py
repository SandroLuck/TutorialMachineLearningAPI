import unittest

from main import SurvivePredictor, PersonInformation


class TestClassifier(unittest.TestCase):
    def test_classifier(self):
        # One testcase to show, rather trivial
        # We could test legal inputs, like non negatives etc
        # But we did not implement
        self.predictor = SurvivePredictor()
        assert 0.5 > self.predictor.predict(
            PersonInformation(sex='male', pclass=2)), "Issue with prediction negative"
        assert 0.5 < self.predictor.predict(
            PersonInformation(sex='female', pclass=2)), "Issue with prediction positive"


if __name__ == '__main__':
    unittest.main()
