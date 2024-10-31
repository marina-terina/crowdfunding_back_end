from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer
from projects.models import Project, Pledge
from projects.models import Project
from projects.serializers import ProjectSerializer, PledgeSerializer 
from projects.permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly, IsSuperuser

class CustomUserList(APIView):
    #permission_classes = [IsSuperuser]  # Apply the superhero permission

    def get_permissions(self):
        if self.request.method == 'POST':
            return []  # Allow any user for POST requests
        elif self.request.method == 'GET':
            return [IsSuperuser()]  # Require IsSuperuser permission for GET requests
        return super().get_permissions()  # For other methods, use the default behavior
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]  
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        if user != request.user:
            return Response({'detail': 'You do not have permission to view this user.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })
    
class UserProjects(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        projects = Project.objects.filter(owner=pk)  
        if not projects.exists():
            return Response({'detail': 'No projects found for this user.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPledges(APIView):
    def get(self, request, pk):
        pledges = Pledge.objects.filter(supporter=pk)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)