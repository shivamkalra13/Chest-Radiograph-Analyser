# CRA(Chest Radiograph Analyser)

## About
Repository for a deep learning project "Chest Radiograph Analyser", The intention of this project is to train machine learning models using different machine learning approaches and comparing the performance of CNN with Traditional Machine Learning methods(Linear SVM, Kernel SVM, KNN and Random Forest) in classifying the Pneumonia Chest Radiographs(Both DICOM and JPEG format is supported).

### Technology Stack :-
##### ->Python
##### ->scikit learn
##### ->CNN(Convolutional Neural N/W)
##### ->Keras

### Feature Extraction :-
##### ->CNN uses embedded Feature Extraction
##### ->For Traditonal Machine Learning methods, Features were extracted manually from images using the 3 following feature extraction techniques:-
######  >Haralick Textural Feature Extraction
######  >HOG(Histogram of Oriented Gradients)
######  >Hu Moments

### User Interface:-
#### User interface is implemented using PyQT framework.
#### Input = Takes either DICOM or JPEG file of Radiograph as input.
#### Output = Pneumonia Positive / Pneumonia Negetive.
#### ML model = CNN model is used to provide prediction.
#### UI1, UI2, UI3, UI4 are the scrshots of the User Interface created and Working Video is the Demo Video of User-Interface.

### For more details refer to ACRA_PPT.pdf

### User Interface Screenshots:-

![UI1.png](https://github.com/shivamkalra13/Chest-Radiograph-Analyser/blob/master/UI1.png)

![UI2.png](https://github.com/shivamkalra13/Chest-Radiograph-Analyser/blob/master/UI2.png)

![UI3.png](https://github.com/shivamkalra13/Chest-Radiograph-Analyser/blob/master/UI3.PNG)

![UI4.png](https://github.com/shivamkalra13/Chest-Radiograph-Analyser/blob/master/UI4.PNG)

