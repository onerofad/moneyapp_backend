from silasdk import App
from silasdk import User
from silasdk import Transaction

silaApp = App("SANDBOX", "b6a9845288190ba96eaf01517c6c867276e3dbb7df720170e14b70fa15bded20", "moneyapp_handle")

# Individual User

payload = {
  "country": "US",
  "user_handle": 'onero.silamoney.eth',    # Required: Must not be already in use
  "first_name": 'onero',                # Required
  "last_name": 'fad',                    # Required
  "entity_name": 'onero fad',          # Required
  "identity_value": "123453333",          # Required (SSN)
  "identity_alias": "SSN",  
  "phone": 1234567880,                    # Required:  Must be a valid phone number (format not enforced)
  "email": "onero@email.com",              # Required:  Must be a valid email address
  "address_alias": "default",  
  "street_address_1": '123 Main Street',  # Required:  Must be a valid USPS mailing address
  "city": 'New City',                     # Required:  Must be a valid US City matching the zip
  "state": 'OR',                          # Required:  Must be a 2 character US State abbr.
  "postal_code": 97204,                   # Required:  Must be a valid US Postal Code
  "crypto_address": '0x9361005EA8041821edF4BeaF5B0518d9e75AeB13',        # Required:  Must be a valid ethereum 20 byte address starting with 0x
  "crypto_alias": "python_wallet_1",
  "birthdate": "1990-05-19",              # Required
  "session_identifier": "<session_key uuid>"  # Required only for Instant ACH V2 else optional

}

# Make sure silaApp is initialized with registered app_private_key and app_handle.
info = User.register(silaApp, payload)

print(info)

### Success Response Object