import json
import os


class UserModel:

    id       = int
    names    = str
    lastname = str
    age      = int
    email    = str

    def __init__(self, id, names, lastname, age, email):
        self.id       = id
        self.names    = names
        self.lastname = lastname
        self.age      = age
        self.email    = email

    def get_id_for_next_new_user(self):
        json_data = self.load_data()
        len_list = len(json_data['users']) - 1
        last_dict = json_data['users'][len_list]
        id_value = last_dict['id'] + 1
        return id_value

    def create_json(self):
        dict = {
                "users": [
                    {
                    "id":        self.id,
                    "names":     self.names,
                    "lastnames": self.lastname,
                    "age":       self.age,
                    "email":     self.email
                },
            ]
        }
        jsonString = json.dumps(dict)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    
    def create_dict(self):
        dict = {
                "id":        self.id,
                "names":     self.names,
                "lastnames": self.lastname,
                "age":       self.age,
                "email":     self.email
            }
        return dict

    def load_data(self):
        with open('data.json', 'r+') as json_data:
            data_dict = json.load(json_data)
            return data_dict

    def save_data(self, json_data):
        with open('data.json', 'w') as f:
            json.dump(json_data, f, indent=4)
            f.close()

    def get_item_from_json(self, id):
        json_data = self.load_data()
        for i in json_data['users']:
            if i["id"] == id:
                return i

    def create_user(self, dict):
        with open('data.json', 'r+') as json_data:
            data_dict = json.load(json_data)
            data_dict['users'].append(dict)
            json_data.seek(0)
            json.dump(data_dict, json_data, indent=4)
            json_data.close()
            
    def modify_user(self, id, update_data):
        json_data = self.load_data()
        for dict in json_data['users']:
            if dict['id'] == id:
                index = json_data["users"].index(dict)
                json_data["users"][index] = update_data
                break
        self.save_data(json_data)

    def delete_user(self, id):
        with open('data.json', 'r+') as json_data:
            data_dict = json.load(json_data)
            json_data.close()
        os.remove('data.json')
        for dict in data_dict['users']:
            if dict['id'] == id:
                data_dict["users"].remove(dict)
                break
        self.save_data(data_dict)
        
    def read_user(self, id):
        json_data = self.load_data()
        for dict in json_data['users']:
            if dict['id'] == id:
                return dict

    def display_all_users(self):
        json_data = self.load_data()
        return json_data