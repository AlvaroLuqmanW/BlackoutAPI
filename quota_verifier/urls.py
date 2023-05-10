from django.urls import path
from quota_verifier.views import verifyQuota

app_name = 'quota_verifier'

urlpatterns = [
    path('<String:event>/<String:userID>/<String:channelID>/<String:messageID>', verifyQuota, name='verifyQuota'),
]

