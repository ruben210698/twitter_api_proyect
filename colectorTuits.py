import requests
import re
import mySecrets

token = mySecrets.token_twitter
header = {}
header['Authorization'] = f"Bearer {token}"


def generate_file_content_tuits(name_file, query, mode = "w+"):
    num_rows = 0
    list_added_tweets = []

    for i in range(3): # Para más posibilidades de encontrar tweets
        if i == 1:
            query = query + "&result_type=popular"
        if i == 2:
            query = query + "&result_type=recent"
        r = requests.get(f'https://api.twitter.com/1.1/search/tweets.json?q={query}', headers = header)
        json_ids = r.json()
        file_twits = open("generated_files/" + name_file, mode)

        for row in json_ids['statuses']:

            id_tuit = row['id']
            text = requests.get(f'https://api.twitter.com/2/tweets/{id_tuit}', headers=header).json()['data']['text']\
                    .replace("\xc3\xa1", 'a').replace("\xc3\xa9", 'e').replace("\xc3\xad", 'i')\
                    .replace("\xc3\xb3", 'o').replace("\xc3\xba", 'u').replace("\n", " . ")

            text = re.sub("RT @..*: ", "", text) # Remove "retweet prefix"
            text = re.sub("@[A-Za-z0-9]*", "", text)  # Remove mentions
            text = re.sub("http[://.A-Za-z0-9]*", "", text)  # Remove url
            text = text.replace("\n", " . ")
            if list_added_tweets.__contains__(text):
                # If the twwet already added
                continue
            num_rows += 1
            list_added_tweets.append(text)
            if text != '\n' and text != '':
                file_twits.write(text + "\n")


    return num_rows

