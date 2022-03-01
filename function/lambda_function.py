from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting AWS Lambda functions\n---------------------------------------------')

    if event["input"] == "Hello":
        return "Hello LIVERPOOL 12345...."

    if event["input"] == "Hi":
        return "Hi LIVERPOOL..."

    else:
        raise
