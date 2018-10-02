from django.contrib.auth.models import User
from rest_framework import serializers
from basic.models import Member


# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('account', 'username', 'email', 'is_staff')
