from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample transaction data for testing
        self.transaction_data = {'amount': 100.0}
        self.invalid_transaction_data = {'amount': 'invalid'}

    def test_create_transaction(self):
        # Test creating a new transaction
        response = self.client.post(reverse('transaction-list-create'), self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().amount, 100.0)

    def test_invalid_transaction_data(self):
        # Test creating a transaction with invalid data
        response = self.client.post(reverse('transaction-list-create'), self.invalid_transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
