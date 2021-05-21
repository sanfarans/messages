from rest_framework import serializers, views, parsers, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Message
from .serializers import MessageSerializer


class CreateMessage(views.APIView):

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewMessage(views.APIView):

    def get_obj_or_404(self, message_id):
        try:
            obj = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            raise NotFound(detail="there's no message with such id", code=404)
        return obj

    def get(self, request, message_id):
        obj = self.get_obj_or_404(message_id)
        obj.views += 1
        obj.save()
        return Response(MessageSerializer(obj).data)

    def put(self, request, message_id):
        obj = self.get_obj_or_404(message_id)
        serializer = MessageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.validated_data["views"] = 0
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id):
        obj = self.get_obj_or_404(message_id)
        obj.delete()
        return Response(status=status.HTTP_200_OK)
