class CustomLanguageDetector:
    def __init__(self):
        self.language_characters = {
            'en': set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            'hi': set('अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह'),
            'bn': set('অআইঈউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ'),
            'ta': set('அஆஇஈஉஊஎஏஐஒஓஔகஙசஞடணதநனபமயரலவழளஷஸஹ'),
            'te': set('అఆఇఈఉఊఋఎఏఐఒఓఔకఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలవశషసహ'),
            'ru': set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'),
            'ja': set('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'),

            # Add more languages as needed
        }

        self.language_names = {'en': 'English', 'hi': 'Hindi', 'bn': 'Bengali', 'ta': 'Tamil', 'te': 'Telugu', 'ru': 'Russian', 'ja': 'Japanese'}


    def detect_language(self, text):
        detected_languages = []
        for language, characters in self.language_characters.items():
            if any(char in characters for char in text):
            # if any(char in text for char in characters):    
                detected_languages.append(language)
                # print(f"{language} has been added")
        return detected_languages if detected_languages else ['NO Language Found']
    
if __name__ == "__main__":

    # text_to_detect = f"Hello boss আপন शुभ प्रभात / नमस्कार"
    text_to_detect = f"আপন शुभ प्रभात / नमस्कार"



    detected_languages = CustomLanguageDetector().detect_language(text_to_detect)
    detected_language_list = ', '.join(detected_languages)
    print(f"The detected languages are: {detected_languages}")
    print(f"The detected languages are: {detected_language_list}")
