import requests

app_id = "b7651a9c"
app_key = "0da5d44688b3109d58d48b71f2947a11"

endpoint = "entries"
language_code = "en-us"

print("🔎 ENGLSH DICTIONNARY 📚")

while True:
    try:
        word_id = input('ENTER WORD:')
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower() + " ?fields=definitions"
        meaning = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
        definition = meaning.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        print('📌', definition)
        Exit = input('Type <exit>  or type  <continue> :')
        if Exit == 'exit':
            break

    except KeyError:
        print('>>>   English required to input [input a single word] , Please try again! ')
