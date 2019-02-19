from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


iris = datasets.load_iris() #Loading data set

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0) #Putting given data into a test set.
clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train) #Choosing which svm kernel to use, using linear as classifier.
scores = cross_val_score(clf, iris.data, iris.target, cv=5) #Obtaining scores by splitting data, fitting the model, and obtaining score "cv=k" times, score checked each iteration.

print("SVM Linear Accuracy: ", scores.mean()) # Return mean of scores.