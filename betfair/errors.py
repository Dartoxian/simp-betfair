'''
    Module to check whether the api response is valid
'''

known_errors = {
   "DSC-0009": {
        "Exception": "ClassConversionFailure",
        "Fault": "Client",
        "Description": "400 Invalid format for parameter, for example passing a string where a number was expected. Can also happen when a value is passed that does not match any valid enum."
    },
    "DSC-0018": {
        "Exception": "MandatoryNotDefined",
        "Fault": "Client",
        "Description": "400 A parameter marked as mandatory was not provided"
    },
    "DSC-0019": {
        "Exception": "Timeout",
        "Fault": "Server",
        "Description": "504 The request has timed out"
    },
    "DSC-0021": {
        "Exception": "NoSuchOperation",
        "Fault": "Client",
        "Description": "404 The operation specified does not exist"
    },
    "DSC-0023": {
        "Exception": "NoSuchService",
        "Fault": "Client",
        "Description": "404  "
    },
    "DSC-0034": {
        "Exception": "UnknownCaller",
        "Fault": "Client",
        "Description": "400 An App Key hasn't been provided in the request"
    },
    "DSC-0035": {
        "Exception": "UnrecognisedCredentials",
        "Fault": "Client",
        "Description": "400  "
    },
    "DSC-0036": {
        "Exception": "InvalidCredentials",
        "Fault": "Client",
        "Description": "400  "
    },
    "DSC-0037": {
        "Exception": "SubscriptionRequired",
        "Fault": "Client",
        "Description": "403 The user is not subscribed to the App Key provided"
    },
    "DSC-0038": {
        "Exception": "OperationForbidden",
        "Fault": "Client",
        "Description": "403 The App Key sent with the request is not permitted to access the operation"
    } 
}


def success(response):
    return response.status_code == 200

def detail(response):
    r_json = response.json()
    if r_json['faultstring'] in known_errors:
        return known_errors[r_json['faultstring']]
    else:
        return {
            'Exception': 'UnknownError',
            'Fault': 'Unknown',
            'Description': 'An undocumented error has occurred. Please expand the library with documentation of this error: %s'%r_json
        } 
