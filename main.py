import pprint
import boto3
from boto3.dynamodb.conditions import Key

def test_get_favorite_article():
    
    client = boto3.client(
        'dynamodb',
        aws_access_key_id='ASIAQI5MD4KIXVQBFXWW',
        aws_secret_access_key='QmTqQRLRsmK4wbP0F1MMjppwpO53LE11mOJX3Eyn',
        aws_session_token='IQoJb3JpZ2luX2VjEHgaDmNuLW5vcnRod2VzdC0xIkgwRgIhAOGC/lSZ+8He5b2XLWaBiUSSekPUKbK7u1Z/WaBDGYSiAiEAx1U4IzIlywbmEDi3RDqoTJpz7EVx8JG53LN22WZAoaAqzwIIpv//////////ARABGgwwMTkxNTE0NDY2NzMiDIQzjsygw5j1GGAkDyqjAilPwx+h6p3+tKqWzEoESH0XM+7oGPk+sfSp2Nn8NavAHOsxozI9Bkh0yCZPsCwrHRg2pWpuAUyn3yXw2mic7e34LU3hb32LyQjxiye3XLiHtLsbSS3Nofm4nzLqGK517pSf/fzddcYbtYVIDonV/gXsewiUDk8gbxOviyOJ0t2iVUrzpV/9ILVX+D4G8kQQQDIZX3bbFv8SAqI1yhSAcWypzvD9xOGT+95yvWnuMzm0HuvNhFaL17FPeyAl89cxoAKSavaPaEq9Ui97ehvXyBiIkXfTaAZHVBpEEfDSMFSaj7H13M/V+dcHf6f14CiR4bz4NwO9QjPwNEWkInBfyxAV7NyPnIzZcqw7oDVvpk3/FE4rS2jbWoWII6ZC9pb69QeIUzDh8ZSSBjqhAdQf6OGAR0ncmdu1EIBrjOMFQe4s3+J5TuFU42eL18Yg3zPAMhKS5T6rOEI3FtPl3CaAwm9L/gSnYBw8yK5zthVMCBEVj7QXlrHlYCTwp2vcvDV97XcKAHWs4RE9Gycvdz29vPVv0qgkUG6lvvvLHKBibm5Wnmw0qujDLbvOQbWU9gVCBjgzqiZcm1xQ+RqAz7Z/bNjOJTrhsZ+6Mb4jHS2h',
    )
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id='ASIAQI5MD4KIXVQBFXWW',
        aws_secret_access_key='QmTqQRLRsmK4wbP0F1MMjppwpO53LE11mOJX3Eyn',
        aws_session_token='IQoJb3JpZ2luX2VjEHgaDmNuLW5vcnRod2VzdC0xIkgwRgIhAOGC/lSZ+8He5b2XLWaBiUSSekPUKbK7u1Z/WaBDGYSiAiEAx1U4IzIlywbmEDi3RDqoTJpz7EVx8JG53LN22WZAoaAqzwIIpv//////////ARABGgwwMTkxNTE0NDY2NzMiDIQzjsygw5j1GGAkDyqjAilPwx+h6p3+tKqWzEoESH0XM+7oGPk+sfSp2Nn8NavAHOsxozI9Bkh0yCZPsCwrHRg2pWpuAUyn3yXw2mic7e34LU3hb32LyQjxiye3XLiHtLsbSS3Nofm4nzLqGK517pSf/fzddcYbtYVIDonV/gXsewiUDk8gbxOviyOJ0t2iVUrzpV/9ILVX+D4G8kQQQDIZX3bbFv8SAqI1yhSAcWypzvD9xOGT+95yvWnuMzm0HuvNhFaL17FPeyAl89cxoAKSavaPaEq9Ui97ehvXyBiIkXfTaAZHVBpEEfDSMFSaj7H13M/V+dcHf6f14CiR4bz4NwO9QjPwNEWkInBfyxAV7NyPnIzZcqw7oDVvpk3/FE4rS2jbWoWII6ZC9pb69QeIUzDh8ZSSBjqhAdQf6OGAR0ncmdu1EIBrjOMFQe4s3+J5TuFU42eL18Yg3zPAMhKS5T6rOEI3FtPl3CaAwm9L/gSnYBw8yK5zthVMCBEVj7QXlrHlYCTwp2vcvDV97XcKAHWs4RE9Gycvdz29vPVv0qgkUG6lvvvLHKBibm5Wnmw0qujDLbvOQbWU9gVCBjgzqiZcm1xQ+RqAz7Z/bNjOJTrhsZ+6Mb4jHS2h',
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