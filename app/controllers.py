from app import app
import csv
import os.path


def get_hackers():
    hackers = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "attendees.csv")
    with open(file_path) as csvfile:
        attendees = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in attendees:
            if count == 0:
                count += 1
                pass
            else:
                entry = {
                    'ticket_type': row[0],
                    'order_ref': row[1],
                    'shirt_size': row[2],
                    'school': row[3],
                    'checkin_first': row[4],
                    'checkin_last': row[5],
                }
                hackers.append(entry)
    return hackers

def get_shirts():
    hackers = get_hackers()
    malexs, males, malem, malel, malexl = 0, 0, 0, 0, 0
    femalexs, females, femalem, femalel, femalexl = 0, 0, 0, 0, 0
    other = 0
    for entry in hackers:
        if 'Male XS' in entry['shirt_size']:
            malexs += 1
        elif 'Male S' in entry['shirt_size']:
            males += 1
        elif 'Male M' in entry['shirt_size']:
            malem += 1
        elif 'Male L' in entry['shirt_size']:
            malel += 1
        elif 'Male XL' in entry['shirt_size']:
            malexl += 1
        elif 'Female XS' in entry['shirt_size']:
            femalexs += 1
        elif 'Female S' in entry['shirt_size']:
            females += 1
        elif 'Female M' in entry['shirt_size']:
            femalem += 1
        elif 'Female L' in entry['shirt_size']:
            femalel += 1
        elif 'Female XL' in entry['shirt_size']:
            femalexl += 1
        else:
            other += 1
    male_total = malexs + males + malem + malel + malexl
    female_total = femalexs + females + femalem + femalel + femalexl

    shirt_data = {
        'Total': male_total + female_total + other,
        'Male': male_total,
        'MaleXS': malexs,
        'MaleS': males,
        'MaleM': malem,
        'MaleL': malel,
        'MaleXL': malexl,
        'Female': female_total,
        'FemaleXS': femalexs,
        'FemaleS': females,
        'FemaleM': femalem,
        'FemaleL': femalel,
        'FemaleXL': femalexl,
        'None': other
    }
    return shirt_data
