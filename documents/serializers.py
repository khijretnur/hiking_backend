from rest_framework import serializers
from documents.models import Document, PrivacyStatement


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'file_type')


class PrivacyStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyStatement
        fields = "__all__"
