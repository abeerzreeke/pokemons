# Pokemon API Tests

This repository contains a set of tests for the Pokemon API. The tests are designed to ensure the proper functioning and behavior of the API endpoints.

## Tests Overview

### 1. test_pokimons_api()

This test fetches the list of pokemons from the API and verifies:
- The response status code is 200.
- The response is in JSON format.
- The list contains exactly 20 items.

### 2. test_charmander_is_in_fire_pokemon_list()

This test fetches the list of pokemons with fire power from the API and verifies if Charmander exists in the list of fire pokemons.

### 3. test_bulbasaur_is_not_in_fire_pokemon_list()

This test fetches the list of pokemons with fire power from the API and verifies if Bulbasaur does not exist in the list of fire pokemons.

### 4. test_five_heaviest_pokemons()

This test fetches the list of pokemons with fire power from the API, calculates the weights of the pokemons, sorts them by weight, and verifies the top 5 heaviest pokemons.

## Usage

To run the tests, execute the test file using a testing framework such as pytest.

## Setup

Before running the tests, ensure you have the necessary dependencies installed. You can install them using the following command:
pip install -r requirements.txt


License
This project is licensed under the MIT License.


Credits
This project was created by Abeer.Zreeke

Contact
For any inquiries or support, please contact abeerzr14@gmail.comthon 