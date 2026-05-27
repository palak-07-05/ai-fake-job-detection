import pandas as pd
import re

def add_features(df):

    # =========================================
    # REQUIRED COLUMNS
    # =========================================

    columns = [
        'title',
        'company_profile',
        'description',
        'requirements',
        'benefits'
    ]

    # Add missing columns safely
    for col in columns:

        if col not in df.columns:
            df[col] = ""

    # =========================================
    # CREATE MAIN TEXT COLUMN
    # =========================================

    df['text'] = (

        df['title'].fillna('') + " " +

        df['company_profile'].fillna('') + " " +

        df['description'].fillna('') + " " +

        df['requirements'].fillna('') + " " +

        df['benefits'].fillna('')
    )

    # Convert to lowercase
    df['text'] = df['text'].astype(str).str.lower()

    # =========================================
    # SCAM FEATURES
    # =========================================

    # Payment / registration scams
    df['has_fee'] = df['text'].str.contains(
        r'fee|payment|registration|deposit|security amount|processing fee',
        regex=True,
        na=False
    ).astype(int)

    # Urgency scams
    df['has_urgent'] = df['text'].str.contains(
        r'urgent|immediate joining|quick hiring|apply now|limited seats',
        regex=True,
        na=False
    ).astype(int)

    # Money attraction scams
    df['has_money_words'] = df['text'].str.contains(
        r'earn money|high salary|income|weekly payout|daily payout|easy money',
        regex=True,
        na=False
    ).astype(int)

    # Remote scams
    df['has_remote_words'] = df['text'].str.contains(
        r'work from home|remote job|online work|part time online',
        regex=True,
        na=False
    ).astype(int)

    # Suspicious contact methods
    df['has_contact'] = df['text'].str.contains(
        r'whatsapp|telegram|dm now|call now|contact us',
        regex=True,
        na=False
    ).astype(int)

    # No experience required scams
    df['has_no_experience'] = df['text'].str.contains(
        r'no experience|freshers welcome|anyone can apply',
        regex=True,
        na=False
    ).astype(int)

    # Unrealistic promises
    df['has_unrealistic_offer'] = df['text'].str.contains(
        r'guaranteed job|instant joining|earn instantly|easy work',
        regex=True,
        na=False
    ).astype(int)

    # =========================================
    # TEXT FEATURES
    # =========================================

    # Exclamation marks
    df['exclamation_count'] = df['text'].str.count(r'!')

    # Capital words count
    df['capital_word_count'] = df['text'].apply(
        lambda x: sum(1 for word in x.split() if word.isupper())
    )

    # Text length
    df['text_length'] = df['text'].apply(len)

    # Word count
    df['word_count'] = df['text'].apply(
        lambda x: len(x.split())
    )

    # Average word length
    df['avg_word_length'] = df['text'].apply(
        lambda x: (
            sum(len(word) for word in x.split()) / len(x.split())
        ) if len(x.split()) > 0 else 0
    )

    # =========================================
    # REMOVE EXTRA SPACES
    # =========================================

    df['text'] = df['text'].str.replace(
        r'\s+',
        ' ',
        regex=True
    )

    return df