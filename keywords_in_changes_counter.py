import re
from collections import defaultdict


def count_substrings_occurrence(string_to_scan, substrings: list):
    patterns = [re.compile(re.escape(substring), re.IGNORECASE) for substring in substrings]

    counts = defaultdict(int)
    for pattern in patterns:
        counts[pattern.pattern] = len(pattern.findall(string_to_scan))

    return counts


class KeywordsInChangesCounter:
    def __init__(self, last_page, changed_page, keywords: list):
        self.last_page = last_page.lower()
        self.changed_page = changed_page.lower()
        self.keywords = list(map(lambda x: x.lower(), keywords))

    def get_keywords_in_changed_part(self):
        last_page_keyword_occurrences = count_substrings_occurrence(self.last_page, self.keywords)
        changed_page_keyword_occurrences = count_substrings_occurrence(self.changed_page,
                                                                       self.keywords)

        keywords_in_changes = []
        for keyword in self.keywords:
            if changed_page_keyword_occurrences[keyword] > last_page_keyword_occurrences[keyword]:
                keywords_in_changes.append(keyword)

        return keywords_in_changes
