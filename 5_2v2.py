import json
import os

class Model:
    
    def save(self, filename="model_data.json"):
        attributes = list(filter(lambda x: not x.startswith('_'), dir(self)))
        
        data = {}
        for attr in attributes:
            value = getattr(self, attr)
            if not callable(value):
                data[attr] = value
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"Сохранено в {filename}")
        return data
    
    def save_all(self, filename="model_data.json"):
        attributes = list(filter(lambda x: not x.startswith('_'), dir(self)))
        
        current_data = {}
        for attr in attributes:
            value = getattr(self, attr)
            if not callable(value):
                current_data[attr] = value
        
        existing_data = []
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)
                    if isinstance(existing_data, dict):
                        existing_data = [existing_data]
                    elif not isinstance(existing_data, list):
                        existing_data = []
            except (json.JSONDecodeError, FileNotFoundError):
                existing_data = []
        
        existing_data.append(current_data)
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
        
        print(f"Запись добавлена в {filename}. Всего записей: {len(existing_data)}")
        return existing_data
