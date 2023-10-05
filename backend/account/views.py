from rest_framework import response, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegistrationSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username.title()
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# User registration
@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            user = serializer.create(request.data)
            if user:
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except: return response.Response({"username":["Username exist"]}, status=status.HTTP_400_BAD_REQUEST)
