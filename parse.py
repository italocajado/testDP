import json
from pymongo import MongoClient
from dataclasses import dataclass
import time

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float

def parse_json_and_insert(file_path):
    client = MongoClient('mongodb+srv://italocajado:ES6pyI4n7XG43rSL@cluster0.ttz2o.mongodb.net/')
    db = client['mydatabase']
    collection = db['users']
    
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        for item in data['users']:  
            roles = []
            if item.get('is_user_admin'):
                roles.append('admin')
            if item.get('is_user_manager'):
                roles.append('manager')
            if item.get('is_user_tester'):
                roles.append('tester')
            
            preferences = UserPreferences(timezone=item.get('user_timezone', 'UTC'))

            user = User(
                username=item['user'],
                password=item['password'],
                roles=roles,
                preferences=preferences,
                active=item.get('is_user_active', True),
                created_ts=time.mktime(time.strptime(item['created_at'], "%Y-%m-%dT%H:%M:%SZ"))
            )
            user_doc = {
                'username': user.username,
                'password': user.password,
                'roles': user.roles,
                'preferences': {
                    'timezone': user.preferences.timezone
                },
                'active': user.active,
                'created_ts': user.created_ts
            }
            collection.insert_one(user_doc)

if __name__ == "__main__":
    parse_json_and_insert('udata.json')  
