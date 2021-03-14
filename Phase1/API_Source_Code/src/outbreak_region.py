def region_filter(region_str, col):
    region_matches = []
    if region_str == '':
        return region_matches
    else:
        for doc in col.find({"region": region_str}):
            region_match = {
                'title': doc['title'].strip(),
                'date': doc['date'].strip(),
                'location': doc['location'].strip(),
                'region': doc['region'].strip(),
                'url': doc['url'].strip(),
                'disease': doc['disease'].strip()
            }

            region_match_copy = region_match.copy()

            region_matches.append(region_match_copy)

        return region_matches
