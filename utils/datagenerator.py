from faker import Faker

fake = Faker()

def generate_user():

    return {
        "name": fake.first_name(),
        "email": fake.email(),
        "password": "Welcome@123",

        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": "UST",

        "address1": "Chennai Main Road",
        "address2": "Near Tech Park",

        "country": "India",

        "state": "Tamil Nadu",
        "city": "Chennai",

        "zipcode": "600001",
        "mobile": "9876543210"
    }