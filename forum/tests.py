from django.test import TestCase, LiveServerTestCase
from forum.models import Forum  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class ForumTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_create_new_forum_via_admin_site(self):
        self.browser.get(self.live_server_url + '/admin')
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        forum_links = self.browser.find_elements_by_link_text('Forum')
        self.assertEquals(len(forum_links), 2)
        
        self.fail('finish this test')