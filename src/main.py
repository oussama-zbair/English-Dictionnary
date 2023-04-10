import requests

def get_definition(word: str) -> str:
    """
    Returns the definition of the given word using the Oxford Dictionaries API.
    
    Parameters:
        word (str): The word to look up.
        
    Returns:
        str: The definition of the word.
    """
    app_id = "b7651a9c"
    app_key = "0da5d44688b3109d58d48b71f2947a11"
    endpoint = "entries"
    language_code = "en-us"

    url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/{word.lower()}?fields=definitions"
    response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    data = response.json()
    definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    return definition

def main():
    print("🔎 ENGLISH DICTIONARY 📚")
    while True:
        word = input("Enter a word: ")
        definition = get_definition(word)
        print(f"📌 {definition}")
        if input("Type 'exit' to exit or 'continue' to look up another word: ") == "exit":
            break

if __name__ == "__main__":
    main()
