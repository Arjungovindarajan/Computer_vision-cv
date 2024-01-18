# Sign language detector

Sign language detector with Python, OpenCV, and Mediapipe!

Here I'm detecting human sign language for numerical number prediction using OpenCV and Mediapipe libs.

step 1: 
        
        =>  install requirement.txt file for dependent libraries.

step 2: 
        
        =>  Run collect_imgs.py file
        
        =>  Collect our own image dataset to train our model
        
        =>  Before mentioning how many classes you want in *number_of_classes*
        
        =>  It will open your webcam --press Q-- button and make hand sign signal
        
        =>  It will save all images in the _data_ folder

step 3: 
        
        =>  Then prepare for the data set
        
        =>  Run the create_dataset.py file
        
        =>  media pipe library used to predict image hand positions
        
        =>  Will load through all class image's respective data and label
        
        =>  Create a dump pickle file

step 4: 
        
        =>  Build a model for predicting the sign Classification
        
        =>  Choosing a Random Forest model Classifier for good accuracy
        
        =>  Passing train and test data into the model
        
        =>  Im getting 98% better accuracy in the model
        
        =>  Create a pickle file in the **model.p**

step 4: 

        =>  Run the sign_lang_classifier.py file
        
        =>  Hear mediapipe use for hand sign position
        
        =>  Assigning respective **class and labels**
        
        =>  live webcam will open and show your sign
        
        =>  OpenCV is used for webcam and Rectangle shapes and put text into the video
