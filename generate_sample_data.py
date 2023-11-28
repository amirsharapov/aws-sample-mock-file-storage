import json
import random

from pathlib import Path

FIRST_NAMES = [
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Charles",
    "Joseph",
    "Thomas",
    "Christopher",
    "Daniel",
    "Paul",
    "Mark",
    "Donald",
    "George",
    "Kenneth",
    "Steven",
    "Edward",
    "Brian",
    "Ronald",
    "Anthony",
    "Kevin",
    "Jason",
    "Matthew",
    "Gary",
    "Timothy",
    "Jose",
    "Larry",
    "Jeffrey",
    "Frank",
    "Scott",
    "Eric",
    "Stephen",
    "Andrew",
    "Raymond",
    "Gregory",
    "Joshua",
    "Jerry",
    "Dennis",
    "Walter",
    "Patrick",
    "Peter",
    "Harold",
    "Douglas",
    "Henry",
    "Carl",
    "Arthur",
    "Ryan",
    "Roger",
    "Joe",
    "Juan",
    "Jack",
    "Albert",
    "Jonathan",
    "Justin",
    "Terry",
    "Gerald",
    "Keith",
    "Samuel",
    "Willie",
    "Ralph",
    "Lawrence",
    "Nicholas",
    "Roy",
    "Benjamin",
    "Bruce",
    "Brandon",
    "Adam",
    "Harry",
    "Fred",
    "Wayne",
    "Billy",
    "Steve",
    "Louis",
    "Jeremy",
    "Aaron",
    "Randy",
    "Howard",
    "Eugene",
    "Carlos",
    "Russell",
    "Bobby",
    "Victor",
    "Martin",
    "Ernest",
    "Phillip",
    "Todd",
    "Jesse",
    "Craig",
    "Alan",
    "Shawn",
    "Clarence",
    "Sean",
    "Philip",
    "Chris",
    "Johnny",
    "Earl",
    "Jimmy",
    "Antonio",
    "Danny",
    "Bryan",
    "Tony",
    "Luis",
    "Mike",
    "Stanley",
    "Leonard",
    "Nathan",
    "Dale",
    "Manuel",
    "Rodney",
    "Curtis",
    "Norman",
    "Allen"
]
LAST_NAMES = [
    "Smith",
    "Doe",
    "Johnson",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "Hernandez",
    "King",
    "Wright",
    "Lopez",
    "Hill",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Gonzalez",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
    "Collins",
    "Stewart",
    "Sanchez",
    "Morris",
    "Rogers",
    "Reed",
    "Cook",
    "Morgan",
    "Bell",
    "Murphy",
    "Bailey",
    "Rivera",
    "Cooper",
    "Richardson",
    "Cox",
    "Howard",
    "Ward",
    "Torres",
    "Peterson",
    "Gray",
    "Ramirez",
    "James",
    "Watson",
    "Brooks",
    "Kelly",
    "Sanders",
    "Price",
    "Bennett",
    "Wood",
    "Barnes",
    "Ross",
    "Henderson",
    "Coleman",
    "Jenkins",
    "Perry",
    "Powell",
    "Long",
    "Patterson",
    "Hughes",
    "Flores",
    "Washington",
    "Butler",
    "Simmons",
    "Foster",
    "Gonzales",
    "Bryant",
    "Alexander",
    "Russell",
    "Griffin",
    "Diaz",
    "Hayes",
]


def create_air_pollution_data():
    data = {
        "zip_codes": {}
    }

    for i in range(1000, 5000):
        data["zip_codes"][str(i)] = {
            "psi": random.randint(0, 100),
            "ozone": random.randint(0, 100),
            "pm25": random.randint(0, 100),
            "pm10": random.randint(0, 100),
            "co": random.randint(0, 100),
            "so2": random.randint(0, 100),
            "no2": random.randint(0, 100)
        }

    path = 'sample-data/air-pollution.json'

    Path(path).unlink()
    Path(path).touch()

    with open(path, "a") as output:
        output.write(
            json.dumps(
                data,
                indent=4
            )
        )


def create_company_a_customers():
    path = 'sample-data/company-a-customers.csv'

    Path(path).unlink()
    Path(path).touch()

    with open(path, 'a') as output:
        output.write('id,name,zip_code\n')

        for i in range(1000):
            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)

            output.write(f'{i},{first_name} {last_name},{random.randint(1000, 5000)}')
            output.write('\n')


if __name__ == "__main__":
    create_air_pollution_data()
    create_company_a_customers()
