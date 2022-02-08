from flask import Flask, jsonify
# Using wikipedia module to get data from wikipedia
import wikipedia
from wikipedia.exceptions import DisambiguationError

app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = 'wiki-search.com:5000'

# route takes subdomain term


@app.route('/', subdomain='<term>', methods=['GET'])
def wiki(term):
    links = []
    # stores data in results
# Using Try and except to handle disambiguation errrors
    try:
        link = wikipedia.WikipediaPage(term).url
        return jsonify(links=link)
    except Exception as error:
        results = error.options

        for result in results:
            try:
                links.append(wikipedia.WikipediaPage(result).url)
            except Exception as error:
                print("This is the error for result: " + result)
    return jsonify(links=links)


if __name__ == "__main__":
    app.run(debug=True)
