from django.test import TestCase
from .factories import ChatTextFactory


class TestCategoryModels(TestCase):
    def setUp(self):
        self.chattext = ChatTextFactory(
            room_id=90,
            json_chat="{'chat': 1}"
        )

    def test_default_category_attrs(self):
        self.assertEqual(self.chattext.room_id, 90)
        self.assertEqual(self.chattext.json_chat, "{'chat': 1}")
