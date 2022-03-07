# PROBLEM STATEMENT -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a script that generates a report of which users are logged in to which machines at that time
# 1. What information is used as input and what information is used as output.
# A. Input is list of events
# B. Each event is an instance of the event class
# C. Event class: Contains the DATE when the event happened, the NAME of the machine where it happened, the USER involved, and the event TYPE
# D. We care about the LOGIN and LOGOUT event type

# NAMES OF ATTRIBUTES
# DATE, USER, MACHINE, and TYPE

# event types are strings and we care about LOGIN and LOGOUT

# Script will receive a list of event objects and will access the event's attributes. - We'll know if the user is logged in or not

# OUTPUT: generate a report that lists all the machine names and for each machine, list of the users that are currently logged in. Print to screen...
#     webserver.local:  # name of the machine
#          - kay
#          - Derrin
#          - Taylor
#          - Mark

# PROBLEM STATEMENT:
#   - We need to process a list of event objects using their DATE, TYPE, MACHINE, and USER attributes to generate a report lists are users currently logged in to the machines.
#    "We need to process a list of Event objects using their attributes to generate a report that lists all users currently logged in to the machines."


# PROBLEM RESEARCH ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Consider all the tools that are available to solve the problem
# sorted() returns new list that has been sorted
# sort() modifies the list sorted
# key parameter print(sorted(names, key=len))


# PROBLEM Approach ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. We know that our input will be a list of events and we'll sort them by time.
# 2. Each event in the list will have a machine name, username, and will tell us whether the event was a login or a Logout
# 3. SCRIPT KEEPS TRACK AS USERS LOGIN OR LOGOUT OF THEIR MACHINE.
# 4. We'll use a SET to store the current users, adding users at login and removing them at logout time.
# 5. We'll store this information in a DICTIONARY: name of the machine is the key, current user in the machine as the value.
# 6. Print the report of the info generated as a serate function


# Define helper function used to sort the list
def get_event_date(event):
    return event.date

# Processing function


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines

# Print dictionary using a function


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


# Event class
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
