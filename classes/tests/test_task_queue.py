from classes.APIConnector import APIConnector
from classes.NameGenerator import NameGenerator


def test():
    print('executed.')


def main():
    api = APIConnector(profile_name="co_troya")
    api.get_queued_events()

if __name__ == "__main__":
    # execute only if run as a script
    main()
