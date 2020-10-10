from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("kakaotalk_aqua.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '","' in line:
            text += (
                line.split('","')[1]
                .replace("이모티콘\n", "")
                .replace("사진\n", "")
                .replace("삭제된 메시지입니다", "")
                .replace("ㅋ", "")
                .replace("ㅠ", "")
                .replace("ㅜ", "")
                .replace("사진", "")
                .replace("동영상", "")
                .replace("이모티콘", "")
                .replace("https", "")
                .replace("EB", "")
                .replace("EC", "")
                .replace("ED", "")
                .replace("2장", "")
                .replace("3장", "")
                .replace("6장", "")
                .replace("co.kr", "")
                .replace("co kr", "")
                .replace("pdf", "")
                .replace("파일", "")
                .replace("blog naver", "")
            )


mask = np.array(Image.open("cloud.png"))
wc = WordCloud(
    font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    background_color="white",
    mask=mask,
)
wc.generate(text)
wc.to_file("wordcloud_aqua.png")