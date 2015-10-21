'''
Settings file to store basic information in a central location. A database should not be required at this time. If at any point
Should we require to store secure information a database will have to be implemented.
'''

# Users to notify
# [0] Add user groups or OU's when the user base becomes large and requires Zone split
#     e.g. Brittany and Keagan get notification pertaining to just their apartment if a whole building is running Secsys

servers = {
    'primary': '45.32.245.71',
    'raspberrypi': '10.0.0.20'  # Statically assigned locally
}

# Users of the system who can be alerted
users = {
    'system': {
        'secsys': 'secsys@' + str(servers['primary'])
    },
    'administrators': {
        'keags': 'keags@' + str(servers['primary']),
        'brodie': 'brodie@' + str(servers['primary'])
    },
    'notify': {
        'brittany': 'brittany@' + str(servers['primary'])
    }
}
