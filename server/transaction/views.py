from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Assuming serializers for request data are defined here
# from .serializers import PaySubscriptionSerializer, ListSubscriptionsSerializer

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description="Amount to pay"),
            'currency': openapi.Schema(type=openapi.TYPE_STRING, description="Currency code")
        },
        required=['amount', 'currency']
    ),
    responses={
        200: openapi.Response(
            description="Successful payment",
            examples={
                "application/json": {
                    "msg": "Payment successful"
                }
            }
        ),
        400: openapi.Response(description="Payment failed")
    }
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    # Extract data from request body
    amount = request.data.get('amount')
    currency = request.data.get('currency')

    # Implement your payment logic here

    return response.Response({"msg": "Payment successful"}, 200)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="User ID to list subscriptions")
        },
        required=['user_id']
    ),
    responses={
        200: openapi.Response(
            description="Successful retrieval of subscriptions",
            examples={
                "application/json": {
                    "msg": "Subscriptions retrieved successfully"
                }
            }
        ),
        404: openapi.Response(description="User not found")
    }
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    user_id = request.data.get('user_id')

    # Implement your logic to list subscriptions here

    return response.Response({"msg": "Subscriptions retrieved successfully"}, 200)
