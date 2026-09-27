"City Info App"
# pylint: disable=no-member

import os
# import math
from urllib.parse import urlparse
import boto3
from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)
# Connect to your AWS account DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Specify your AWS region
cities_table = dynamodb.Table('Cities')
reviews_table = dynamodb.Table('CityReviews')

def nl2br(value):
    """Replace newlines with <br> tags."""
    return Markup(value.replace("\n", "<br>"))

def relative_url(endpoint):
    """Build a relative URL from an absolute path."""
    start_dir = os.path.dirname(urlparse(request.url).path)
    relative_path = os.path.relpath(endpoint, start=start_dir)
    return relative_path

# Register the custom filters with Flask
app.jinja_env.filters['nl2br'] = nl2br
app.jinja_env.filters['relative_url'] = relative_url

def load_cities():
    """Load all the cities from the data store"""
    results = []
    response = cities_table.scan()
    for item in response['Items']:
        city = {
            "Name": item['CityName'],
            "CountryCode": item['CountryCode'],
            "CountryName": item['CountryName'],
            "TopThingsToDo": item['TopThingsToDo'],
            "Itinerary": item['Itinerary']
        }
        results.append(city)
    return results

def load_city(name):
    """Load a city name and country code"""
    response = cities_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('CityName').eq(name)
    )
    if response['Items']:
        item = response['Items'][0]
        return {
            "Name": item['CityName'],
            "CountryCode": item['CountryCode'],
            "CountryName": item['CountryName'],
            "TopThingsToDo": item['TopThingsToDo'],
            "Itinerary": item['Itinerary']
        }
    return None


def load_city_reviews(name):
    """Load all reviews for a given city from DynamoDB."""
    results = []
    response = reviews_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('CityName').eq(name)
    )
    for item in response['Items']:
        review = {
            "ReviewContent": item['ReviewContent'],
            "Stars": int(item['Stars'])
        }
        results.append(review)
    return results

@app.route('/')
def home_route():
    """Render the homepage with the list of cities."""
    cities = load_cities()
    return render_template('index.html', cities=cities)

@app.route('/city/<name>')
def city_route(name):
    """Render a city page"""
    city = load_city(name)
    if not city:
        return render_template('404.html'), 404
    reviews = load_city_reviews(name)
    return render_template('city.html', city=city, reviews=reviews)
