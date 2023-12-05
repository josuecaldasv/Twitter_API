# Twitter_API

## 1. About

Explore and analyze Twitter timelines effortlessly. This tool allows users to access and navigate through a user's timeline while providing the functionality to save selected parameters and the number of tweets chosen for a customized experience.

## 2. Using the `get_timeline` function

The `get_timeline` function in module in the `function` module is designed to retrieve and save a user's Twitter timeline data from the Twitter API in a JSON file. Follow the steps below to use this function effectively:

### Parameters:

- **username (str):** The Twitter username of the target user.
- **max_tweets (int):** The maximum number of tweets to retrieve.
- **param_list (list):** A list of tweet fields to include in the API response.
- **keys (str):** The path to the JSON file containing Twitter API keys.
- **path (str):** The directory path to save the JSON file.

### Example Usage:

```python
import function as fn

# Replace these values with your actual data
username   = 'target_username'
max_tweets = 10
param_list = ['tweet_field_1', 'tweet_field_2']
keys_path  = 'path/to/your/keys.json'
save_path  = 'path/to/save/json/file'

# Call the function
fn.get_timeline( username, max_tweets, param_list, keys_path, save_path )
