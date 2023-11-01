import googletrans

translator = googletrans.Translator()


def translate(text, dest='en', src='ko'):
    try:
        result1 = translator.translate(text1, dest, src)
        return result1.text
    except Exception as e:
        print("Error: ", e)
        return text

if __name__ == "__main__":
    text1 = "코스피, 2,300선 안착 시도…삼성전자 1.49% 강세 움직임"
    print(translate(text1))
