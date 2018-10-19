from django.test import TestCase
from .factories import ChatTextFactory


class TestCategoryModels(TestCase):
    def setUp(self):
        self.chattext = ChatTextFactory(
            room_id=90,
            content='test message',
            count=9
        )

    def test_default_category_attrs(self):
        self.assertEqual(self.chattext.room_id, 90)
        self.assertEqual(self.chattext.content, 'test message')
        self.assertEqual(self.chattext.count, 9)
