def disease_filter(disease_str, col):
    disease_matches = []

    if disease_str == '':
        return disease_matches
    else:
        for doc in col.find({"disease": disease_str}):
            disease_match = {
                'title': doc['title'].strip(),
                'date': doc['date'].strip(),
                'location': doc['location'].strip(),
                'region': doc['region'].strip(),
                'url': doc['url'].strip(),
                'disease': doc['disease'].strip()
            }

            disease_match_copy = disease_match.copy()

            disease_matches.append(disease_match_copy)

        return disease_matches
















    for doc in col.find({"disease": disease_str}):
        # print(doc)
        # print(doc['title'].strip())
        # print(doc['location'].strip())
        # print(doc['date'].strip())

        disease_match = {
            'title': doc['title'].strip(),
            'date': doc['date'].strip(),
            'location': doc['location'].strip(),
            'region': doc['region'].strip(),
            'url': doc['url'].strip(),
            'disease': doc['disease'].strip()
        }

        disease_match_copy = disease_match.copy()

        disease_matches.append(disease_match_copy)

    return disease_matches
    # return col
    
