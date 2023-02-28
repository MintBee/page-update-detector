from s3_repository import S3Repository


class LastPageRepository(S3Repository):
    def __init__(self, bucket_name, user_id):
        super().__init__(bucket_name, user_id)

    def save_last_page(self, page_url, html_page):
        assert page_url is not None and html_page is not None
        self.save(f'last-pages/{page_url}', html_page)

    def get_last_page(self, page_url):
        assert page_url is not None
        return self.get(f'last-pages/{page_url}')

    def save_last_pages(self, pages: dict):
        assert pages is not None
        for page_url, html_page in pages.items():
            self.save_last_page(page_url, html_page)

    def get_last_pages(self, page_urls: list):
        assert page_urls is not None
        pages = {}
        for page_url in page_urls:
            pages[page_url] = self.get_last_page(page_url)
        return pages
