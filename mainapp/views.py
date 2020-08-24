from django.shortcuts import render, redirect
import requests
import json


def main(request):
    if request.user.is_authenticated:
        return redirect('/authenticated/')
    return render(request, 'main.html')


def authenticated(request):
    
    token = 'a041ea88a041ea88a041ea8806a0327df1aa041a041ea88ff03ccef14249df9041d7884'
    v = '5.122'
    response_id = requests.get(f'https://api.vk.com/method/users.get?user_ids={request.user}&access_token={token}&v={v}')
    data = json.loads(response_id.content)
    name = ' '.join([data['response'][0]['first_name'], data['response'][0]['last_name']])
    user_id = data['response'][0]['id']
    response_friends = requests.get(f'https://api.vk.com/method/friends.get?user_id={user_id}&count=5&access_token={token}&v={v}&name_case=ins&fields=first_name%last_name&order=random')
    friends = json.loads(response_friends.content)['response']['items']
    return render(request, 'authenticated.html', {'friends': friends, 'name': name})
