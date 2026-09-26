import boto3
import uuid
import os

S3_BUCKET = os.environ.get('S3_BUCKET')
AWS_REGION = 'ap-southeast-1'

def upload_image(file):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    filename = f"{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}"
    s3.upload_fileobj(
        file,
        S3_BUCKET,
        filename,
        ExtraArgs={'ContentType': file.content_type}
    )
    url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"
    return url