class AlphabetLanguageDetector:
    def __init__(self):
        self.language_characters_set = {

            "en": set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "hi": set("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह" + "्ािीुूृॄॅॆेैॉॊोौॐंःँ"),
            "bn": set("অআইঈউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ" + "্ািীুূৃৄেৈোৌ" + "ৎংঃঁ"),


            "ta": set("அஆஇஈஉஊஎஏஐஒஓஔகஙசஞடணதநனபமயரலவழளஷஸஹ" + "ாிீுூ௃௄ெேைொோௌ்ௗ"),
            "te": set("అఆఇఈఉఊఋఎఏఐఒఓఔకఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలవశషసహ" + "ాిీుూృౄెేైొోౌ్ౕౖౘౙౚ౛౜ౝ౞౟ౠౡ"),

            "or": set("ଅଆଇଈଉଊଋଏଐଓଔକଖଗଘଙଚଛଜଝଞଟଠଡଢଣତଥଦଧନପଫବଭମଯରଲଵଶଷସହ" + "ାିୀୁୂୃୄେୈୋୌ଼୍"),
            "gu": set("અઆઇઈઉઊઋએઐઓઔકખગઘઙચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહ" + "ાિીુૂૃૄૅ૆ેૈૉ૊ોૌ્૕૖૗૘૙૚૛૜૝૞૟"),
            "pa": set("ਅਆਇਈਉਊ਋ਏਐਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵਸ਼ਸ਼ਸਹ" + "ਾਿੀੁੂੇੈੋੌ੍ਯ"),
            "ml": set("അആഇഈഉഊഋഎഏഐഒഓഔകഖഗഘങചഛജഝഞടഠഡഢണതഥദധനപഫബഭമയരലവശഷസഹ" + "ാിീുൂൃൄെേൈൊോൌ്ൎൗ"),
            "kn": set("ಅಆಇಈಉಊಋಎಏಐಒಓಔಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹ" + "ಾಿೀುೂೃೄೆೇೈೊೋೌ್ಕೖ"),

            "ru": set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
            "ja": set("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"),
            "el": set("ͰͱͲͳʹ͵Ͷͷͺͻͼͽ;Ϳ΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϏϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰϱϲϳϴϵ϶ϷϸϹϺϻϼϽϾϿ"),
            "ss1": set("`~!@#%^&*(){}[]\\|;:',.<>/?")

            # Add more languages as needed
        }


        self.language_code_1 = {"en": "English", "hi": "Hindi", "bn": "Bengali", "ta": "Tamil", "te": "Telugu", "or": "Odia", "gu": "Gujarati", "pa": "Punjabi", "ml": "Malayalam", "kn": "Kannada", "ru": "Russian", "ja": "Japanese", "el": "Greek", "ss1": "Symbol 1"}       

        self.language_code_2 = {
            "en": "English",
            "hi": "हिन्दी",
            "bn": "বাংলা",
            "ta": "தமிழ்",
            "te": "తెలుగు",
            "or": "ଓଡ଼ିଆ",
            "gu": "ગુજરાતી",
            "pa": "ਪੰਜਾਬੀ",
            "ml": "മലയാളം",
            "kn": "ಕನ್ನಡ",
            "ru": "Русский",
            "ja": "日本語",
            "el": "Ελληνικά",
            "ss1": "Symbol 1🍌"}




    def detect_language(self, text):
        detected_languages = []
        for language, character_set in self.language_characters_set.items():
            if any (letter in character_set for letter in text):
                detected_languages.append(language)
        return detected_languages
        # return detected_languages if detected_languages else ["No language Found "]


    def print_detected_languages(self, text):
        detected_languages = AlphabetLanguageDetector().detect_language(text=text)
        print(detected_languages)

        language_count = len(detected_languages)
        full_name = AlphabetLanguageDetector().language_code_1 #To see the full name in output print

        if language_count == 0:
            print("No Languages Found ❌")

        elif language_count == 1:
            language_name = full_name.get(detected_languages[0], 'Unknown Full Form')
            print(f"One Language Found: {language_name}")

        elif language_count == 2:
            language_names = [full_name.get(lang, 'Unknown Full Form') for lang in detected_languages]
            print(f"Two Languages Found: {', '.join(language_names)}")

        elif language_count == 3:
            language_names = [full_name.get(lang, 'Unknown Full Form') for lang in detected_languages]
            print(f"3 Languages Found: {', '.join(language_names)}")

        elif language_count > 3:
            language_names = [full_name.get(lang, 'Unknown Full Form') for lang in detected_languages]
            print(f"{language_count} Number of Languages Found: {', '.join(language_names)}")

        else:
            print("It can do Multiple Tasks")






if __name__ == "__main__":

    text1 = f"kjhরপুপর"


    detected_languages = AlphabetLanguageDetector().detect_language(text=text1)
    print(detected_languages)

    print_detected_languages = AlphabetLanguageDetector().print_detected_languages(text=text1)
    