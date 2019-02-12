from collections import defaultdict

if __name__ == "__main__":
    team_profile = defaultdict(dict)
    while True:
        line = input().strip()
        if line == '-1':
            break
        team, problem, correct = line.split()
        if correct == 'right':
            if 'right' not in team_profile[problem]:
                team_profile[problem]['right'] = 'right'
                team_profile[problem]['time'] = team
            elif team_profile[problem]['right'] == 'wrong':
                team_profile[problem]['right'] = 'right'
                team_profile[problem]['time'] = team
        else:
            if 'right' in team_profile[problem] and team_profile[problem]['right']=='right':
                continue
            else:
                team_profile[problem]['right'] = 'wrong'
            if 'wrongtime' not in team_profile[problem]:
                team_profile[problem]['wrongtime'] = 1
            else:
                team_profile[problem]['wrongtime'] += 1
    solved,time = 0,0
    #print(team_profile)
    for key in team_profile:
        
        if team_profile[key]['right'] == 'right':
            solved += 1
            time += int(team_profile[key]['time'])
            if 'wrongtime' in team_profile[key]:
                time += 20*int(team_profile[key]['wrongtime'])

    print(solved, time)
        
        
