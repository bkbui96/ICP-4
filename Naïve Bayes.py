from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris() #Loading data set

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0) #Putting given data into a test set.
clf = GaussianNB() #Using Naive Bayes as classifier.
clf.fit(x_train, y_train) #Fitting data
scores = cross_val_score(clf, iris.data, iris.target, cv=5) #Obtaining scores by splitting data, fitting the model, and obtaining score "cv=k" times, score checked each iteration.

print("Naive Bayes Accuracy: ", scores.mean())