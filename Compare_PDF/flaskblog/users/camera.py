import cv2
import face_recognition
from PIL import Image
import os
import time

dir_path = "images"


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def get_frame(self):
        success, frame = self.video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=2)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_image = rgb_small_frame[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            File_Formatted = ("%s" % (top)) + ".jpg"
            file_path = os.path.join(dir_path, File_Formatted)
            pil_image.save(file_path)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

