from rest_framework.decorators import api_view
from rest_framework.response import Response


from accountapp.models import Profile
from accountapp.api.serializer.account_serializer import ProfileSerializer


@api_view(['GET'])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)