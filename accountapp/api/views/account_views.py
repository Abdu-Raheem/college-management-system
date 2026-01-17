from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from accountapp.models import Profile
from accountapp.api.serializer.account_serializer import ProfileSerializer


class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileManagementView(APIView):
    def get(self, request, id):
        if not Profile.objects.filter(user=id).exists():
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.get(user=id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        if not Profile.objects.filter(user=id).exists():
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.get(user=id)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not Profile.objects.filter(user=id).exists():
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.get(user=id)
        profile.delete()
        return Response({'message': 'Profile deleted successfully'}, status=status.HTTP_200_OK)


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer