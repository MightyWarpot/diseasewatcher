def location_filter(location_str, col):
    location_matches = []
    if location_str == '':
        return location_matches

    # location_matches = []
    else:
        for doc in col.find({"location": location_str}):
            location_match = {
                'title': doc['title'].strip(),
                'date': doc['date'].strip(),
                'location': doc['location'].strip(),
                'region': doc['region'].strip(),
                'url': doc['url'].strip(),
                'disease': doc['disease'].strip()
            }
            location_match_copy = location_match.copy()

            location_matches.append(location_match_copy)

        return location_matches