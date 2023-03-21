from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_info_social(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    social_media = SocialMedia.objects.all()
    social_media_ser = SocialMediaSerializer(social_media, many=True)
    data = {
        "info": info_ser.data,
        "social_media": social_media_ser.data
    }
    return Response(data)


@api_view(["POST"])
def create_order(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    if name and phone is not None:
        if name.isalpha():
            if len(phone) == 13:
                if phone[:4] == "+998":
                    a = phone[4:6]
                    list = ["99", "98", "97", "95", "94", "93", "91", "90", "88", "33"]
                    if a in list:
                        if phone[6:].isdigit():
                            Order.objects.create(name=name, phone=phone)
                            order = Order.objects.last()
                            data = OrderSerializer(order).data
                        else:
                            data = {
                                "error": "Number must include only numbers"
                            }
                    else:
                        data = {
                            "error": "Number company not found"
                        }
                else:
                    data = {
                        "error": "Ex. +998901234567"
                    }
            else:
                data = {
                    "error": "The length of number must be 13"
                }
        else:
            data = {
                "error": "Name must include only letters"
            }
    else:
        data = {
            "error": "Name and number can't be None"
        }
    return Response(data)


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all().order_by('-id')[:2]
    ser = ProductSerializer(product,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about_product(request):
    product = Product.objects.all().order_by('-id')[:2]
    ser = AboutProductSerializer(product,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_unity_product(request):
    product = Product.objects.last()
    ser = UnityProductSerializer(product)
    return Response(ser.data)


@api_view(['GET'])
def get_about_company(request):
    company = AboutCompany.objects.last()
    ser = AboutCompanySerializer(company)
    return Response(ser.data)


@api_view(["GET"])
def get_who_use(request):
    who_use = WhoUse.objects.all()
    who_use_ser = WhoUseSerializer(who_use, many=True)
    data = {
        "data": who_use_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_how_to_use(request):
    how_to_use = HowToUse.objects.last()
    how_to_use_ser = HowToUseSerializer(how_to_use)
    data = {
        "data": how_to_use_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_fact(request):
    fact = Fact.objects.all()
    fact_ser = FactSerializer(fact, many=True)
    data = {
        "data": fact_ser.data,
    }
    return Response(data)