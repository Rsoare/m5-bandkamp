from .models import Album
from users.models import User
from .serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView


class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        userId = self.request.user.id
        user = User.objects.filter(id=userId).first()
        serializer.save(user=user)
