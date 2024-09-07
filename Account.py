import numpy as np
import firebase_admin
from firebase_admin import credentials, db

creds = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(creds, {
    "databaseURL":"https://house-pricing-database-6f957-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

class Account():
    def __init__(self):
        self.id_number = None

    # Get user credentials info
    def read_credentials(self):
        ref = db.reference("account_credentials")
        accounts_credentials = ref.get()
        
        for account in accounts_credentials.items():
            if account["unique_id"] == self.id_number:
                return account["username"]
        return None

    # Create Account Functions
    def create_account_username_password(self, parse_username, parse_password, parse_repassword):

        self.id_number = np.random.randint(1000, 10000)
        retype_password = parse_repassword

        account_credentials = {
            "username": parse_username,
            "password": parse_password,
            "unique_id": self.id_number
        }

        if account_credentials["password"] == retype_password:
            ref = db.reference("account_credentials")
            ref.push(account_credentials)
            return True
        else:
            return False

    # Create Account Data Functions    
    def create_account_data(self, parse_nama, parse_pekerjaan, parse_email, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan):
        account_data = {
            "unique_id": self.id_number, # Should Identify the Account of an user ideally yeah?
            "full_name": parse_nama,
            "email": parse_email,
            "job": parse_pekerjaan,
            "salary": parse_gaji,
            "job_address": parse_tempat_kerja,
            "tanggungan": parse_tanggungan,
            "beban_cicilan": parse_cicilan,
            "tabungan": parse_tabungan
        }

        ref = db.reference("account_data")
        ref.push(account_data)
        return True
    
    # Login Functions
    def user_login(self, parsed_username, parsed_password):
        accounts_ref = db.reference("account_credentials")
        account_credentials = accounts_ref.get()
        
        for account_data in account_credentials.items():
            if account_data["username"] == parsed_username and account_data["password"] == parsed_password:
                self.id_number = account_data["unique_id"]
                return True
        return False
        
    # Changing User Data Functions
    def change_user_data(self, parse_nama, parse_pekerjaan, parse_email, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan):
        ref = db.reference("account_data")
        accounts_data = ref.get()
        
        for account_id, account in accounts_data.items():
            if account["unique_id"] == self.id_number:
                updated_account_data = {
                    "unique_id": self.id_number,
                    "full_name": parse_nama,
                    "email": parse_email,
                    "job": parse_pekerjaan,
                    "salary": parse_gaji,
                    "job_address": parse_tempat_kerja,
                    "tanggungan": parse_tanggungan,
                    "beban_cicilan": parse_cicilan,
                    "tabungan": parse_tabungan
                }
                ref.child(account_id).update(updated_account_data)
                return True

    # Search email
    def search_user_email(self, parse_email):
        ref = db.reference("account_data")
        accounts_data = ref.get()
        
        for account in accounts_data.items():
            if account["email"] == parse_email:
                return True
            return False

    # Reset password function
    def reset_user_password(self, parse_password, parse_repassword):
        if parse_password == parse_repassword:
            ref = db.reference("account_credentials")
            accounts_credentials = ref.get()
            for account_id, account in accounts_credentials.items():
                if account["unique_id"] == self.id_number:
                    ref.child(account_id).update({"password": parse_password})
                    return True
            return False