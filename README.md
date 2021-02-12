2021-02-12 21:25:06 Friday

------------


------------
># English Dictionnary

------------

[![](https://i.ibb.co/NTKNtkS/English-Dictionary.png)](https://i.ibb.co/NTKNtkS/English-Dictionary.png)

<br>

------------

### Techologies Used:
### 1. [![python](https://th.bing.com/th/id/R591873ea1d6c882779c930108451b4c6?rik=3cujZ%2fXGEpuZxw&riu=http%3a%2f%2fblog.magiksys.net%2fsites%2fdefault%2ffiles%2fpictures%2fpython-logo-64.png&ehk=yYto2GxfibPTkZzVSvFbRnZEnCUbxoUxvXpl%2fh6gG48%3d&risl=&pid=ImgRaw "python")](https://th.bing.com/th/id/R591873ea1d6c882779c930108451b4c6?rik=3cujZ%2fXGEpuZxw&riu=http%3a%2f%2fblog.magiksys.net%2fsites%2fdefault%2ffiles%2fpictures%2fpython-logo-64.png&ehk=yYto2GxfibPTkZzVSvFbRnZEnCUbxoUxvXpl%2fh6gG48%3d&risl=&pid=ImgRaw "python")
### 2. Application Programming Interface(API) [Learn More!](https://tacc.github.io/CSC2017Institute/docs/day2/APIs_intro.html "Learn More!")

[![](https://blog.testlodge.com/wp-content/uploads/2018/05/api-testing.png)](https://blog.testlodge.com/wp-content/uploads/2018/05/api-testing.png)


#### We use API of [Oxford Dictionaries API](https://developer.oxforddictionaries.com/ "Oxford Dictionaries API")

------------
### The Pyhton code:
```python
import  requests
import json
# TODO: replace with your own app_id and app_key
app_id = '<my app_id>'
app_key = '<my app_key>'
language = 'en-gb'
word_id = 'Ace'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
```
### *To build our Dictionary  , we must following the code above*
#### 1. import the request model.
```python
import  requests
```
##### - -  [For more information on how to install requests](http://docs.python-requests.org/en/master/user/install/#install "for more information on how to install requests")
##### 2. Get your own app_id and app_key from [Oxford Dictionaries API](https://developer.oxforddictionaries.com/ "Oxford Dictionaries API")
- Example of mine key & id
```python
app_id = "b7651a9c"
app_key = "0da5d44688b3109d58d48b71f2947a11"
endpoint = "entries"
language_code = "en-us"
print("🔎 ENGLSH DICTIONNARY 📚")

```
##### 3. The rest
```python
while True:
    try:
        word_id = input('📑 ENTER WORD:')
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower() + " ?fields=definitions"
        meaning = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
        definition = meaning.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        print("---------------------------------------------------------------------")
        print('📌',definition)
        print("----------------------------------------------------------------")
        Exit = input('Type <exit> to stop or type  <search>  to continue:')
        if Exit == 'exit':
            break

    except KeyError:
        print('>>>   English required to input [input a single word] , Please try again! ')
```

