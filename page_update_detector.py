from keywords_in_changes_counter import KeywordsInChangesChecker


class PageUpdateDetector:
    def __init__(self, current_page: str, last_page: str, keywords: list):
        self.current_page = current_page
        self.last_page = last_page
        self.keywords = keywords

    # Compare current_page html and last_page html. If there is a difference, return True.
    # Otherwise, return False.
    # Also, return the list of keywords that is included in updated part of current keyword.
    def detect(self):
        assert self.current_page is not None and self.last_page is not None
        if self.current_page == self.last_page:
            return False, []
        else:
            keywords_in_changes_checker = KeywordsInChangesChecker(self.last_page,
                                                                   self.current_page, self.keywords)
            return True, keywords_in_changes_checker.get_keywords_in_changed_part()
