
import openai
import os
import traceback
#from retrying import retry
import pprint
import json
#http://proxy.example.com/proxy.pac

#curl https://ap#i.openai.com/v1/models -H "Authorization: Bearer sk-
#"C:\Users\Owner\AppData\Local\Programs\Python\Python37-32\python.exe"

#https://community.openai.com/t/how-can-i-disable-ssl-verification-when-using-openai-api-in-python/110837

#@retry(stop_max_attempt_number=5)
import logging
def make_create():
    try:
        print("call openai")
        import json

        # Opening JSON file
        #mykeys = json.load(open('C:\workarea\open-ai-api-keys.json'))
        #pprint.pprint(mykeys)
        client = OpenAI(api_key="test",organization="org")
        response = client.embeddings.create(input="test", 
                                             model="gpt-3.5-turbo-0613")
        print(response)
    except Exception as e:
        pass

def readfile(file):
    with open(file, 'r', encoding="utf8") as file:
        data = file.read()
        return data

import base64
import requests

def read_imagefile(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to encode the image
def encode_image():
    image_path = 'C:\WorkArea\\forkumar\sybase-to-oracle\Image.jpeg'
    mykeys = json.load(open('c:\workarea\mykey.json'))
    api_key   = mykeys["api_key"]
    # Path to your image

    # Getting the base64 string
    base64_image = read_imagefile(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "convert the above sql into oracle code "
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", 
    headers=headers, json=payload)
    print(response)
    print(response.json())

    payload = {
    "model":"gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "rewrite the extracted code into for oracle"
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", 
    headers=headers, json=payload)
    print(response)
    print(response.json())


def test3():
    try:
        print("debug calling test3")
        from openai import OpenAI
        mykeys = json.load(open('c:\workarea\mykey.json'))
       # client = OpenAI(api_key="sk-",organization="org-")
        client = OpenAI(api_key=mykeys["api_key"],organization=mykeys["organization"])
        print(client)
        openai.verify_ssl_certs = False

        messages=[
                    {'role':"user","content":" rest"}
                    ,{'role':"user","content":" compare job descrtion vs resume"}
                    ,{'role':"user","content":" here jobs description1 "+readfile("jobs-des1.txt")}
                    ,{'role':"user","content":" here resume"+readfile("resume1.txt")}                 
                # {"role" : "user", "content" : "what features removed from apachetomcat 9.05 compare to apachetomcat 8.5.31"
                    # ,{  'role':"user","content":" do word match matching skills in the scale of 10 in summary match by words"}
                    ,{'role':"user","content":" here is jobs 2nd jobs description1 "+readfile("jobs-des2.txt")}
                    ,{'role':"user","content":"do word match skills in the scale of 10 in summary match by words give table format"}
                ]
        messages=[
                    {'role':"user","content":" rest"}
        ]
        messages=[
                    {'role':"user","content":" convert sybase stored proc into oracle stored proc give code only"}
        ]
        print("before calling client.chat.completions.create")
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                #model="text-embedding-3-small",
                messages=messages
                )
            print(completion)
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
            print(dir(e))
            print(e.code)
            print(e.body)
            print(e.request) 
            print(e.args)
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
            print(dir(e))
            print(e.code)
            print(e.body)
            print(e.request)
            print(e.args)
    except Exception as e:
        logging.exception(e)




def old_test4():
    openai.api_key = "sk-"

    response = openai.Completion.create(
        engine="gpt-4",
        #model = 'gpt-4',
        prompt = 'TEST',
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

try:
   #make_create()
   #test2()
   #test3()
   encode_image()
  #Make your OpenAI API request here
   # response = client.chat.completions.create(
    #model="gpt-3.5-turbo",
   # messages=[
   #     {"role": "system", "content": "You are a helpful assistant."},
   #     {"role": "user", "content": "Who won the world series in 2020?"},
   #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
   #     {"role": "user", "content": "Where was it played?"}
   # ],

    #chat_test_response  = client.chat.completions.create(
    #        model="gpt-3.5-turbo-0613",
    #        messages=[ { "role": "user","content":"tell me story" }],
      #  temperature=0,)    
    #print(chat_test_response)                            
except Exception as e:
    logging.exception(e)
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
