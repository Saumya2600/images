import boto3
import os

def upload_image_to_s3(bucket_name, local_file_path, s3_key):
    s3_client = boto3.client('s3')
    
    try:
        # Get the image file name from the local file path
        file_name = os.path.basename(local_file_path)
        
        # Upload the image to S3
        with open(local_file_path, 'rb') as file:
            s3_client.upload_fileobj(file, bucket_name, file_name)
        
        print(f"Image uploaded successfully to S3 bucket '{bucket_name}' with key '{file_name}'")
    except Exception as e:
        print(f"Error uploading image: {str(e)}")

# Replace the following variables with your values
bucket_name = "main-upload-user"  # Replace with your S3 bucket name
local_file_path = "C:/Users/user/Downloads/h11.jpeg"  # Replace with the local path of the image file
# local_file_path = "https://www.onemedical.com/media/images/woman-wearing-mask.original.jpg"
s3_key = "image.jpg"  # Replace with the desired S3 key (object name) for the uploaded image in the root

upload_image_to_s3(bucket_name, local_file_path, s3_key)
