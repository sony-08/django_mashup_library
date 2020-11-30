from catalog.models import BookInstance
from rest_framework import serializers

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ('id', 'book', 'imprint', 'due_back')