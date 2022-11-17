import cv2
from PIL import Image

original_face_img = "images/face_img.png"
original_eye_img = "images/eye_img.png"


def find_face():
    # 顔検出分類器を用意
    cascade_file = "haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = cv2.imread(original_face_img)  # 画像を読み込み、グレイスケールに変換
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(img_gray)
    return face_list


def paste_img(facd_list):
    # 右目
    r_eye_x = face_list[0][0]
    r_eye_y = face_list[0][1]
    r_eye_w = face_list[0][2]
    r_eye_h = face_list[0][3]

    # 左目
    l_eye_x = face_list[1][0]
    l_eye_y = face_list[1][1]
    l_eye_w = face_list[1][2]
    l_eye_h = face_list[1][3]

    face_img = Image.open(original_face_img)
    r_eye_img = Image.open(original_eye_img)
    l_eye_img = Image.open(original_eye_img)

    resized_r_eye_img = r_eye_img.resize((r_eye_w, r_eye_h))
    resized_l_eye_img = l_eye_img.resize((l_eye_w, l_eye_h))

    face_img.paste(resized_r_eye_img, (r_eye_x, r_eye_y), resized_r_eye_img.split()[3])
    face_img.paste(resized_l_eye_img, (l_eye_x, l_eye_y), resized_l_eye_img.split()[3])
    face_img.save("images/hensin_pillow.png")


face_list = find_face()
# print(face_list)
paste_img(face_list)
