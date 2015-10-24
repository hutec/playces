from flask import Blueprint, request, redirect, render_template, flash, g, session,\
            url_for

def add_and_get_percentile(id, distance):
    """ records result and returns, how many people did
    equally good or better than the user"""

    # TODO replace session with db
    if 'recorded_results' not in session:
        session['recorded_results'] = {}

    if id not in session['recorded_results']:
        session['recorded_results'][id] = []
        
    prev_results = session['recorded_results'][id]

    worse_players = -1
    n = len(prev_results)
    # these are sorted in descending order
    for count, result in enumerate(prev_results):
        if result < distance:
            worse_players = count
            prev_results.insert(count, distance)
            break
    if worse_players == -1:
        # list was empty or user did better than anybody
        worse_players = n
        prev_results.append(distance)

    if n == 0:
        return 0;
    better_or_equal_players = n - worse_players
    return (better_or_equal_players / float(n)) * 100
