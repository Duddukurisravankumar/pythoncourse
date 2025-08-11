import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("bankmanagement/data.json")
    data = []

    @classmethod
    def load_data(cls):
        if cls.database.exists():
            try:
                with open(cls.database) as f:
                    cls.data = json.load(f)
            except json.JSONDecodeError:
                print("Corrupted data file. Starting fresh.")
                cls.data = []
        else:
            print("Data file does not exist. Creating a new one.")
            cls.data = []

    @classmethod
    def save_data(cls):
        cls.database.parent.mkdir(parents=True, exist_ok=True)
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def generate_account_number():
        parts = random.choices(string.ascii_uppercase, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(parts)
        return ''.join(parts)

    @classmethod
    def find_user(cls, acc_no, pin):
        return next((user for user in cls.data if user['accnumber'] == acc_no and user['pin'] == pin), None)

    def create_account(self, name, age, phone, pin):
        if age <= 18 or len(str(pin)) < 4:
            return {"success": False, "message": "You must be over 18 and PIN must be at least 4 digits."}

        acc_number = self.generate_account_number()
        new_user = {
            "name": name,
            "age": age,
            "phno": phone,
            "pin": pin,
            "accnumber": acc_number,
            "balance": 0
        }
        Bank.data.append(new_user)
        Bank.save_data()
        return {"success": True, "user": new_user}

    def deposit(self, acc_no, pin, amount):
        user = Bank.find_user(acc_no, pin)
        if not user:
            return {"success": False, "message": "Invalid credentials."}

        if not (0 < amount <= 10000):
            return {"success": False, "message": "Deposit amount must be between 1 and 10,000."}

        user['balance'] += amount
        Bank.save_data()
        return {"success": True, "balance": user['balance']}

    def withdraw(self, acc_no, pin, amount):
        user = Bank.find_user(acc_no, pin)
        if not user:
            return {"success": False, "message": "Invalid credentials."}
        if amount <= 0 or amount > user['balance']:
            return {"success": False, "message": "Invalid withdrawal amount."}

        user['balance'] -= amount
        Bank.save_data()
        return {"success": True, "balance": user['balance']}

    def get_details(self, acc_no, pin):
        user = Bank.find_user(acc_no, pin)
        if not user:
            return {"success": False, "message": "Invalid credentials."}
        return {"success": True, "user": user}

    def update_details(self, acc_no, pin, field, new_value):
        user = Bank.find_user(acc_no, pin)
        if not user:
            return {"success": False, "message": "Invalid credentials."}
        if field not in ["name", "phno", "pin"]:
            return {"success": False, "message": "Invalid field."}
        user[field] = new_value
        Bank.save_data()
        return {"success": True, "user": user}

    def delete_account(self, acc_no, pin):
        user = Bank.find_user(acc_no, pin)
        if not user:
            return {"success": False, "message": "Invalid credentials."}

        Bank.data.remove(user)
        Bank.save_data()
        return {"success": True, "message": "Account deleted successfully."}


# Load data once at start
Bank.load_data()
