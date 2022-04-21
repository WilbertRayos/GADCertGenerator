from model.certificate_creator import CertificateCreator

class InputController:
    def __init__(self):
        self._name = ""
        self._sex = ""
        self._title = ""
        self._date = ""

    def submit_to_process(self):
        print(self._name)
        CertificateCreator(self._name, self._sex, self._title, self._date)

    @property
    def name(self):
        print(self.name)

    @name.setter
    def name(self, value):
        if value == "":
            return -1
        self._name = value

    @property
    def sex(self):
        print(self.sex)

    @sex.setter
    def sex(self, value):
        if value == "":
            return -1
        self._sex = value

    @property
    def title(self):
        print(self._title)

    @title.setter
    def title(self, value):
        if value == "":
            return -1
        self._title = value

    @property
    def date(self):
        print(self.date)

    @date.setter
    def date(self, value):
        if value == "":
            return -1
        self._date = value