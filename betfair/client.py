import json
import requests
import errors
import constants

class SimpleBetfairClient:

    # Setup

    endpoint = 'https://api.betfair.com/exchange/betting/rest/v1.0/'

    def __init__(self, appKey, sessionToken):
        self._appKey = appKey
        self._sessionToken = sessionToken

        self.init_headers()

    def init_headers(self):
        self._headers = {
            'X-Application': self._appKey, 
            'X-Authentication': self._sessionToken, 
            'content-type': 'application/json',
            'Connection': 'keep-alive'
        }

    def _query(self, method, payload):
        response = requests.post(self.endpoint + method, headers=self._headers, data=json.dumps(payload))
        if errors.success(response):
            return response.json()
        else:
            return errors.detail(response)

    # API
    
    def list_countries(self, market_filter = {}):
        response = self._query( 'listCountries/', {
            'filter': market_filter,
            'locale': 'EN'
        }) 
        return response

    # Markets

    def list_events(self, market_filter = {}):
        response = self._query( 'listEvents/', {
            'filter': market_filter,
            'locale': 'EN'
        })
        return response

    def list_event_types(self, market_filter = {}):
        response = self._query( 'listEventTypes/', {
            'filter': market_filter,
            'locale': 'EN'
        })
        return response

    def list_market_types(self, market_filter = {}):
        response = self._query( 'listMarketTypes/', {
            'filter': market_filter,
            'locale': 'EN'
        })
        return response

    def list_market_catalogue(self, market_filter = {}, market_projection = [], max_results = 100, sort = None): 
        params = {
            'filter': market_filter,
            'marketProjection': [x.name for x in market_projection],
            'maxResults': max_results,
            'locale': 'EN'
        }
        if sort != None:
            params['sort'] = sort.name
        response = self._query( 'listMarketCatalogue/', params)
        return response

    # Orders

    def list_current_orders(self):
        response = self._query( 'listCurrentOrders/', {
        })
        return response

class MarketFilter():
    def __init__(self):
        self._rep = {}

    def _add_set_value(self, field, val):
        if field not in self._rep:
            self._rep[field] = []
        self._rep[field].append(val)

    def _set_scalar_value(self, field, val):
        self._rep[field] = val

    def get_filter(self):
        return self._rep

    def filter_text(self, text):
        self._set_scalar_value('textQuery', text)

    def filter_event_type(self, eventType):
        self._add_set_value('eventTypeIds', eventType)

    def filter_event(self, event):
        self._add_set_value('eventIds', event)

    def filter_competition(self, competition):
        self._add_set_value('competitionIds', competition)

    def filter_market(self, market):
        self._add_set_value('marketIds', market)

    def filter_venue(self, venue):
        self._add_set_value('venues', venue)

    def filter_bsp(self, bsp):
        # bsp = Betfair Starting Price.
        self._set_scalar_value('bspOnly', bsp)

    def filter_in_play(self, in_play):
        self._set_scalar_value('inPlayOnly', in_play)

    def filter_turn_in_play(self, turn_in_play):
        self._set_scalar_value('turnInPlayEnabled', turn_in_play)

    def filter_market_country(self, country):
        self._add_set_value('marketCountries', country)

    def filter_market_betting_type(self, market_betting_type):
        self._add_set_value('marketBettingTypes', market_betting_type.name)

    def filter_market_type(self, market_type):
        self._add_set_value('marketTypeCodes', market_type)

    def filter_market_start_time_range(self, start, end):
        # date in format yyyy-mm-dd hh:mm:ss
        self._set_scalar_value('marketStartTime', {'from': start, 'to': end})





