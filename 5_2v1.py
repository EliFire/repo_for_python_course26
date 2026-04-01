import json

class Model:
    
    def save(self, filename="model_data.json"):
         attributes = list(filter(lambda x: not x.startswith('_'), dir(self)))
        
        data = {}
        for attr in attributes:
            value = getattr(self, attr)
            data[attr] = value
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"Сохранено в {filename}")
        return data

