# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
# import requests
#
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class APIReq(metaclass=Singleton):
#     pass
#     query = ''
#     searchendpoint = 'https://trackapi.nutritionix.com/v2/search/instant?branded_region=2&query='
#     fooddata = None
#     searchres = None
#     def getDetails(self, request):
#         url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
#         mydata = {'query': request}
#         response = requests.post(url, json=mydata, headers={"x-app-id": "6d3a9ca1",
#                                                             "x-app-key": "a5facf6d43ddb75f5ae1f14c4091e45a",
#                                                             "Content-Type": "application/json"})
#         resdata = response.json()
#         self.fooddata = resdata['foods']
#
#
#     def getSearchResult(request):
#         url = 'https://trackapi.nutritionix.com/v2/search/instant?branded_region=2&branded=false&query=' + request
#         response = requests.get(url, headers={"x-app-id": "6d3a9ca1",
#                                                             "x-app-key": "a5facf6d43ddb75f5ae1f14c4091e45a",
#                                                             "Content-Type": "application/json"})
#         resdata = response.json()
#         searchres = resdata['common']
#         food_name = (searchres[0])['food_name']
#         finallist = []
#         for foodname in searchres:
#             finallist.append(foodname['food_name'])
#         print(finallist)
#         return finallist
#
#     def getFoodName(self):
#         food_name = (self.fooddata[0])['food_name']
#         return(food_name)
#
#     def getCalories(self):
#         calories = (self.fooddata[0])['nf_calories']
#         return(calories)
#
#     def getTotalFats(self):
#         totalfats = (self.fooddata[0])['nf_total_fat']
#         return(totalfats)
#
#     def getSaturates(self):
#         saturates = (self.fooddata[0])['nf_saturated_fat']
#         return(saturates)
#
#     def getSalt(self):
#         salt = (self.fooddata[0])['nf_sodium']
# # Need to multiply this by 2.5 to get the actual salt value
#         return(salt)
#
#     def getSugar(self):
#         sugar = (self.fooddata[0])['nf_sugars']
#         return(sugar)
