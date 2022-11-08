import wikipedia

# take in date of query
# index the sentences that are returned based on time since that date
# figure out whether there are any sentences remaining that haven't been shared
# if no more sentences left, then throw random facts - or (more advanced) the results from the first suggestion
# create a stop, somehow (if user inputs "stop facts" from slack then stop running this bot)

def get_summary(search_term):

    try:
        if search_term!="":
            resp = wikipedia.summary(search_term) 
        else:
            resp="how about you try a little something"
    except wikipedia.exceptions.DisambiguationError as err:
        new_opts = err.options
        resp=f"ok, so actually, '{err.title}' turns out not be a great search term. i'll cut you a deal. your new search term is '{new_opts[0]}'. and you're going to learn to live with it:\n"
        resp = resp + wikipedia.summary(new_opts[0])
    except wikipedia.exceptions.PageError:
        resp="na man, that doesn't return any results. Try again brohannes gutenbro."
    return resp

