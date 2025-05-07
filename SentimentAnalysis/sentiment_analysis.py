import requests, json 

def sentiment_analyzer(text_to_analyse: str) -> dict[str,any]:
    ''' This function executes the sentiment analysis over the text
        provided by the user. It returns a dictionary with the label
        and its confidence score.
    '''

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    
    response = requests.post(url, json = myobj, headers = header)  # Send a POST request to the API with the text and headers
    formated = json.loads(response.text)

    label = formated.get("documentSentiment", {}).get("label", "")
    score = formated.get("documentSentiment", {}).get("score", "")

    return {'label': f"{label}", 'score': f"{score}"}  # Return the response text from the API