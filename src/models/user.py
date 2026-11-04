# Файл src/models/user.py
from SFMShop.src.models.exceptions import ValidationError
class User:

    def __init__(self, name, email):
        self.name = name
        if '@' not in email:
            raise ValueError("Неверный формат email")
        self.email = email

    def get_email(self):
        return 'Пользователь: ' + self.name + ', Email: ' + self.email

    def set_email(self,email):
        if '@' not in email:
            raise ValidationError("Неверный формат email")
        self._email = email
