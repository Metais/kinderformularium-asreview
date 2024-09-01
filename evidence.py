

def check_if_not_exists(term, row):
    if (f"not {term}" in str(row["title"]).lower() or 
        f"not {term}" in str(row["abstract"]).lower()):
        return True
    else:
        return False

def insert_evidence(df):
    print("Checking for levels of evidence...")
    #Add empty evidence column to dataframe
    df["evidence"] = ""
    df["keyword for evidence"] = ""

    #Evidence definitions
    definitions = {"A1": ["meta-analysis", "meta analysis", "systematic-review", "systematic review"],
                "A2": ["randomized", "controlled", "double-blind", "double blind", " rct ", " rcts ", "placebo-controlled", "placebo controlled"],
                "B": ["comparative", "observational", "retrospective", "prospective"],
                "C": ["case report", "case-report", "case-series", "case series"]}

    #Loop through rows and definitions
    for index, row in df.iterrows():
        for key, value in definitions.items():

            #Check if any of the terms occur in title or abstract and write according evidence label to column
            for v in value:
                if v in str(row["title"]).lower() or v in str(row["abstract"]).lower():
                    # for specific instances... negatives may apply
                    if v == "randomized" and ("non-randomized" in str(row["title"]).lower() or
                                              "non-randomized" in str(row["abstract"]).lower()):
                        continue
                    if v in ["randomized", "double blind", "double-blind", "placebo-controlled", "placebo controlled"]:
                        if check_if_not_exists(v, row):
                            continue

                    df.loc[index, "evidence"] += key + " "
                    df.loc[index, "keyword for evidence"] += v + " "
                    break
        
        #If nothing is found, write X to evidence column
        if not df["evidence"][index]:
            df.loc[index, "evidence"] = "X"
            df.loc[index, "keyword for evidence"] = "-"

    return df
