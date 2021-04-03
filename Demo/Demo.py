import http.client, json, urllib.request, urllib.parse, urllib.error, urllib
import requests
import difflib
import sys
import azure.cognitiveservices.speech as speechsdk


print("""Let us spell check your input.""")

key = "19e46f9180454c3ead087b1aa1fbb499"

demo_text = input("Please enter something: ")

endpoint = "https://api.bing.microsoft.com/v7.0/spellcheck"
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
    }
data = {'text': demo_text}
params = urllib.parse.urlencode(
    {
    'mkt':'en-US',
    'setLang':'EN',
    'text':demo_text,
        }
    )
 
response = requests.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()
new_demo_text = (json.dumps(json_response, indent=4))

jsonData = new_demo_text
data = json.loads(jsonData)
print("""Here are the suggestions:""")
print('\n')
for token in data['flaggedTokens']:
    print('Change ' + '[' + token['token'] + ']' + ' for:')
    for suggestion in token['suggestions']:
      print(' ' + '{' + suggestion['suggestion'] + '}')
      print(' Accuaracy score is  '  + str(suggestion['score']))
    print('\n')
    print('**************************************************************************')
    print('\n')

       
input("Press enter to continue: ")

print (""" Now let us see your conversational skill""")
print('-----------------------------')
print('\n')
text1 = """That is a hungry elephant."""
print(text1)
text1_lines = text1.splitlines()

speech_config = speechsdk.SpeechConfig(subscription="38dcfaad146345b188c97dd6955404c8", region="southeastasia")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)   
print("Please speak into your microphone.")
result = speech_recognizer.recognize_once_async().get()
print('\n')
print("You spoke:   " + result.text)

text2_lines = result.text.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n')
print("We have identified the differnces as highlighed: ")
print('\n'.join(diff))