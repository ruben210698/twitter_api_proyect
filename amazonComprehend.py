import boto3



def get_weights_sentiment_analysis(name_file, language):
    client = boto3.client('comprehend', region_name="eu-west-1")
    fd = open(name_file)
    list_lines = [a for a in fd.readlines()]

    final_respone = {'Positive':0, 'Negative':0, 'Neutral': 0, 'Mixed':0}
    for i in range(0, list_lines.__len__(), 20):
        response_list = client.batch_detect_sentiment(
            TextList = list_lines[i: i+20],
            LanguageCode=language
        )['ResultList']
        for response in response_list:
            values = response['SentimentScore']
            final_respone['Positive'] = final_respone['Positive'] + values['Positive']
            final_respone['Negative'] = final_respone['Negative'] + values['Negative']
            final_respone['Neutral'] = final_respone['Neutral'] + values['Neutral']
            final_respone['Mixed'] = final_respone['Mixed'] + values['Mixed']
    return final_respone

