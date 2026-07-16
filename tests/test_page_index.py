import unittest
from unittest.mock import Mock, patch

from pageindex.page_index import process_toc_no_page_numbers


class ProcessTocNoPageNumbersTest(unittest.TestCase):
    def test_rejects_same_length_reordered_llm_toc(self):
        toc = [
            {"structure": "1", "title": "First"},
            {"structure": "2", "title": "Second"},
        ]
        reordered = [
            {"structure": "2", "title": "Second", "physical_index": "<physical_index_2>"},
            {"structure": "1", "title": "First", "physical_index": "<physical_index_1>"},
        ]

        with patch("pageindex.page_index.toc_transformer", return_value=toc), \
             patch("pageindex.page_index.count_tokens", return_value=1), \
             patch("pageindex.page_index.page_list_to_group_text", return_value=["<physical_index_1> <physical_index_2>"]), \
             patch("pageindex.page_index.add_page_number_to_toc", return_value=reordered):
            with self.assertRaises(ValueError):
                process_toc_no_page_numbers(
                    "toc",
                    [],
                    [["page one"], ["page two"]],
                    logger=Mock(),
                )


if __name__ == "__main__":
    unittest.main()
