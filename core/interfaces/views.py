# core/interfaces/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.application.user_service import UserService
from core.infrastructure.user_repository import UserRepository
from core.interfaces.serializers import UserSerializer

class UserView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService(UserRepository())

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.user_service.create_user(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        user = self.user_service.get_user(user_id)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
