

try:
    from PIL import Image
   
except ImportError:
    
    import Image
import pytesseract

def ocr_core(filename):

    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    custom_config = r'--oem 3 --psm 6'

    img_info = pytesseract.image_to_data( Image.open(filename) , output_type=pytesseract.Output.DICT, config=custom_config,lang='ben')



    def parse(data):
        '''Function to parse data from detected text'''
        parsed = []
        last_word = ''
        for word in data:
            if word != '':
                parsed.append(word)
                last_word = word
            if last_word != '' and word == '':
                parsed.append('\n')

        return " ".join(parsed)

    data = parse(img_info['text'])
    file = open('data/image_result.txt', 'w', encoding='utf-8')
    file.write(data)


    # CHECK THE VALUE IF IT IS AVAILABLE IN THE FILE OR NOT, IF AVAILABLE THEN HOW MANY TIMES
    #
    # val = input("Enter the finding word :- ")
    # x = img_info['text'].count(val)
    # if x > 0:
    #     print(f"\nThe {val} is in the file and {val} is available in the list {x} times.")
    # else:
    #     print(f"{val} is not available in the file")

    text = pytesseract.image_to_string(Image.open(filename) , config=custom_config, lang='ben')
    # text = pytesseract.image_to_string(Image.open(filename), output_type=pytesseract.Output.DICT, config=custom_config, lang='ben')

    return text

def ocr_freq(filename):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    custom_config = r'--oem 3 --psm 6'

    img_info = pytesseract.image_to_data(Image.open(filename), output_type=pytesseract.Output.DICT, config=custom_config,lang='ben')
    final_list = [string for string in img_info['text'] if string != ""]
    l=len(final_list)

    return l

def ocr_count(filename):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    custom_config = r'--oem 3 --psm 6'

    img_info = pytesseract.image_to_data(Image.open(filename), output_type=pytesseract.Output.DICT, config=custom_config,lang='ben')
    def parse(data):
        '''Function to parse data from detected text'''
        parsed = []
        last_word = ''
        for word in data:
            if word != '':
                parsed.append(word)
                last_word = word
            if last_word != '' and word == '':
                parsed.append('\n')

        return " ".join(parsed)

    data = parse(img_info['text'])

    # from collections import Counter
    # freq = Counter(data.split()).most_common()

    my_list = []
    my_list = data.split()
    word_frequency = [my_list.count(a) for a in my_list]

    freq=dict(zip(my_list, word_frequency))

    return freq



# def ocr_search(filename):
#     pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
#     custom_config = r'--oem 3 --psm 6'
#     img_info = pytesseract.image_to_data(Image.open(filename), output_type=pytesseract.Output.DICT, config=custom_config,lang='ben')
#
#     x = img_info['text'].count({% search %})
#     return x

# # For  Test purposes --- TEST CODE
# def oct_cmt(file):
#     import cv2
#     import numpy as np
#     import pytesseract
#
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
#
#     img = cv2.imread(file,0)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Remove shadows,
#     dilated_img = cv2.dilate(gray, np.ones((7, 7), np.uint8))
#     bg_img = cv2.medianBlur(dilated_img, 21)
#     diff_img = 255 - cv2.absdiff(gray, bg_img)
#     norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255,
#                              norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
#
#     # Threshold using Otsu's
#     work_img = cv2.threshold(norm_img, 0, 255, cv2.THRESH_OTSU)[1]
#
#     # Tesseract
#     custom_config = r'--oem 3 --psm 6'
#     text1 = pytesseract.image_to_string(work_img, config=custom_config, lang='ben')
#
#     return img








# print(ocr_core('test1.png'))
