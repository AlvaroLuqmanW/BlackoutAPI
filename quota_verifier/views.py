from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from BLACKOUT_API.settings import BOT_TOKEN

# Create your views here.
def verifyQuota(request, event, userID, channelID, messageID):
    divisionalEventChannelIDs = ['780627292434726922', '923455236809588778', '736609429167931463']
    contractedEventChannelIDs = ['780623012390633492', '923455236809588778', '736609429167931463', '780623059009798144']

    # if event == 'divisional' and channelID not in divisionalEventChannelIDs:
    #     return JsonResponse({'message': 'Invalid\nInvalid channel ID'})
    # if event == 'contracted' and channelID not in contractedEventChannelIDs:
    #     return JsonResponse({'message': 'Invalid\nInvalid channel ID'})
    
    bot_token = BOT_TOKEN
    api_endpoint = f"https://discord.com/api/v9/channels/{channelID}/messages/{messageID}"
    headers = {"Authorization": f"Bot {bot_token}"}
    response = requests.get(api_endpoint, headers=headers)
    message_content = response.json().get('content')

    print(message_content)

    if message_content is None:
        return JsonResponse({'message': 'Invalid\nInvalid Server ID'})
    
    if userID in message_content:
        return JsonResponse({'message': 'Valid'})
    else:
        return JsonResponse({'message': 'Invalid\nUser not mentioned in event log'})

    # return HttpResponse(response.json()['content']) 
    # return response.json()['content']
    # return JsonResponse({'userID': userID, 'channelID': channelID, 'messageID': messageID}, status=200)