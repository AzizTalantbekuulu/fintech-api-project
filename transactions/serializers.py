from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        transaction = Transaction.objects.create(user=user, **validated_data)
        return transaction