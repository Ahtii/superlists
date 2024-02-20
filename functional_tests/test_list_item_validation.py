from selenium.webdriver.common.keys import Keys

from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element('id', 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element('class name', 'has-error').text,
            "You can't have an empty list item"
        ))
        self.browser.find_element('id', 'id_new_item').send_keys('Buy milk')
        self.browser.find_element('id', 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tables('1: Buy milk')

        self.browser.find_element('id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element('class name', 'has-error').text,
            "You can't have an empty list item"
        ))

        self.browser.find_element('id', 'id_new_item').send_keys('Make tea')
        self.browser.find_element('id', 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tables('1: Buy milk')
        self.wait_for_row_in_list_tables('1: Make tea')
