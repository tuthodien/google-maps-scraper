from src import Gmaps

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "Vườn cây ăn quả"
]

Gmaps.places(queries,  use_cache=False, convert_to_english=False, geo_coordinates="21.4864463,105.824221", zoom=11)