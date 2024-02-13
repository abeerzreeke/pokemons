import json
import requests
from requests import RequestException
from tests.enums_values import PokemonPowerType, PokemonNames, PokemonProperty


class Endpoint:
    URL = 'https://pokeapi.co/api/v2/type'


class RequestTypes:
    GET = requests.get


class StatusCodes:
    STATUS_200 = 200


class HTTPRequests:

    @staticmethod
    def get_pokemons_list(api_url: str):
        try:
            response = requests.get(api_url)

            # Check if the response is failed
            if response.status_code != StatusCodes.STATUS_200:
                raise requests.exceptions.HTTPError(f"HTTP error {response.status_code}: {response.reason}")

            # Return response content
            return response
        except RequestException as e:
            print('Could not request {} due to an exception: {}'.format(Endpoint.URL, e))

    def get_pokemons_list_by_power_type(self, power_type: PokemonPowerType):
        # Get all pokemons list
        all_pokemons_list = self.get_pokemons_list(Endpoint.URL)

        # Read response content
        pokemons_list_by_power = json.loads(all_pokemons_list.content)['results']

        # Get specific pokemon power url
        pokemon_power_url = self.find_url_by_name(pokemons_list_by_power, power_type.value)

        # Fetch pokemons list
        pokemons_power_type_list = self.get_pokemons_list(pokemon_power_url)
        return pokemons_power_type_list

    @staticmethod
    def find_url_by_name(dict_list, search_name):
        for item in dict_list:
            if item['name'] == search_name:
                return item['url']
        return None

    @staticmethod
    def is_pokemon_name_exists_in_list(pokemons_list: list, searched_pokemon: PokemonNames):
        for pokemon in pokemons_list:
            pokemon_name = pokemon['pokemon']['name']
            if searched_pokemon.value in pokemon_name:
                return True
        return False

    def loop_over_pokemons_and_fetch_specific_property(self, fire_pokemons_list: dict, pokemon_property: PokemonProperty):
        pokemons_info = {}
        for pokemon in fire_pokemons_list['pokemon']:
            specific_pokemon_info = self.get_pokemons_list(pokemon['pokemon']['url'])
            response_content = json.loads(specific_pokemon_info.content)

            pokemons_info[pokemon['pokemon'][pokemon_property.Name.value]] = response_content[pokemon_property.Weight.value]
        return pokemons_info

    @staticmethod
    def get_the_first_amount_of_dictionary_values(items: dict, amount: int):
        values_list = {}
        for key in list(items.keys())[:amount]:
            values_list[key] = items[key]
        return values_list
