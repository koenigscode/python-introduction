from sklearn.datasets import load_iris
iris = load_iris()  # load example dataset
data = iris.data  # get the data of the dataset
print(data[:3])  # print first three entries