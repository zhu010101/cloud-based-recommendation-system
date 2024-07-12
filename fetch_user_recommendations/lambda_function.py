import json
# import http.client
from urllib.request import urlopen

def lambda_handler(event, context):
    try:
        # Parse the user id from the incoming query parameters
        user_id = event.get('queryStringParameters', {}).get('user_id')
        api_url = f"http://ec2-44-222-225-19.compute-1.amazonaws.com/recommend?user_id={user_id}"

        # Create a connection and request data
        response = urlopen(api_url)

        # Read and parse the JSON data
        data = json.loads(response.read())

        # Just return the json data, used to be html
        html_response = data

        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps(html_response)
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "headers": { "Content-Type": "application/json" },
            "body": str(e)
        }
