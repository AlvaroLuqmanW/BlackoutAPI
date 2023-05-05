from django.urls import path
from quota_verifier.views import verifyQuota

app_name = 'quota_verifier'

urlpatterns = [
    path('<userID>/<channelID>/<messageID>', verifyQuota, name='verifyQuota'),
]

