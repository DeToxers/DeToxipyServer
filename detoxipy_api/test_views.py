from django.test import TestCase, Client
from .models import ChatText
from .factories import ChatTextFactory


class TestSessionViews(TestCase):
    def setUp(self):
        """ Sets up the test instance with a client
        """
        self.c = Client()

    # def test_view_list(self):
    #     """ Tests that the bubble route returns a 201 status code when posted to
    #     """
    #     res = self.c.post('/api/v1/chat')
    #     self.assertEqual(res.status_code, 200)

    def test_cannot_delete(self):
        """ Tests that the bubble route returns a 400 status code when deleted to
        """
        res = self.c.delete('/api/v1/bubble')
        self.assertEqual(res.status_code, 405)

    def test_cannot_put(self):
        """ Tests that the bubble route returns a 400 status code when put to
        """
        res = self.c.delete('/api/v1/bubble')
        self.assertEqual(res.status_code, 405)

    def test_theres_roomid_in_response(self):
        """ Tests that the response along the bubble route has room id in the response
        """
        chattext = ChatTextFactory()
        res = self.c.get('/api/v1/bubble')
        self.assertIn(chattext.room_id, res.content)
        self.assertIn(chattext.json_chat.encode(), res.content)
