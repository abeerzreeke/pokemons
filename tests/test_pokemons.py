import json
from api_functions import HTTPRequests, StatusCodes, Endpoint
from test_utils import decorate_test
from assertpy import assert_that
from tests.Constants import Const
from tests.enums_values import PokemonPowerType, PokemonNames, PokemonProperty


class TestStations:

    @staticmethod
    @decorate_test
    def test_pokimons_api():
        # Fetch pokemons list
        pokemons_list_response = HTTPRequests.get_pokemons_list(api_url=Endpoint.URL)

        # Very response code is 200
        assert_that(pokemons_list_response.status_code).described_as('Very response code is 200')\
            .is_equal_to(StatusCodes.STATUS_200)

        # Verify the response is JSON
        response_headers = dict(pokemons_list_response.headers)
        assert_that(response_headers['Content-Type']).described_as('Verify the response is JSON') \
            .contains('application/json')

        # Read response content
        pokemons_list = json.loads(pokemons_list_response.content)

        # Verify the list contains 20 items
        assert_that(pokemons_list['count']).described_as('Verify the list contains 20 items') \
            .is_equal_to(20)

    @decorate_test
    def test_charmander_is_in_fire_pokemon_list(self):
        # Fetch pokemons list with fire power
        http_requests_instance = HTTPRequests()
        pokemons_list_response = http_requests_instance.get_pokemons_list_by_power_type(
            power_type=PokemonPowerType.Fire)

        # Read response content
        fire_pokemons_list = json.loads(pokemons_list_response.content)['pokemon']

        # Verify Charmander exists in the fire pokemons list
        is_charmander_exists = http_requests_instance.is_pokemon_name_exists_in_list(
            pokemons_list=fire_pokemons_list, searched_pokemon=PokemonNames.Charmander)
        assert_that(is_charmander_exists).described_as('Verify Charmander exists in fire pokemons list').is_true()

    @decorate_test
    def test_bulbasaur_is_in_fire_pokemon_list(self):
        # Fetch pokemons list with fire power
        http_requests_instance = HTTPRequests()
        pokemons_list_response = http_requests_instance.get_pokemons_list_by_power_type(
            power_type=PokemonPowerType.Fire)

        # Read response content
        fire_pokemons_list = json.loads(pokemons_list_response.content)['pokemon']

        # Verify Bulbasaur does not exist in the fire pokemons list
        is_charmander_exists = http_requests_instance.is_pokemon_name_exists_in_list(
            pokemons_list=fire_pokemons_list, searched_pokemon=PokemonNames.Bulbasaur)
        assert_that(is_charmander_exists).described_as('Verify Charmander exists in fire pokemons list').is_false()

    @decorate_test
    def test_five_heaviest_pokemons(self):
        # Fetch pokemons list with fire power
        http_requests_instance = HTTPRequests()
        pokemons_list_response = http_requests_instance.get_pokemons_list_by_power_type(
            power_type=PokemonPowerType.Fire)

        # Read response content
        fire_pokemons_list = json.loads(pokemons_list_response.content)

        # Get fire pokemons weight
        pokemons_weights = http_requests_instance.loop_over_pokemons_and_fetch_specific_property(
            fire_pokemons_list=fire_pokemons_list, pokemon_property=PokemonProperty.Weight)

        # Sort the pokemons by the biggest weights
        sorted_weights = dict(sorted(pokemons_weights.items(), key=lambda item: item[1], reverse=True))
        top_5_heavy_weights = http_requests_instance.get_the_first_amount_of_dictionary_values(
            items=sorted_weights, amount=5)

        # Verify correct 5 heaviest weights
        assert_that(top_5_heavy_weights).described_as('Verify correct 5 heaviest weights') \
            .is_equal_to(Const.HEAVIEST_FIRE_POKEMONS)
