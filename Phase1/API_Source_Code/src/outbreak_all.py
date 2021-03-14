def disease_all(col):
    all_matches = []
    for doc in col.find({}):
        all_match = {
            'title': doc['title'].strip(),
            'date': doc['date'].strip(),
            'location': doc['location'].strip(),
            'region': doc['region'].strip(),
            'url': doc['url'].strip(),
            'disease': doc['disease'].strip(),
            'body': doc['body']
        }
        all_match_copy = all_match.copy()

        all_matches.append(all_match_copy)

    return all_matches
