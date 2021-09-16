class Text_processor:
    def __init__(self):
        self._punktuation = '.,!?;:'

    def __is_punctuation(self, char):
        return char in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punctuation(char):
                continue
            clean_text += char
        return clean_text


p = Text_processor()
print(p.get_clean_string('Hello, world! Result: ?'))
