def calculate_score(participants):
    scores = []
    
    for participant in participants:
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append({'name': participant['name'], 'score': score})
    
    scores.sort(key=lambda x: (-x['score'], x['name']))
    
    return scores


participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11},
    {'name': "Spicy Steve", 'chickenwings': 15, 'hamburgers': 10, 'hotdogs': 8},
    {'name': "Sizzling Sarah", 'chickenwings': 10, 'hamburgers': 8, 'hotdogs': 15},
    {'name': "Munching Mike", 'chickenwings': 8, 'hamburgers': 15, 'hotdogs': 10}
]

scoreboard = calculate_score(participants)
print(scoreboard)
