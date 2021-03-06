import requests
import json

firebaseKEY = "AAAA6Uqx-AY:APA91bHVqcEznfJUhgtBAR5WpojLz0EvFmIrgv0CZ7IMODfIjH_4L1jZwDmsnmOMmdm10IZuBmGKYo8UKv4LB8i9DCv18DgN6P-ErLIHBYQndLdIJvVtczbj4JiR8cP6pYZsc2Bk8Mbr"

def send_fcm(seller, item, number):
	url = 'https://fcm.googleapis.com/fcm/send'
	body = {
		"data": {
			"seller": seller,
			"item": item,
			"number": number
		},
		"notification": {
			"title": "비둘기장터",
			"body": seller + "님이 " + item + "을(를) 구매하고 싶어합니다.",
			"click_action": ".BuyerInfoActivity"
		},
		"to": "/topics/WantBuy"
	}

	headers = {"Content-Type": "application/json",
			   "Authorization": "key="+firebaseKEY}
	requests.post(url, data=json.dumps(body), headers=headers)