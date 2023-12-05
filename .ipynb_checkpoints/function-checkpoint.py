import requests
import os
import json


def create_url( username, max_tweets = 100 ):
    
    '''
    Creates and returns the Twitter API endpoint URL for fetching recent tweets from a specific user.

    Parameters:
    - username (str): The Twitter username of the target user.
    - max_tweets (int): The maximum number of tweets to retrieve (default is 100).

    Returns:
    - str: The formatted URL for the Twitter API endpoint.
    '''
    
    return f'https://api.twitter.com/2/tweets/search/recent?query=from:{ username }&max_results={ max_tweets }'


def get_params( param_list ):
    
    '''
    Generates and returns the dictionary of parameters for the Twitter API request.

    Parameters:
    - param_list (list): A list of tweet fields to include in the API response.

    Returns:
    - dict: A dictionary containing the tweet fields as keys and their values.
    '''
    
    param_value = ','.join( param_list )
    params_dict = { 'tweet.fields': param_value }

    return params_dict


def bearer_oauth( r, bearer_token ):
   
    '''
    Adds the necessary headers (Authorization and User-Agent) to the HTTP request for authentication.

    Parameters:
    - r: The HTTP request object.
    - bearer_token (str): The Twitter API bearer token for authentication.

    Returns:
    - The modified HTTP request object.
    '''
    
    r.headers[ 'Authorization' ] = f'Bearer { bearer_token }'
    r.headers[ 'User-Agent' ]    = 'v2UserTweetsPython'
    return r


def connect_to_endpoint( url, params, bearer_token ):
    
    '''
    Connects to the Twitter API endpoint using the provided URL, parameters, and bearer token.

    Parameters:
    - url (str): The Twitter API endpoint URL.
    - params (dict): The parameters for the API request.
    - bearer_token (str): The Twitter API bearer token for authentication.

    Returns:
    - dict: The JSON response from the API.
    '''
    
    r        = requests.Request( 'GET', url, params = params ).prepare()
    r        = bearer_oauth( r, bearer_token )
    response = requests.Session().send( r )
    print( response.status_code )
    
    if response.status_code != 200:  
        raise Exception( f'Request returned an error: { response.status_code } { response.text }' ) 
    return response.json()        
        

def get_timeline( username, max_tweets, param_list, keys, path ):
    
    
    '''
    Retrieves and saves the user's timeline data from Twitter API in a JSON file.

    Parameters:
    - username (str): The Twitter username of the target user.
    - max_tweets (int): The maximum number of tweets to retrieve.
    - param_list (list): A list of tweet fields to include in the API response.
    - keys (str): The path to the JSON file containing Twitter API keys.
    - path (str): The directory path to save the JSON file.

    Returns:
    - None
    '''
    
    with open( keys, 'r' ) as file:
        keys_loades = json.load( file )
    
    bearer_token  = keys_loades.get( 'bearer_token' )
    url           = create_url( username, max_tweets )
    params        = get_params( param_list )
    json_response = connect_to_endpoint( url, params, bearer_token )    
    
    os.makedirs( path, exist_ok = True )
    file_path = os.path.join( path, username + '.json' )

    with open( file_path, 'w', encoding = 'utf-8' ) as json_file:
        json.dump( json_response, json_file, ensure_ascii = False, indent = 4 )
        

    print( f'Data saved in { file_path }' )