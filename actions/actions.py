# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSayEnemyName(Action):

    def name(self) -> Text:
        return "action_say_enemy_name"
    
    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        enemy_name = tracker.get_slot("enemy_pokemon_name")
        if not enemy_name:
            dispatcher.utter_message(text= "I don't know the enemy pokemon!")
        else:
            dispatcher.utter_message(text=f"The enemy pokémon is a {enemy_name}, correct?")
    
        return []

class ActionSayEnemyTypes(Action):

    def name(self) -> Text:
        return "action_say_enemy_types"
    
    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            api_url = "https://pokeapi.co/api/v2/pokemon/" #API
        except:
            print("API_URL NOT WORKING")
        # try catch where if slot is none, just print NONE - -> use try catch to debug
        try:
            pokemon = str(tracker.get_slot("enemy_pokemon_name")) #EXAMPLE POKEMON INPUT
        except:
            print("POKEMON NOT FOUND IN SLOT??")
        try:
            api_url+= pokemon #APPEND POKEMON TO API
        except:
            print("APPEND NOT WORKING REALLY BRUH")
        try:
            response = requests.get(api_url) # GET REQUEST TO API
        except:
            print("CANT GET RESPONSE = REQUESTS.GETAPI_URL")
        jsonObject = response.json() #TURN REQUEST INTO JSON
        typeName = ""
        typeCount = 0
        typeUrlList = []
        typeList = []
        SuperEffective = []
        NotVeryEffective = []
        DoesNotAffect = []
        for type in jsonObject['types']:
            typeCount += 1
            typeList.append(type.get('type').get('name'))
            typeUrlList.append(type.get('type').get('url'))
        print(typeList)
        dispatcher.utter_message(text="{} has these typings:".format(pokemon))

        for x in range(len(typeList)):
            dispatcher.utter_message(text= "{}, ".format(x))

        return []

class ActionHelloWorld(Action):
     

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #api_url = "https://pokeapi.co/api/v2/pokemon/ditto"
        #response = requests.get(api_url)
        #response.json()
        #dispatcher.utter_message(json_message=self.response.json())
        dispatcher.utter_message(text="Hello World!")
        return []
