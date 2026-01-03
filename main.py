import cv2
from hyperlpr3 import LicensePlateCatcher
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def get_font(font_size=32):
    # 常见字体路径
    font_paths = [
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",  # Linux Noto
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",  # 另一种Linux
        "/usr/share/fonts/truetype/arphic/ukai.ttc",               # Linux开源字体
        "C:/Windows/Fonts/simhei.ttf",                             # Windows黑体
        "simhei.ttf",                                              # 项目目录
    ]
    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, font_size)
    # 没有中文字体时，退回默认
    return ImageFont.load_default()

def draw_chinese_text(img, text, position, color=(0,255,0), font_size=32):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = get_font(font_size)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    lpr = LicensePlateCatcher()
    print("按 'q' 键退出程序")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取帧")
            break

        results = lpr(frame)
        for plate, confidence, _, bbox in results:
            print(f"识别结果: {plate}, 置信度: {confidence:.2f}")
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            frame = draw_chinese_text(frame, f"{plate} {confidence:.2f}", (x1, y1-35), color=(0,255,0), font_size=32)
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()