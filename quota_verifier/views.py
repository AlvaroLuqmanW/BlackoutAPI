from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from BLACKOUT_API.settings import BOT_TOKEN

# Create your views here.
def verifyQuota(request, userID, channelID, messageID):
    channel_id = channelID
    message_id = messageID
    user_id = userID
    bot_token = BOT_TOKEN
    api_endpoint = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    headers = {"Authorization": f"Bot {bot_token}"}
    response = requests.get(api_endpoint, headers=headers)

    return HttpResponse(response.json()['content']) 
    # return response.json()['content']
    # return JsonResponse({'userID': userID, 'channelID': channelID, 'messageID': messageID}, status=200)