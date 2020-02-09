import cv2
import numpy as np


class FaceDetector():

    """Detect faces on image."""

    def __init__(
        self,
        factor: float = 1.2,
        neighbors: int = 5,
        minsize: tuple = (30, 30)
    ) -> None:
        self._factor = factor
        self._neighbors = neighbors
        self._minsize = minsize
        self._face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

    def load_image_from_bytes(self, data):
        """Load image from byte string."""
        np_array = np.frombuffer(data, np.uint8)
        return cv2.imdecode(np_array,  cv2.IMREAD_COLOR)

    def convert_to_grayscale(self, image):
        """Convert image to grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def detect_faces(self, image):
        """
        Detect faces on image and return them as `numpy` array or
        return empty tuple if faces not detected.
        """
        faces = self._face_cascade.detectMultiScale(
            self.convert_to_grayscale(image),
            scaleFactor=self._factor,
            minNeighbors=self._neighbors,
            minSize=self._minsize
        )
        return faces
