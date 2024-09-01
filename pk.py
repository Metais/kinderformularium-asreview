import pandas as pd
import re

keywords = [
    r'pharmacokinetic.*', r'exposure', r'clearance', r'\bCL\b', r'\bCl\b', r'volume of distribution', 
    r'\bVd\b', r'\bVss\b', r'plasma concentration', r'\bCmax\b', r'\bTmax\b', 
    r'area under the curve', r'\bAUC\b', r'half-life', r'\bt1/2\b'
]

# Function to detect keywords
def keyword_detect(text):
    for keyword in keywords:
        if re.search(keyword, text, re.IGNORECASE):
            return keyword
    return None

# Apply the detection function to 'title' and 'abstract' columns and store the results
def find_keywords(row):
    if pd.notna(row['title']) and row['title'] != '':
        title_keyword = keyword_detect(row['title'])
    else:
        title_keyword = None
    if not title_keyword and pd.notna(row['abstract']) and row['abstract'] != '':
        abstract_keyword = keyword_detect(row['abstract'])
    else:
        abstract_keyword = None

    if title_keyword:
        return (1, title_keyword)
    elif abstract_keyword:
        return (1, abstract_keyword)
    else:
        return (0, None)

def process_pk(df):
    print("Checking for levels of pharmacokinetics...")
    # Apply the function and expand the results into two new columns
    df[['PK', 'PK_keyword']] = df.apply(lambda row: pd.Series(find_keywords(row)), axis=1)
    
    return df