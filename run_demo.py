import cv2
import sys
from faceorientationprep.faceorientationfixer import FaceOrientationFixer


def main():

    if len(sys.argv) == 1:
        msg = """Usage: 
        python run_demo.py \"<image-path>\""""
        print(msg)
        return

    f = FaceOrientationFixer()
    im = cv2.imread(sys.argv[1])
    cv2.imshow("s", f.fixOrientation(im))
    cv2.waitKey(0)
    return


if __name__ == '__main__':
    main()