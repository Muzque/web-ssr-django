from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from basic.models import Member
from basic.serializer import MemberSerializer


class Member(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        member = Member.objects.all()
        return Response(member)


def index(request):
    return render(request, "basic/index.html", locals())
