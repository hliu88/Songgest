# Songgest
 
## Setup
To set up the enviroment, run:
`make dev_env`

## Description
Songgest is a music utility service that replaces music streaming service's recommendation system. Recommendation systems currently often recommends from artists or even songs that is in user's playlist, or recommends the same songs everytime. The algorithm shows its weakness especially for users who does not consume main stream generas/artists. Songgest is a service that intends to provide better song recommendations to users. User of Songgest will be able to view and understand their favourite music and be able to get music recommendations talored to their own likings.

## Requirements
1. User can import their playlist 
1. User can choose to login to circumvent recommendations to the same songs from a playlist
1. User can view statistics about their playlist
1. User has the option to fine tune algorithm with the ability to favor
    1. Newer
    1. Popular
    1. Trending
    1. Related artists 
1. User can view/import suggested playlist into their own Spotify account

## Design
1. Flask
1. Spotipy
1. SKlearn
1. Keras/Tensorflow
1. Pydoc
1. Unittest, nose, flake8, coverage
1. SQL
1. React
1. Heroku


