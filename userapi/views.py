from django.shortcuts import render
from response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Warning
from .serializers import WarningSerializer, MailSerializer
from rest_framework import permissions, viewsets
import tasks

class WarningList(ListCreateAPIView):

    serializer_class = WarningSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Warning.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = WarningSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "max_value"

    def get_queryset(self):
        return Warning.objects.filter(owner=self.request.user)
class MailViewset(viewsets.ViewSet):
    '''
    Email endpoint which receives email address and email HTML content
    '''

    def create(self, request):
        try:
            ip_data = request.data
            subject, sender = 'drf_celery_email_api_test', 'ataberkyakar@outlook.com'
            serialized = MailSerializer(request.data).data
            receiver = serialized['email_id']
            if '@' not in receiver:
                raise Exception
            # html_content = '<h1>hey!! It worked</h1>'
            html_content = serialized['email_content']
            result = tasks.send_mail(subject, sender, receiver, html_content)
            if result == 'success':
                return Response('Mail sent successfully')
            else:
                raise Exception
        except:
            return Response('Error in sending mail')