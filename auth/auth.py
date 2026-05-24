import streamlit_authenticator as stauth

# USER DATA

names = ["Palak"]
usernames = ["palak"]

# PASSWORDS

passwords = ["jobshield123"]

# HASH PASSWORDS

hashed_passwords = stauth.Hasher(passwords).generate()

# AUTHENTICATOR

authenticator = stauth.Authenticate(
    {
        "usernames": {
            usernames[0]: {
                "name": names[0],
                "password": hashed_passwords[0]
            }
        }
    },
    "jobshield_cookie",
    "abcdef",
    cookie_expiry_days=30
)