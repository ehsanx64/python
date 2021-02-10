"""
Source code for example in scikit-learn official tutorial.
"""
from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

print("digits.data: \n", digits.data)
print("digits.target: \n", digits.target)
print("digits.images[0]: \n", digits.images[0])
