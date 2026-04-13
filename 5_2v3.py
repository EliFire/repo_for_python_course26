import json
import os

class Model:
    _instances = {}

    def __init__(self):
        class_name = self.__class__.__name__
        if class_name not in self._instances:
            self._instances[class_name] = []
        self._instances[class_name].append(self)

    @classmethod
    def save_all(cls, filename=None):
        if filename is None:
            filename = f"{cls.__name__.lower()}s.json"

    all_data = []
    for instance in cls._instances.get(cls.__name__, []):
        attributes = list(filter(lambda x: not x.startswith('_'), dir(instance)))
        data = {}
        for attr in attributes:
            value = getattr(instance, attr)
            if not callable(value):
                data[attr] = value
        data['_saved_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all_data.append(data)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)

    print(f"Сохранено {len(all_data)} объектов в {filename}")
    return all_data

    @classmethod
    def get_all(cls, filename=None):
        if filename is None:
            filename = f"{cls.__name__.lower()}s.json"

        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    class Post(Model):
        def __init__(self, title, content, author="Unknown"):
            super().__init__()
            self.title = title
            self.content = content
            self.author = author