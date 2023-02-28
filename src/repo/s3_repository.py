import json

import boto3


class S3Repository:
    def __init__(self, bucket_name, user_id):
        self.bucket_name = bucket_name
        self.user_id = user_id
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(self.bucket_name)

    def save(self, key, value):
        self.bucket.put_object(Key=f'{self.user_id}/{key}', Body=value)

    def get(self, key):
        obj = self.bucket.Object(f'{self.user_id}/{key}')
        return obj.get()['Body'].read().decode('utf-8')

    def delete(self, key):
        self.bucket.Object(f'{self.user_id}/{key}').delete()

    def save_all(self, key_value_pairs: dict):
        for key, value in key_value_pairs.items():
            self.save(key, value)

    def get_all(self, keys: list):
        key_value_pairs = {}
        for key in keys:
            key_value_pairs[key] = self.get(key)
        return key_value_pairs

    def delete_all(self, keys: list):
        for key in keys:
            self.delete(key)


class S3JsonRepository(S3Repository):
    def __init__(self, bucket_name, user_id, file_key):
        super().__init__(bucket_name, user_id)
        self.file_key = file_key

    def save(self, key, value):
        json_val = super().get(self.file_key)
        json_val[key] = value
        super().save(self.file_key, json.dumps(json_val))

    # exception: None value exception can occur
    def get(self, key):
        json_val = json.loads(super().get(self.file_key))
        return json_val.get(key)

    def delete(self, key):
        json_val = super().get(self.file_key)
        del json_val[key]
        super().save(self.file_key, json.dumps(json_val))

    def delete_all(self, keys: list):
        json_val = super().get(self.file_key)
        for key in keys:
            del json_val[key]
        super().save(self.file_key, json.dumps(json_val))

    def save_all(self, key_value_pairs: dict):
        json_val = super().get(self.file_key)
        for key, value in key_value_pairs.items():
            json_val[key] = value
        super().save(self.file_key, json.dumps(json_val))

    def get_all(self, keys: list):
        json_val = json.loads(super().get(self.file_key))
        key_value_pairs = {}
        for key in keys:
            if value := json_val.get():
                key_value_pairs[key] = value
        return key_value_pairs
