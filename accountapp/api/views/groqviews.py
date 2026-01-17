from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from ...groq_ai import ask_ai


class AIChatView(APIView):
    @swagger_auto_schema(
        operation_summary="AI Chat",
        operation_description="Send a prompt and receive an AI-generated response",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["prompt"],
            properties={
                "prompt": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Explain GST in simple terms"
                )
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "response": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="GST is a single indirect tax applied on goods and services..."
                    )
                },
            ),
            400: "Bad Request",
        },
    )
    def post(self, request):
        prompt = request.data.get("prompt")

        if not prompt:
            return Response(
                {"error": "Prompt is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        answer = ask_ai(prompt)
        return Response({"response": answer}, status=status.HTTP_200_OK)
