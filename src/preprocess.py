import re

def clean_text(text):

    # =========================================
    # HANDLE NONE VALUES
    # =========================================

    if text is None:
        return ""

    # Convert to string & lowercase
    text = str(text).lower()

    # =========================================
    # REMOVE URLS
    # =========================================

    text = re.sub(r'http\S+|www\S+', ' ', text)

    # =========================================
    # REMOVE EMAILS
    # =========================================

    text = re.sub(r'\S+@\S+', ' ', text)

    # =========================================
    # REMOVE NUMBERS
    # =========================================

    text = re.sub(r'\d+', ' ', text)

    # =========================================
    # REMOVE SPECIAL CHARACTERS
    # =========================================

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # =========================================
    # REMOVE EXTRA SPACES
    # =========================================

    text = re.sub(r'\s+', ' ', text)

    # Final cleaned text
    return text.strip()