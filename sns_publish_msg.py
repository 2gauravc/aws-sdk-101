
import boto3
import json 
import decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
sns = boto3.client('sns', region_name = 'us-east-1')

response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:726621848335:newfileupload',
    Message='Hi from Python',
    Subject='SNS Python')

print(json.dumps(response, indent=4, cls=DecimalEncoder))
