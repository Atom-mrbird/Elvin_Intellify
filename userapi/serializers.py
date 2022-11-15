from rest_framework.serializers import ModelSerializer
from .models import Warning
from rest_framework import serializers

class WarningSerializer(ModelSerializer):

    class Meta:
        model = Warning

        fields = ['name', 'max_value', 'datapoint_id'
                  ]


class MailSerializer(serializers.Serializer):
   email_id = serializers.CharField()
   email_content = serializers.CharField()