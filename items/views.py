from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ItemSerializers
from .models import Items
#  logger.info(f"This is the log message {e}")


class ItemsApiView(APIView):
    serializer_class = ItemSerializers

    def post(self,request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
              serializer.save()
              return Response(data ={"status":1,"data":serializer.data}, status=status.HTTP_200_OK)
            return Response(data ={"status":0,"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"status":0, "message":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        try:
            objs = Items.objects.all()
            serializer = self.serializer_class(objs, many=True)
            return Response(data ={"status":1,"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"status":0, "message":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        


