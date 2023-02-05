from django.shortcuts import render
from .query import query_with_fetchall


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .encoding_filter import enc_filter

from .get_company_for_id import get_company_for_id
from .get_roles_for_company import get_roles_for_company
from .get_roles_for_user_query import get_roles_for_user_query
from .get_users_for_roles import get_users_for_roles
from .get_login_verification import get_login_verification

from .post_create_new_company import post_create_company
from .post_create_role import post_create_role
from .post_create_new_user import post_create_user


def ichack_view(request):
    """Serve the html file for the ichack"""
    return render(request, "index.html")



@api_view(["GET"])
def request_get_company_for_id(request, comp_id=None):
    print(request)
    response = get_company_for_id(comp_id)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_roles_for_company(request, comp_id=None):
    response = get_roles_for_company(comp_id)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_roles_for_user_query(request, text=None):
    response = get_roles_for_user_query(text)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_users_for_roles(request, role_id=None):
    response = get_users_for_roles(role_id)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_login_verification(request, email=None, password=None):
    print(email, password)
    return Response(get_login_verification(email, password), status=status.HTTP_200_OK)



@api_view(["POST"])
def request_post_create_new_user(request):
    data = request.POST
    post_create_user(data)
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
def request_post_create_new_company(request):
    data = request.POST
    print(data)
    post_create_company(data)
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
def request_post_create_role(request):
    data = request.POST
    post_create_role(data)
    return Response({}, status=status.HTTP_200_OK)