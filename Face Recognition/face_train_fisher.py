import numpy as np
import cv2
import sys
import os

FREQ_DIV = 5   #frequency divider for capturing training images
RESIZE_FACTOR = 4
NUM_TRAINING = 100

class TrainFisherFaces:
    def __init__(self):
        cascPath = "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = 'face_data'
        self.face_name = sys.argv[1]
        self.path = os.path.join(self.face_dir, self.face_name)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        self.model = cv2.createFisherFaceRecognizer()
        self.count_captures = 0
        self.count_timer = 0

    def capture_training_images(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            self.count_timer += 1
            ret, frame = video_capture.read()
            inImg = np.array(frame)
            outImg = self.process_image(inImg)
            cv2.imshow('Video', outImg)

            # When everything is done, release the capture on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                return

    def process_image(self, inImg):
        frame = cv2.flip(inImg,1)
        resized_width, resized_height = (112, 92)        
        if self.count_captures < NUM_TRAINING:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            gray_resized = cv2.resize(gray, (gray.shape[1]/RESIZE_FACTOR, gray.shape[0]/RESIZE_FACTOR))        
            faces = self.face_cascade.detectMultiScale(
                gray_resized,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                )
            if len(faces) > 0:
                areas = []
                for (x, y, w, h) in faces: 
                    areas.append(w*h)
                max_area, idx = max([(val,idx) for idx,val in enumerate(areas)])
                face_sel = faces[idx]
            
                x = face_sel[0] * RESIZE_FACTOR
                y = face_sel[1] * RESIZE_FACTOR
                w = face_sel[2] * RESIZE_FACTOR
                h = face_sel[3] * RESIZE_FACTOR

                face = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (resized_width, resized_height))
                img_no = sorted([int(fn[:fn.find('.')]) for fn in os.listdir(self.path) if fn[0]!='.' ]+[0])[-1] + 1
                
                if self.count_timer%FREQ_DIV == 0:
                    cv2.imwrite('%s/%s.png' % (self.path, img_no), face_resized)
                    self.count_captures += 1
                    print "Captured image: ", self.count_captures

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, self.face_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1,(0, 255, 0))
        elif self.count_captures == NUM_TRAINING:
            print "Training data captured. Press 'q' to exit."
            self.count_captures += 1

        return frame           

    def are_enough_faces(self):
        existingFaces = 0
        for (subdirs, dirs, files) in os.walk(self.face_dir):
            for subdir in dirs:
                existingFaces += 1

        if existingFaces > 1:
            return True
        else:
            return False

    def fisher_train_data(self):
        imgs = []
        tags = []
        index = 0

        for (subdirs, dirs, files) in os.walk(self.face_dir):
            for subdir in dirs:
                img_path = os.path.join(self.face_dir, subdir)
                for fn in os.listdir(img_path):
                    path = img_path + '/' + fn
                    tag = index
                    imgs.append(cv2.imread(path, 0))
                    tags.append(int(tag))
                index += 1
        (imgs, tags) = [np.array(item) for item in [imgs, tags]]

        self.model.train(imgs, tags)
        self.model.save('fisher_trained_data.xml')
        print "Training completed successfully"
        return


if __name__ == '__main__':
    trainer = TrainFisherFaces()
    trainer.capture_training_images()
    
    if trainer.are_enough_faces():
        trainer.fisher_train_data()
        print "Type in next user to train, or press Recognize"
    else:
        print "Type in next user to train, or press Recognize"

