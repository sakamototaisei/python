import os
import sys
import face_recognition
import cv2
import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import glob

import config

# 設定ファイルの読み込み
threshold = config.threshold

# 顔情報の初期化
face_locations = []
face_encodings = []

# 登録画像の読み込み
image_paths = glob.glob('JARVIS/image/*')
image_paths.sort()
known_face_encodings = []
known_face_names = []
checked_face = []

# delimiter = "/"

for image_path in image_paths:
    im_name = os.path.basename(image_path).split('.')[0]
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(im_name)


video_capture = cv2.VideoCapture(0)
# 顔判定フラグの初期化
sakatai_face_flag = []


def main():

    while True:
        # ビデオの単一フレームを取得
        _, frame = video_capture.read()

        # ビデオの現在のフレーム内のすべての顔に対してその位置情報を検索
        face_locations = face_recognition.face_locations(frame)
        # 顔の位置情報からエンコードを生成
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            # 顔が登録済みの顔と一致するか確認
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding, threshold)
            if len(sakatai_face_flag) == 0:
                sakatai_face_flag.append(matches[0])
            name = "Unknown"

            # カメラ画像と最も近い登録画像を見つける
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # 位置情報の表示
        for (top, right, bottom, left) in face_locations:
            # 顔領域に枠を描画
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # 枠の下に名前を表示
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # 結果をビデオに表示
        cv2.imshow('Video', frame)

        # ESCキーで終了
        if cv2.waitKey(1) == 27:
            break
        if len(sakatai_face_flag) == 1:
            # print(sakatai_face_flag)
            if sakatai_face_flag[0] == True:
                print('SAKATAI様本人の確認ができました')
                time.sleep(3)
                sakatai_face_flag.clear()
                break
            else:
                print('あなたはSAKATAI様ではありません')
                sakatai_face_flag.clear()


main()

video_capture.release()
cv2.destroyAllWindows()
