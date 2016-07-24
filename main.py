#THIS IS A SIMPLE TEST TO WORK WITH THE IMGFLIP API

import requests
import json

#test0 = input("Top > ")
#test1 = input("Bottom > ")

template = "61579"
text0 = "One Does Not Simply"
text1 = "Copy Michelle Obama's Speech"

        

imgflip = "https://api.imgflip.com/caption_image"

values = {"template_id":template,
          "username":"memescool",
          "password":"awesomenessstartshere",
          "text0":text0,
          "text1":text1}

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

req = requests.get(url=imgflip, params=values, headers=headers)
data = json.loads(req.text)
print(data['data']['url'])
