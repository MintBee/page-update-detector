from keywords_in_changes_counter import KeywordsInChangesChecker


class PageUpdateDetector:
    def __init__(self, current_page: str, last_page: str, keywords: list):
        self.current_page = current_page
        self.last_page = last_page
        self.keywords = keywords

    def detect(self):
        assert self.current_page is not None and self.last_page is not None
        if self.current_page == self.last_page:
            return False, []
        else:
            keywords_in_changes_checker = KeywordsInChangesChecker(self.last_page,
                                                                   self.current_page, self.keywords)
            return True, keywords_in_changes_checker.get_keywords_in_changed_part()
