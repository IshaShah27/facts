import wikipedia

search_term = "sddfs"

# take in date of query
# index the sentences that are returned based on time since that date
# figure out whether there are any sentences remaining that haven't been shared
# create a stop, somehow


try:
    resp = wikipedia.summary(search_term) 
except wikipedia.exceptions.DisambiguationError as err:
    print(f"Sorry, '{err.title}' was not a great search term. Let's try another.")
    new_opts = err.options
    print(f"Your new search term is '{new_opts[0]}'. Hope that's cool.")
    resp = wikipedia.summary(new_opts[0])
except wikipedia.exceptions.PageError:
    print("Nah man, that doesn't return any results. Try again bromie.")





# import requests
# from bs4 import BeautifulSoup
 
# # update - take subject from command line
# subject = 'aboveground biomass'
 
# url = 'https://en.wikipedia.org/w/api.php'
# params = {
#             'action': 'parse',
#             'page': subject,
#             'format': 'json',
#             'prop':'text',
#             'redirects':''
#         }
 
# response = requests.get(url, params=params)
# print(response.status_code)
# data = response.json()
# # if data["error"] is not None:

# # print(data["error"])
 
# raw_html = data['parse']['text']['*']
# soup = BeautifulSoup(raw_html,'html.parser')
# soup.find_all('p')
# text = ''
 
# for p in soup.find_all('p'):
#     text += p.text

# print(text[:58])