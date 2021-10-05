class Student:
    first_name = ''
    last_name = ''
    class_number = ''
    is_late = False

    def update_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def update_attendance(cls, late):
        cls.is_late = late

