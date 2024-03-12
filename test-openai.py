import openai
import os
import traceback
from retrying import retry

#http://proxy.example.com/proxy.pac


#curl https://api.openai.com/v1/models -H "Authorization: Bearer sk-" -H "OpenAI-Organization: org-"

#https://community.openai.com/t/how-can-i-disable-ssl-verification-when-using-openai-api-in-python/110837

@retry(stop_max_attempt_number=5)
def make_create():
    try:
         print("call openai")
         client = OpenAI(api_key='sk-',
                 organization='org-')
         response = client.embeddings.create(input="test", model="gpt-3.5-turbo-0613")
         print(response)
    except Exception as e:
        pass

    
def test3():
    from openai import OpenAI
    client = OpenAI(api_key='sk-',
                 organization='org-')
    openai.verify_ssl_certs = False

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
           {"role" : "user", "content" :"what is name expensive whiskey and price give short answer"}
    ]
    )
    print(completion.choices[0].message)




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
   test3()
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
  #Handle rate limit error (we recommend using exponential backoff)
  print(f"OpenAI API request exceeded rate limit: {e}")
  pass

```
openssl  s_client -showcerts -verify 5 -connect api.openai.com:443
S C:\Users\KumarSundaram\workflow> pip list
Package             Version
------------------- ---------
aiohttp             3.9.3
aiosignal           1.3.1
annotated-types     0.6.0
anyio               4.3.0
asgiref             3.5.2
async-generator     1.10
async-timeout       4.0.3
attrs               21.4.0
autopep8            1.6.0
certifi             2022.9.24
cffi                1.15.1
charset-normalizer  2.1.1
colorama            0.4.6
cryptography        37.0.4
distlib             0.3.6
distro              1.9.0
django-crispy-forms 1.14.0
docutils            0.19
ffmpeg-python       0.2.0
filelock            3.8.2
frozenlist          1.4.1
future              0.18.2
gunicorn            20.1.0
h11                 0.13.0
httpcore            1.0.4
httpx               0.27.0
idna                3.4
jmespath            1.0.1
multidict           6.0.5
mypy-extensions     0.4.3
numpy               1.23.1
openai              1.13.3
opencv-python       4.6.0.66
outcome             1.2.0
pathspec            0.10.0
pbr                 5.11.0
phonenumberslite    8.12.55
Pillow              9.2.0
pip                 22.1.1
platformdirs        2.5.2
psycopg2-binary     2.9.3
pycodestyle         2.8.0
pycparser           2.21
pydantic            2.6.3
pydantic_core       2.16.3
pyOpenSSL           22.0.0
PySocks             1.7.1
python-dateutil     2.8.2
pytube              12.1.3
pytz                2022.2.1
requests            2.28.1
retrying            1.3.4
selenium            4.3.0
setuptools          58.1.0
six                 1.16.0
sniffio             1.2.0
sorl-thumbnail      12.9.0
sortedcontainers    2.4.0
sqlparse            0.4.2
stevedore           4.1.1
toml                0.10.2
tomli               2.0.1
tqdm                4.66.2
trio                0.21.0
trio-websocket      0.9.2
typing_extensions   4.10.0
tzdata              2022.7
urllib3             1.26.11
virtualenv          20.17.1
virtualenv-clone    0.5.7
virtualenvwrapper   4.8.4
wsproto             1.1.0
yarl                1.9.4
WARNING: There was an error checking the latest version of pip.
```
