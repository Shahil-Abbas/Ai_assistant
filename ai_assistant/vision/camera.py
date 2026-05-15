import cv2

camera_running = False


def open_camera():

    global camera_running

    camera_running = True

    cap = cv2.VideoCapture(0)

    while camera_running:

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Jarvis Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    camera_running = False


def close_camera():

    global camera_running

    camera_running = False