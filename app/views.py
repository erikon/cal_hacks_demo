from app import app
from flask import jsonify, render_template, request
from . import controllers as controller
import csv
import os.path

@app.route('/')
@app.route('/index')
def index():
    shirt_data = controller.get_shirts()
    # hacker_data = controller.get_hackers()
    return render_template('index.html', shirts=shirt_data)

# Visualize data for Shirt size/gender and schools/type of attendee

@app.route('/hackers', methods=['GET', 'POST'])
def get_hackers():
    school_filter = request.args.get('school')
    hackers = controller.get_hackers()
    # print(school_filter)
    hacker_alt = []
    for hacker in hackers:
        entry = {
            'ticket_type': hacker['ticket_type'],
            'order_ref': hacker['order_ref'],
            'school': hacker['school'],
            'checkin_first': hacker['checkin_first'],
            'checkin_last': hacker['checkin_last'],
        }
        hacker_alt.append(entry)

    if school_filter == None:
        return jsonify({'hackers': hacker_alt})
    else:
        hackers_sub = []
        for hacker in hacker_alt:
            if hacker['school'].lower() == school_filter.lower():
                hackers_sub.append(hacker)
        return jsonify({'hackers': hackers_sub})

@app.route('/shirts', methods=['GET'])
def get_shirts():
    shirt_data = controller.get_shirts()
    return jsonify(shirt_data)
