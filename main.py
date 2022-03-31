import pprint
import boto3
from boto3.dynamodb.conditions import Key

def test_get_favorite_article():
    
    client = boto3.client(
        'dynamodb',
        aws_access_key_id='*********',
        aws_secret_access_key='****',
        aws_session_token='********',
    )
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id='*****',
        aws_secret_access_key='*****',
        aws_session_token='******',
    )
    
    ddb_exceptions = client.exceptions

    table = dynamodb.Table('favorite-article')
    try:
        # response = table.get_item(Key={'open_id': 'otzgU5K8ZTC9_qqFh4UVS3Rtht4Y', 'pii': 'S0140673620311879'})
        response = table.query(
            KeyConditionExpression=Key('open_id').eq('otzgU5K8ZTC9_qqFh4UVS3Rtht4Y')
        )   
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']


if __name__ == '__main__':
    articles = test_get_favorite_article()
    if articles:
        print("Get article succeeded:")
        for article in articles:
            print(f"\n{article['open_id']} : {article['pii']}")