from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def verifyQuota(request, userID, channelID, messageID):
    channel_id = channelID
    message_id = messageID
    user_id = userID
    bot_token = "MTA4NzY1MTA1NTIzNzYwMzMzMQ.GYgSiH.4I5-4F4307thsobmHa4Vd_VFMY7yBEHuYpiNl0"
    api_endpoint = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    headers = {"Authorization": f"Bot {bot_token}"}
    response = requests.get(api_endpoint, headers=headers)

    # return HttpResponse(response.json()['content']) - Httpresponse is not JSON serializable
    return response.json()['content']
    # return JsonResponse({'userID': userID, 'channelID': channelID, 'messageID': messageID}, status=200)