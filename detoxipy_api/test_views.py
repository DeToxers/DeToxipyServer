from django.test import TestCase, Client
from .models import ChatText
from .factories import ChatTextFactory


class TestSessionViews(TestCase):
    def setUp(self):
        self.c = Client()

    def test_view_list(self):
        # session = SessionFactory
        res = self.c.post('/api/v1/bubble')
        self.assertEqual(res.status_code, 201)

        # self.assertIn(session.room_id.encode(), res.content)

#     def test_lists_only_owned_categories(self):

#         own_category = BudgetFactory(user=self.user)
#         other_category = BudgetFactory()

#         res = self.c.get('/budgets/budget')

#         self.assertIn(own_category.name.encode(), res.content)
#         self.assertNotIn(other_category.name.encode(), res.content)

#     def test_transactions_listed_in_view(self):

#         budget = BudgetFactory(user=self.user)
#         transaction = TransactionFactory(budget=budget)
#         res = self.c.get('/budgets/budget')

#         self.assertIn(transaction.title.encode(), res.content)


# class TestTransactionViews(TestCase):
#     pass


# class TestBudgetCreateViews(TestCase):
#     """ Tests transaction create view returns what's expected
#     """

#     def test_new_budget_view(self):

#         res = self.c.get('/budgets/budget/new')

#         self.assertEqual(res.status_code, 200)
#         self.assertIn(b'input type="submit"', res.content)
#         self.assertIn(b'name="name"', res.content)
#         self.assertIn(b'name="description"', res.content)

#     def test_create_view_adds_new_category(self):
#         form_data = {
#             'name': 'Name of it',
#             'description': 'a description'
#         }
#         res = self.c.post('/budgets/budget/add', form_data, follow=True)

#         self.assertIn(b'Name of it', res.content)
