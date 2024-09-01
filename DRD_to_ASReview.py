import os
import re
import docx

from RBA_to_ASReview import create_csv_path, pubmed2csv

def getDRDs():
    directory = os.path.join(os.getcwd(), "DRDs")

    docx_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.docx') and not file.startswith('~$'):
                docx_files.append(os.path.join(root, file))

    return docx_files

def remove_numbered_prefix(text):
    pattern = r'^\d+\.\t'
    return re.sub(pattern, '', text)

def extract_references_from_DRD(doc_path):
    # Load the document
    doc = docx.Document(doc_path)
    
    references = []
    in_references = False
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        
        # Check for reference section headers
        if re.match(r'(?i)references?|referenties?|reference\s+list', text):
            in_references = True
            continue
        
        # append each reference
        if in_references and text:
            # If it's in a numbered list, take that out
            text = remove_numbered_prefix(text)
            references.append(text)
        
        # Check for end of reference section
        if in_references and text == '':
            in_references = False
    
    return references

def extract_title(reference):
    # Regular expression to capture the title between authors and journal name
    # We assume:
    # 1. The title starts after the first period after author names (ignoring 'et al.')
    # 2. The title ends where a pattern for journal name or year starts
    match = re.search(r'\.\s(.*?)\s(?:\d{4}|\d+\(\d+\):|\w+ J \w+)', reference)
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    drd_files = getDRDs()

    for i, drd_path in enumerate(drd_files):
        print(f"Processing DRD #{i+1}...")

        csv_path = create_csv_path(drd_path)

        # Collect the references from the DRD file
        references_list = extract_references_from_DRD(drd_path)
        # Remove duplicates
        references_list = list(set(references_list))
        # Extract just the title
        references_list_titles = [extract_title(x) for x in references_list]
        # Turn into list of dicts with ref['title']
        references_list_titles = [{'p_title': x} for x in references_list_titles]
        # Call pubmed2csv and get proper reference format from PubMed
        pubmed2csv(references_list_titles, csv_path, max_hash_distance=12)

    input("Press Enter to exit...")
