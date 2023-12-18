from django.shortcuts import render
from users.forms import RegisterForm
from users import validators, models_api
from rest_framework import permissions, response, status, decorators
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def sign_up(request):
    form  = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(
        request ,
        "user_registration.html",
        {"form" : form}
        )


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def login(request):
    print("reques", request.data)
    # print("username", request.data.get("username"))
    validators.validate_content_type(request=request)
    username = request.data.get("username", "")
    password = request.data.get("password", "")
    if not username or not password:
        return response.Response({
            "result": False,
            "msg": "username or password missing or empty"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user_model = models_api.UserManagementModel()
    user = user_model.is_valid_user(username=username, password=password)

    token = Token.objects.get_or_create(user=user)[0]

    return response.Response({
        "result": True,
        "msg": "Logged in sucessfully",
        "data": {
            "token": token.key,
            },
        }, status=status.HTTP_200_OK,
    )


@decorators.api_view(['POST'])
@decorators.permission_classes([IsAuthenticated])
def sign_out(request):
    if request.method == 'POST':
        try:
            print("requesr", request.user)
            request.user.auth_token.delete()
            return Response(
                {
                    "status" : True,
                    "msg": "Successfully logged out"
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def password_reset(request):
    old_password = request.data.get("old_password", "")
    new_password = request.data.get("new_password", "")
    cnfirm_new_password = request.data.get("cnfirm_new_password", "")
    user = request.user
    if not old_password:
        return response.Response(
            {"result": False, "msg": "Old Password is missing"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not new_password:
        return response.Response(
            {"result": False, "msg": "new_password Password is missing"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not cnfirm_new_password:
        return response.Response(
            {"result": False, "msg": "cnfirm_new_password Password is missing"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    elif not user.check_password(old_password):
        return response.Response(
            {"result": False, "msg": "Incorrect Old password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    elif new_password != cnfirm_new_password:
        return response.Response(
            {
                "result": False,
                "msg": "new password and reentered password does not match",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    user.set_password(new_password)
    user.save()
    return response.Response(
        {
            "result": True,
            "msg": "Your password has been changed successfully.",
        },
        status=status.HTTP_200_OK,
    )