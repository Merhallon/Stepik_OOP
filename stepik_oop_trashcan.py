# Создайте класс  File, у которого есть:
#
# метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name.
# Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False

# метод  restore_from_trash,
# который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False
# метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
# метод read, который
# печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
# метод write, который принимает значение content для записи и
# печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            return print(f'ErrorReadFileDeleted({self.name})')
        if self.in_trash:
            return print(f'ErrorReadFileTrashed({self.name})')
        if not self.in_trash and not self.is_deleted:
            return print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            return print(f'ErrorWriteFileDeleted({self.name})')
        if self.in_trash:
            return print(f'ErrorWriteFileTrashed({self.name})')
        if not self.in_trash and not self.is_deleted:
            return print(f'Записали значение {content} в файл {self.name}')




# f1 = File('puppies.jpg')
# print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
# f1.read()  # Прочитали все содержимое файла puppies.jpg
# f1.remove()  # Файл puppies.jpg был удален
# f1.read()  # ErrorReadFileDeleted(puppies.jpg)
#
f2 = File('cat.jpg')
f2.write('hello')  # Записали значение hello в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)