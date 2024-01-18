# sign-language-detector-python

Sign language detector with Python, OpenCV and Mediapipe!

Hear im detecting human sign language for numariacal number prediction using OpenCV and Mediapipe libs.

step 1: =>  install requirement.txt file for dependend libraries.

step 2: =>  Run collect_imgs.py file
        =>  Collect our own images dataset to train our model
        =>  Before mention how many class you want in *number_of_classes*
        =>  It will open your webcam --press Q-- button and make hand sign signal
        =>  It will save the all images in _data_ folder

step 3: =>  Then prepere for data set
        =>  Run the create_dataset.py file
        =>  mediapipe library use to predict in image hand positions
        =>  Will load through all class images respective data and label
        =>  create dump pickle file

step 4: =>  Build a model for predict the sign Classification
        =>  Choosing Random Forest model Classifier for good accuracy
        =>  Passing train and test data into the model
        =>  Im getting 98% better accuracy in the model
        =>  Create pickle file in the **model.p**

step 4: =>  Run the sign_lang_classifier.py file
        =>  Hear midiapipe use for hand sign position
        =>  Assigning respective **class and labels**
        =>  live web cam will open show your sign
        =>  OpenCV use for webcam and Rectangle shape and put text into the video



tutorial behind the project credits for the tutor
[![Watch the video](https://img.youtube.com/vi/MJCSjXepaAM/0.jpg)](https://www.youtube.com/watch?v=MJCSjXepaAM)