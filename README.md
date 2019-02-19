# ICP-4

## Prerequisites

Before starting the user should download the libraries :

* 1 Latest version of pip

* 2 scikit-learn
* 3 numpy, (numpy is automatically installed with scikit-learn)

## Question 1.

<details><summary>Use cross validation with Naive Bayes method and evaluate the data.</summary>
<p>
    
![Screenshot](https://i.imgur.com/Kpkp86c.png)
</p>
</details>  

User must import the following :

Import GaussianNB from sklearn.naive_bayes to use as classifier.

from sklearn import datasets to read the data

from sklearn.model_selection import train_test_split to experiment.

from sklearn.model_selection import cross_val_score to evaluate score.

![Screenshot](https://i.imgur.com/m1CDf4t.png)

First the user must test the data by inputting the loaded dataste into train_test_split.

Then choose a classifier ("GaussianNB()") and then obtain the score.

![Screenshot](https://i.imgur.com/nzmCXmB.png)

Above is the output accuracy of the Naïve Bayes classifier.

## Question 2.

<details><summary> Using the same dataset as before, implement it using linear SVM.</summary>
  
![Screenshot](https://i.imgur.com/mY5g9ic.png)
</p>
</details>
  
User must import the following :

from sklearn import svm, datasets to read the data, and to use the svm library.

from sklearn.model_selection import train_test_split to experiment.

from sklearn.model_selection import cross_val_score to evaluate score.

![Screenshot](https://i.imgur.com/nirrjXC.png)

Reapeat as in question one, except change "clf" aka classifier to use "svm.SVC(kernel='linear', C=1).fit(x_train, y_train)".

This will change the classifier to utilize linear SVM and give the following output :

![Screenshot](https://i.imgur.com/TTvslUZ.png)

Linear SVM gives a higher percentage accuracy scored in comparison to using the Naïve Bayes classifier.

The main differnces between these two classifiers is that Naïve Bayes uses probability to calculate and estimate while line SVM uses geometry. There is no saying which one is better unless there is a good understanding of the prepared dataset. However in this case, linear SVM had higher accuracy than Naïve Bayes. Linear SVM's advantage is when a dataset of large quantities is given, which will result in higher accuracy, which Naïve Bayes falls short of.

## Question 3.

<details><summary> Using the same dataset as before, implement it using rbf kernel with SVM.</summary>
<p>
  
![Screenshot](https://i.imgur.com/h15M8Rc.png)
</p>
</details>

Everything imported is reused as in Question 2. Only one minor change is applied in which changing the kernel from "linear"  to "rbf" on line 9.

![Screenshot](https://i.imgur.com/SYOXFSj.png)

![Screenshot](https://i.imgur.com/fLDSqMx.png)

There elicited no change in the output.
