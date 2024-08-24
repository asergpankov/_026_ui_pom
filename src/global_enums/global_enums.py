from enum import Enum


class SelectablePageEnums(Enum):
    LIST_NAMES = ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus', 'Porta ac consectetur ac']
    GRID_NAMES = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']


class MenuPageEnums(Enum):
    LIST_NAMES = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                  'Sub Sub Item 2', 'Main Item 3']


class LoginPageEnums(Enum):
    CREDS = [('user', 'pass_123'), ('123', 'pass_123'), ('@#', 'pass_123')]


class StudentRegistrationFormPageEnums(Enum):
    SUBJECTS = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics", ]
