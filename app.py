import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_tube_stops():
    return [
        "Acton Town", "Aldgate", "Aldgate East", "Alperton", "Amersham", "Angel", "Archway", 
        "Arnos Grove", "Arsenal", "Baker Street", "Balham", "Bank", "Barbican", "Barking", 
        "Barkingside", "Barons Court", "Battersea Power Station", "Bayswater", "Becontree", 
        "Belsize Park", "Bermondsey", "Bethnal Green", "Blackfriars", "Blackhorse Road", 
        "Bond Street", "Borough", "Boston Manor", "Bounds Green", "Bow Road", "Brent Cross", 
        "Brixton", "Bromley-by-Bow", "Buckhurst Hill", "Burnt Oak", "Caledonian Road", 
        "Camden Town", "Canada Water", "Canary Wharf", "Canning Town", "Cannon Street", 
        "Canons Park", "Chalfont & Latimer", "Chalk Farm", "Chancery Lane", "Charing Cross", 
        "Chesham", "Chigwell", "Chiswick Park", "Chorleywood", "Clapham Common", 
        "Clapham North", "Clapham South", "Cockfosters", "Colindale", "Colliers Wood", 
        "Covent Garden", "Croxley", "Dagenham East", "Dagenham Heathway", "Debden", 
        "Dollis Hill", "Ealing Broadway", "Ealing Common", "Earl's Court", "East Acton", 
        "East Finchley", "East Ham", "East Putney", "Eastcote", "Edgware", "Edgware Road", 
        "Elephant & Castle", "Elm Park", "Embankment", "Epping", "Euston", "Euston Square", 
        "Fairlop", "Farringdon", "Finchley Central", "Finchley Road", "Finsbury Park", 
        "Fulham Broadway", "Gants Hill", "Gloucester Road", "Golders Green", 
        "Goldhawk Road", "Goodge Street", "Grange Hill", "Great Portland Street", "Green Park", 
        "Greenford", "Gunnersbury", "Hainault", "Hammersmith", "Hampstead", "Hanger Lane", 
        "Harlesden", "Harrow & Wealdstone", "Harrow-on-the-Hill", "Hatton Cross", 
        "Heathrow Terminals 2 & 3", "Heathrow Terminal 4", "Heathrow Terminal 5", 
        "Hendon Central", "High Barnet", "High Street Kensington", "Highbury & Islington", 
        "Highgate", "Hillingdon", "Holborn", "Holland Park", "Holloway Road", "Hornchurch", 
        "Hounslow Central", "Hounslow East", "Hounslow West", "Hyde Park Corner", "Ickenham", 
        "Kennington", "Kensal Green", "Kensington (Olympia)", "Kentish Town", "Kenton", 
        "Kew Gardens", "Kilburn", "Kilburn Park", "King's Cross St. Pancras", "Kingsbury", 
        "Knightsbridge", "Ladbroke Grove", "Lambeth North", "Lancaster Gate", "Latimer Road", 
        "Leicester Square", "Leyton", "Leytonstone", "Liverpool Street", "London Bridge", 
        "Loughton", "Maida Vale", "Manor House", "Mansion House", "Marble Arch", "Marylebone", 
        "Mile End", "Mill Hill East", "Monument", "Moor Park", "Moorgate", "Morden", 
        "Mornington Crescent", "Neasden", "Newbury Park", "Nine Elms", "North Acton", "North Ealing", 
        "North Greenwich", "North Harrow", "North Wembley", "Northfields", "Northolt", 
        "Northwick Park", "Northwood", "Northwood Hills", "Notting Hill Gate", "Oakwood", 
        "Old Street", "Osterley", "Oval", "Oxford Circus", "Paddington", "Park Royal", 
        "Parsons Green", "Perivale", "Piccadilly Circus", "Pimlico", "Pinner", "Plaistow", 
        "Preston Road", "Putney Bridge", "Queen's Park", "Queensbury", "Queensway", 
        "Ravenscourt Park", "Rayners Lane", "Redbridge", "Regent's Park", "Richmond", 
        "Rickmansworth", "Roding Valley", "Royal Oak", "Ruislip", "Ruislip Gardens", 
        "Ruislip Manor", "Russell Square", "Seven Sisters", "Shepherd's Bush", 
        "Shepherd's Bush Market", "Sloane Square", "Snaresbrook", "South Ealing", 
        "South Harrow", "South Kensington", "South Kenton", "South Ruislip", "South Wimbledon", 
        "South Woodford", "Southfields", "Southgate", "Southwark", "St. James's Park", 
        "St. John's Wood", "St. Paul's", "Stamford Brook", "Stanmore", "Stepney Green", 
        "Stockwell", "Stonebridge Park", "Stratford", "Sudbury Hill", "Sudbury Town", 
        "Swiss Cottage", "Temple", "Theydon Bois", "Tooting Bec", "Tooting Broadway", 
        "Tottenham Court Road", "Tottenham Hale", "Totteridge & Whetstone", "Tower Hill", 
        "Tufnell Park", "Turnham Green", "Turnpike Lane", "Upminster", "Upminster Bridge", 
        "Upney", "Upton Park", "Uxbridge", "Vauxhall", "Victoria", "Walthamstow Central", 
        "Wanstead", "Warren Street", "Warwick Avenue", "Waterloo", "Watford", 
        "Wembley Central", "Wembley Park", "West Acton", "West Brompton", "West Finchley", 
        "West Ham", "West Hampstead", "West Harrow", "West Kensington", "West Ruislip", 
        "Westbourne Park", "Westminster", "White City", "Whitechapel", "Willesden Green", 
        "Willesden Junction", "Wimbledon", "Wimbledon Park", "Wood Green", "Woodford", 
        "Woodside Park"
    ]

def has_no_common_letters(stop, input_text):
    stop_letters = set(stop.lower().replace(" ", "").replace("&", ""))
    input_letters = set(input_text.lower().replace(" ", "").replace("&", ""))
    return stop_letters.isdisjoint(input_letters)

def find_unique_stop(input_text):
    tube_stops = get_tube_stops()
    unique_stops = [stop for stop in tube_stops if has_no_common_letters(stop, input_text)]

    if len(unique_stops) == 1:
        return {
            "success": True,
            "message": f"Congratulations! You've entered '{input_text}' which shares no letters with exactly one tube stop.",
            "matching_stops": unique_stops
        }
    elif len(unique_stops) == 0:
        return {
            "success": False,
            "message": f"Bad luck! There are no tube stops which share exactly 0 letters with '{input_text}'. Try a different word or phrase.",
            "matching_stops": []
        }
    else:
        return {
            "success": False,
            "message": f"Bad luck! There are {len(unique_stops)} tube stops that share no letters with '{input_text}'. Here they are:",
            "matching_stops": unique_stops
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/find-unique-stop', methods=['POST'])
def api_find_unique_stop():
    input_text = request.json.get('input_text', '')
    result = find_unique_stop(input_text)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)