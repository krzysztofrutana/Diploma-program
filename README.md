<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
  <h3 align="center">Finding the optimal grouping method for a data set using a classifier </h3>

  <p align="center">
    The program is based on selected features of the set, such as median, mode, kurtosis, skewness, quartiles, etc. Based on these features, the classifier proposes the best grouping method, distance calculation method and grouping method parameter.


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

The main window for selecting a data set (.tab, .csv, .txt format) with an indication of whether a given set has a row with column headers. Then you can delete empty or unnecessary columns. Before calculating the features, it is also recommended to select the decision attribute and the indexing attribute, if any. Then, after receiving the features, the learned classifier can be used to determine the best grouping method, distance calculation method, and grouping method parameter. The result can be compared with the result of searching for these parameters using the Brute Force method. The program includes three clustering quality measures (the results for each are significantly different) and includes three clustering methods (KMeans iterative, agglomerative Agglomerative and DBScan density method) and three distance calculation methods (Euclidean, cityblock and cosine)

![Diploma program Screen Shot](https://i.ibb.co/x2fHWGN/main-Window.jpg)


This window allows you to calculate the features of the selected set and add the results to the classifier training table. The more results in the table, the better the prediction.

![Diploma program Screen Shot](https://i.ibb.co/SRM2F2Y/edycja-Bazy.jpg)


This window allows you to change the classifier parameters.

![Diploma program Screen Shot](https://i.ibb.co/SJKYNvc/parametryklasyfikatora.jpg)


This window allows you to test the classification quality on the training table with the LeaveOneOut method.

![Diploma program Screen Shot](https://i.ibb.co/Snk2nyQ/test-Klasyfikatora.jpg)


This window allows you to find the best classifier parameters for defined ranges of parameters by the GridSearchCV method.

![Diploma program Screen Shot](https://i.ibb.co/TKBV46g/test-Parametrow-Klasyfikatora.jpg)


### Built With

* [Python 3.7](https://www.python.org/)
* [Pyside2 (PyQT5)](https://wiki.qt.io/Qt_for_Python)
* [Scikit-learn](https://scikit-learn.org/stable/)


<!-- GETTING STARTED -->
## Getting Started

This is only source code. Affter add project to PyCharm and download neccesary packages everything should work. 



<!-- CONTACT -->
## Contact

Krzysztof Rutana - krzysztofrutana@wp.pl

Project Link: [https://github.com/krzysztofrutana/OCR-Desktop](https://github.com/krzysztofrutana/OCR-Desktop)

