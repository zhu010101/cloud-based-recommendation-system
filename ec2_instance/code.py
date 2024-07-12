import sys
import boto3
from flask import Flask, request, jsonify
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from collections import defaultdict
from surprise import accuracy
import pandas as pd
import codecs

sys.path.append("/home/ec2-user/.local/lib/python3.9/site-packages")

app = Flask("APAN5450App")

@app.route('/recommend', methods=['GET'])
def recommend():
    
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    # Query the DynamoDB table for 20 rows of data
    response = dynamodb.scan(
        TableName='amzn-reviews',
        Limit=200000
    )

    # Extract the items from the response
    df = pd.DataFrame(response.get('Items', []))
    
    reader = Reader(rating_scale=(1, 5))

    df.drop(['id', 'timestamp'], axis=1, inplace=True)
    df = df.rename(columns={'asin': 'product_id'})
    df = df.rename(columns={'event_type': 'title'})
    # Extracting values from dictionary objects in DataFrame
    df['user_id'] = df['user_id'].apply(lambda x: x['S'])
    df['product_id'] = df['product_id'].apply(lambda x: x['S'])
    df['rating'] = df['rating'].apply(lambda x: float(x['S']))
    # Add similar lines for other fields you want to extract and transform
    df['parent_asin'] = df['parent_asin'].apply(lambda x: x['S'])
    df['title'] = df['title'].apply(lambda x: codecs.decode(x['S'], 'unicode_escape'), convert_dtype=False)
    df['text'] = df['text'].apply(lambda x: x['S'].replace('<br /><br />', ''))

    data = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)

    # Split the data into train and test sets
    trainset, testset = train_test_split(data, test_size=0.2)
    # Train the SVD algorithm
    algo = SVD()
    algo.fit(trainset)

    user_id = request.args.get('user_id')
    
    # Get all unique item ids
    all_product_ids = set(df['product_id'].unique())
    
    # Get item ids already reviewed by the user
    reviewed_product_ids = set(df[df['user_id'] == user_id]['product_id'].unique())
    
    # Get item ids not reviewed by the user
    not_reviewed_product_ids = all_product_ids - reviewed_product_ids
    
    # Make predictions for items not reviewed by the user
    user_predictions = algo.test([(user_id, product_id, 0) for product_id in not_reviewed_product_ids])
    
    # Get top 5 recommendations for the user with recommendation score
    top_n = sorted(user_predictions, key=lambda x: x.est, reverse=True)[:5]
    
    recommendations = []
    for pred in top_n:
        product_info = df[df['product_id'] == pred.iid].iloc[0]  # Get item info from DataFrame
        recommendation = {
            "product_id": pred.iid,
            "score": round(pred.est, 2),
            "title": product_info['title'],
            "text": product_info['text'],
            "parent_asin": product_info['parent_asin']
        }
        recommendations.append(recommendation)
    
    return jsonify({"user_id": user_id, "recommendations": recommendations})


app.run(host='0.0.0.0', port=80)

