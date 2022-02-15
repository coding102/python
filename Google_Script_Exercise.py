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
