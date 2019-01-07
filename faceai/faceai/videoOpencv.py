# coding=utf-8
# 视频人脸检测类 - OpenCV版本
import cv2


# 图片识别方法
def discern(img):
    classifier = cv2.CascadeClassifier(
        "/Users/zhangmingxing/resp/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    )
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # OpenCV人脸识别分类器
    color = (0, 255, 0)  # 定义绘制颜色
    # 调用识别人脸
    faceRects = classifier.detectMultiScale(
        grayImg, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRects):  # 大于0则检测到人脸
        for faceRect in faceRects:  # 单独框出每一张人脸
            x, y, w, h = faceRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)

    cv2.imshow("image", img)  # 显示图像


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        discern(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
