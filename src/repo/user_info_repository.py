import s3_repository


class UserInfoRepository(s3_repository.S3JsonRepository):
    def __init__(self, bucket_name, user_id, json_id):
        super().__init__(bucket_name, user_id, json_id)

    def save_user_urls(self, urls: list):
        assert urls is not None
        self.save('urls', urls)

    def save_user_keywords(self, keywords: list):
        assert keywords is not None
        self.save('keywords', keywords)

    def save_user_contacts(self, contacts: list):
        assert contacts is not None
        self.save('contacts', contacts)

    def get_user_urls(self):
        return self.get('urls')

    def get_user_keywords(self):
        return self.get('keywords')

    def get_user_contacts(self):
        return self.get('contacts')
