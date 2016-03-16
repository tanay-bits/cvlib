Real-Time Face Detection and Recognition with OpenCV (Python)
==============
This is a small Python program which performs [face detection using Haar cascades](http://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0) based on the [Viola-Jones framework](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework), as well as face recognition with a choice of two of the most popular algorithms for this purpose - EigenFaces and FisherFaces. For a detailed introduction to these techniques, refer to [this tutorial](http://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html).

[![demo](http://i.imgur.com/rXUSWd2.png)](https://www.youtube.com/watch?v=nvPzOo8tyUs "Click to watch demo!")


Program Interface
----------------------

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Face%20Recognition/misc/flow_chart.png)

+  Save the above Python scripts and XML files in a directory and create a subdirectory within it named "face_data".
+  Run the *gui_face.py* script to start up the program. Type in the user's name and hit *Train (FisherFaces)* or *Train (EigenFaces)*. Note that FisherFaces requires at least two users trained, for [LDA](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) to work.

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Face%20Recognition/misc/gui.png)

+  A webcam feed is opened from which photos of the user's face are detected and captured (stored in a folder corresponding to the user within the "face_data" folder) at regular intervals. The number of images captured to make the user's training dataset is set in *face_train_fisher.py* and *face_train_eigen.py* as the value of global variable *NUM_TRAINING* (currently 100). For the algorithms to work robustly, it is advisable to capture photos of the face at several distances, with different expressions, and different background lighting conditions. If there is someone else near you, make sure that during the capturing process, you (the intended user for whom the training set is being created) are in closest to the camera, to ensure only your face is captured. Once training images are captured, hit 'q' on your keyboard to close the webcam feed.

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Face%20Recognition/misc/Capture.PNG)

+  Other users who wish to be recognized should take turns to enter their names in the GUI and use the desired training method, going through the same process as described above.
+  Once all users have finished making their training sets, press *Recognize (FisherFaces)* or *Recognize (EigenFaces)*, depending on the method that was used for training. A webcam feed pops up, which shows blue boxes around recognized faces (and shows their name and confidence value), and red boxes around unknown faces.
+ The lower the confidence value, the more accurate is the recognition.
+ Every time you train a face, the training data is updated instead of overwritten, which means you can add to a previous user's training data in different lighting/distance settings later on.

Results
---------

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Face%20Recognition/misc/Results.png)

+ There is a clear difference between the confidence values reported by the two algorithms - FisherFaces results in much lower confidence values (=> more accurate) than EigenFaces.
+ Having more pictures in each user's dataset, both in number and in diversity of setting (expression, lighting, distance, etc.) produces more reliable recognition compared to small datasets in the same location. But in any case, Fisherfaces is more robust against external sources of variation like illumnination, since it also takes into account the training images' label when doing classification.