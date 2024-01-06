import sys
from producer import publish
from datetime import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get the topic from the command line

    if len(sys.argv) < 2:
        print("Usage: python main.py <topic>")

        sys.exit(1)

    topic = sys.argv[1]

    # loop from 0 to 10 and send data to the topic

    for i in range(2000,3000):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        publish(topic, "message", {"id": i, "username": "user" + str(i), "date": date})
