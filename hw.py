import requests


def get_random_joke():
    '''Fetch a random joke from official Joke API'''
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        # One line to print the JSON respose(for debugging)
        # print(f"Full JSON responce: {response.json()}")
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return f"Failed to retrieve joke. Status code: {response.status_code}"


def main():
    print("Welcome to Random Joke Generator")

    while True:
        user_input = input(
            "Press Enter to egt a new joke, or type 'q' or 'exit' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Bye!")
            break

        joke = get_random_joke()
        print(f"{joke}\n")


if __name__ == "__main__":
    main()


