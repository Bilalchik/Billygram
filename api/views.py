from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.utils.decorators import method_decorator


from django.contrib.auth.models import User

from app.models import Like, Post, Following


@method_decorator(csrf_exempt, name='post')
class LikeViewApi(APIView):
    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        post_id = data.get('post_id')

        if user_id is None or post_id is None:
            return Response({"error_massage": 'user_id netu libo post_id netu'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Like(user_id=user_id, post_id=post_id).save()
        except (ValidationError, IntegrityError) as error:
            return Response({'error_massage': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='post')
class FollowingViewApi(APIView):
    def post(self, request):
        data = request.data

        user_id = data.get("user_id")
        following_id= data.get("following_id")

        if user_id is None or following_id is None:
            return Response({"error_massage": 'user_id netu libo following_id netu'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Following(user_id=user_id, following_id=following_id).save()
        except (ValidationError, IntegrityError) as error:
            return Response({'error_massage': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)







