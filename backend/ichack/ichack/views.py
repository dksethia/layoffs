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

from .post_create_new_company import post_create_company
from .post_create_role import post_create_role
from .post_create_new_user import post_create_user


def ichack_view(request):
    """Serve the html file for the ichack"""
    return render(request, "ichack.html")



@api_view(["GET"])
def request_get_company_for_id(request):
    response = get_company_for_id(request)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_roles_for_company(request):
    response = get_roles_for_company(request)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_roles_for_user_query(request):
    response = get_roles_for_user_query(request)
    return Response(response, status=status.HTTP_200_OK)

@api_view(["GET"])
def request_get_users_for_roles(request):
    response = get_users_for_roles(request)
    return Response(response, status=status.HTTP_200_OK)



@api_view(["POST"])
def request_post_create_new_user(request):
    post_create_user(request)
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
def request_post_create_new_company(request):
    post_create_company(request)
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
def request_post_create_role(request):
    post_create_role(request)
    return Response({}, status=status.HTTP_200_OK)