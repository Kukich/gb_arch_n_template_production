from abc import ABC, abstractmethod

class Language(ABC):
    def menu_headers(self):
        return [
             {'language': self.language, 'level': 'senior', 'name': f'Курс профессионального {self.language} программиста'},
             {'language': self.language, 'level': 'middle', 'name': f'Курс профессионального {self.language} программиста'},
             {'language': self.language, 'level': 'junior', 'name': f'Курс профессионального {self.language} программиста'}
        ]
    @abstractmethod
    def create_senior(self):
        pass

    @abstractmethod
    def create_middle(self):
        pass

    @abstractmethod
    def create_junior(self):
        pass





class PythonEducation(Language):
    def __init__(self):
        self.language = 'python'

    def create_junior(self):
        return {'text': 'Это страница курса для начинающего питон программиста'}

    def create_middle(self):
        return {'text': 'Это страница курса для продвинутого питон программиста'}

    def create_senior(self):
        return {'text': 'Это страница курса для профессионального питон программиста'}

class JavaEducation(Language):
    def __init__(self):
        self.language = 'java'

    def create_junior(self):
        return {'text': 'Это страница курса для начинающего джава программиста'}

    def create_middle(self):
        return {'text': 'Это страница курса для продвинутого джава программиста'}

    def create_senior(self):
        return {'text': 'Это страница курса для профессионального джава программиста'}

class JavaScriptEducation(Language):
    def __init__(self):
        self.language = 'javascript'

    def create_junior(self):
        return {'text': 'Это страница курса для начинающего джаваскрипт программиста'}

    def create_middle(self):
        return {'text': 'Это страница курса для продвинутого джаваскрипт программиста'}

    def create_senior(self):
        return {'text': 'Это страница курса для профессионального джаваскрипт программиста'}

class EducationFabric:
    def __init__(self,language):
        self.object =None
        if(language == 'python'):
            self.object = PythonEducation()
        elif(language == 'java'):
            self.object = JavaEducation()
        elif (language == 'javascript'):
            self.object = JavaScriptEducation()

    def create_level_page(self,level):
        if(level == 'senior'):
            return self.object.create_senior()
        elif(level == 'middle'):
            return self.object.create_middle()
        elif (level == 'junior'):
            return self.object.create_junior()

