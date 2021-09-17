import text_loader


class DataInterface:
    def __init__(self):
        self.__text_loader = text_loader.TextLoader()

    def process_text(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ['Hello, i .am Jhon', 'Hey, what is! the weather today?']
ct = di.process_text(t)
