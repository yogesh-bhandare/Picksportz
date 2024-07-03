# Welcome to Picksportz

## Project Overview
"Sport has the power to change the world. It has the power to inspire. It has the power to unite people in a way that little else does." - Nelson Mandela

Picksportz is an innovative platform designed to bring sports enthusiasts together. Whether you have a full team with a couple of spots to fill or are an individual looking to join a game, Picksportz connects players and organizes team sports games on nearby turfs. By making it easier for everyone to participate, Picksportz not only encourages physical activity but also fosters community and camaraderie.

## Motivation
In today's digital age, finding people to play sports with can be a challenge. Many individuals are eager to play but lack a full team or have friends who aren't interested in sports. This often results in missed opportunities for physical activity and social interaction. Picksportz addresses this issue by creating a platform that fills the gaps in teams, ensuring that everyone has a chance to play. Additionally, sharing the cost of turf rental makes the experience more affordable and accessible.

## What It Does
Picksportz allows users to:

- Join teams with open spots for various sports games.
- Find nearby turfs where games are organized.
- Share the cost of turf rental with other players.

By matching players based on location and availability, Picksportz makes it easy for anyone to find a game to join and enjoy the benefits of team sports.

## Features
### Team Integration
- **Fill Open Spots:** Connects players who are looking to join games with teams that have open spots.
- **Easy Team Formation:** Helps individuals and groups form complete teams for various sports.

### Location-Based Matching
- **Nearby Turfs:** Organizes games on turfs that are conveniently located for the players.
- **Geolocation Services:** Uses location data to suggest games and turfs near the user's home.

### Cost Sharing
- **Turf Rental Distribution:** Splits the cost of renting turf among all players, making it more affordable.
- **Transparent Pricing:** Provides clear information on costs to ensure fairness and transparency.

## How We Built It
Picksportz is developed using a combination of modern web technologies and tools. The platform is built with:

- **Frontend:** React.js for a responsive and intuitive user interface.
- **Backend:** Django and Django Rest Framework for robust server-side operations.
- **Database:** PostgreSQL for reliable and scalable data storage.
- **Geolocation:** Google Maps API for location-based services.
- **Payment Integration:** Stripe API for secure and seamless transactions.

## Challenges
One of the main challenges we faced was ensuring real-time updates for game availability and team spots. We addressed this by implementing WebSocket communication to keep all users informed of changes instantly. Additionally, integrating location services to accurately suggest nearby turfs required careful calibration and testing.

## What We Learned
Throughout the development of Picksportz, we gained significant insights into real-time data handling and geolocation integration. We also learned the importance of user feedback in refining our platform to better meet the needs of sports enthusiasts. Our team enhanced its skills in full-stack development and collaborative project management.

## What's Next for Picksportz
We are excited about the future of Picksportz and have several plans for its continued growth:

- **Enhanced Matching Algorithms:** Improve the accuracy of player and team matching based on skill levels and preferences.
- **Expanded Sports Categories:** Include more sports to cater to a broader audience.
- **Community Features:** Add social features such as team chats, player profiles, and game highlights.
- **Mobile App Development:** Launch a mobile app for greater accessibility and convenience.

## Getting Started
To start using Picksportz, follow these simple steps:

1. **Sign Up:** Create an account on the Picksportz website.
2. **Find or Create a Game:** Search for available games or create a new game and list open spots.
3. **Join a Team:** Select a game and join a team with available spots.
4. **Play and Enjoy:** Participate in the game at a nearby turf and enjoy playing with new friends.

Thank you for your interest in Picksportz. We are committed to making sports more accessible and enjoyable for everyone. Let's play!

# Django API Project Setup

This repository contains a Django API project setup guide with instructions on installing Virtualenv, creating a virtual environment outside the API project directory, installing Django and Django Rest Framework, and running the Django app.

## Prerequisites

Before proceeding with the setup, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation Steps

### 1. Install Virtualenv

```
pip install virtualenv

virtualenv myenv

myenv\Scripts\activate

pip install django djangorestframework

git clone <repository-url>

cd <api-project-directory>

python manage.py runserver
