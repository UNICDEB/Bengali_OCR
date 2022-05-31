

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
