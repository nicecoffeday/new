import sqlite3
import requests
import json

custom_headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    'Referer': 'https://stats.nba.com/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

conn = sqlite3.connect('/Users/heart/Desktop/project/tmp.db')
cur = conn.cursor()
try:
    gen_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='
    gen_resp = requests.get(gen_url, headers = custom_headers)
    gen_datas = json.loads(gen_resp.text)
    print('insert general table')
    for gen_data in gen_datas['resultSets'][0]['rowSet']:
        cur.execute('insert into nba_general(player_id, player_name, gp, pts, fgm, fga, fg_per) values (?, ?, ?, ?, ?, ?, ?)', 
                   (gen_data[0], gen_data[1], gen_data[5], gen_data[29], gen_data[10], gen_data[11], gen_data[12]))
        
    sho_url = 'https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    sho_resp = requests.get(sho_url, headers=custom_headers)
    sho_datas = json.loads(sho_resp.text)
    print('insert shooting table')
    for sho_data in sho_datas['resultSets']['rowSet']:
        cur.execute('insert into nba_shooting (player_id, res_fgm, res_fga, res_fg_per, pai_fgm, pai_fga, pai_fg_per, mid_fgm, mid_fga, mid_fg_per, left3_fgm, left3_fga, left3_fg_per, right3_fgm, right3_fga, right3_fg_per, pt3_fgm, pt3_fga, pt3_fg_per) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (sho_data[0], sho_data[5], sho_data[6], sho_data[7], sho_data[8], sho_data[9], sho_data[10], sho_data[11], sho_data[12], sho_data[13], sho_data[14], sho_data[15], sho_data[16], sho_data[17], sho_data[18], sho_data[19], sho_data[20], sho_data[21], sho_data[22]))
        
    conn.commit()                
                    
                    
finally:
    conn.close()
    print('finish')



