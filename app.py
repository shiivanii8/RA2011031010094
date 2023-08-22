from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Dummy data for trains (you should fetch this from the John Doe Railway Server)
trains_data = [
    {
        "trainName": "Chennai Exp",
        "trainNumber": "2344",
        "departureTime": {
            "Hours": 21,
            "Minutes": 35,
            "Seconds": 0
        },
        "seatsAvailable": {
            "sleeper": 3,
            "AC": 1
        },
        "price": {
            "sleeper": 5,
            "AC": 15
        },
        "delayedBy": 15
    },
    {
        "trainName": "Hyderabad Exp",
        "trainNumber": "2341",
        "departureTime": {
            "Hours": 23,
            "Minutes": 55,
            "Seconds": 0
        },
        "seatsAvailable": {
            "sleeper": 6,
            "AC": 7
        },
        "price": {
            "sleeper": 554,
            "AC": 1854
        },
        "delayedBy": 5
    },
    # Add more train data here
]

# Function to filter and sort trains based on requirements
def filter_and_sort_trains(trains):
    # Filter and sort logic here (as per your requirements)
    # You should filter trains departing in the next 12 hours and sort them
    # based on price, ticket availability, and departure time after considering delays
    # Sample logic below, adjust as needed
    filtered_trains = [train for train in trains if train["delayedBy"] <= 30]
    sorted_trains = sorted(filtered_trains, key=lambda x: (x["price"]["sleeper"], -x["seatsAvailable"]["sleeper"], -(x["departureTime"]["Hours"] * 60 + x["departureTime"]["Minutes"])))

    return sorted_trains

# Define an endpoint to get filtered and sorted trains
@app.route('/api/trains', methods=['GET'])
def get_trains():
    filtered_trains = filter_and_sort_trains(trains_data)
    return jsonify(filtered_trains)

if __name__ == '__main__':
    app.run(debug=True)