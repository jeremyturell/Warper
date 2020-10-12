# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

def what_is_war():
    print("WAR, short for Wins Above Replacement, measures a player's value in all facets of the game by deciphering how many \nmore wins he's worth than a replacement-level player. \n\nWhile WAR is extremly helpful in determining the best baseball players, it has its \nflaws in that it is a cumulative statistic, and players who have played less games, \nor have had less chances at the plate are less likely to show a high number for WAR \nwhich would fail to account for a players true value when they are on the field.")

import pandas as pd
data = pd.read_csv ('/Users/jeremyturell/Desktop/war_leaders.csv', index_col = "Rank")
print(data) 
leaders = data["Name"] # list of just names in order of WAR

def leaders_war():
    print("Since 2010, 767 Players have had 600 or more Plate Appearences. 600 PAs is considered a full season. \nListed below are the top 5 and bottom 5 players in terms of WAR since 2010. This chart tells us \nwhich players have accumulated the most or least value towards thier teams since 2010. This does not \nweigh players on a per game basis, rahter this is a cumulation of everything they've done.")
    return data

leaders_war()

lower_list = []

for names in leaders:
    lower_names = names.lower()
    lower_list.append(lower_names)
    
    
empty_name = []

def player_input():
        # emptying our empty list above incase were changing names out
        empty_name.clear()  
        name = ""
        
     
    
        while name not in lower_list:
            name = input("Please type the full name of a player who has had 600 or more plate appearences since 2010, \nto find more detailed information regrarding thier WAR and thier WAR on a per season basis \nto see where they stack up").lower()
        
        if name in lower_list:
            # fetching the rest of the players data by index postion
            ranking = lower_list.index(name)
            
        #splitting name into 2 srtings so i can capitalize first letter of first and last
        first, last = name.split() 
        cap_first = first.capitalize()
        cap_last = last.capitalize() 
       
        
        # now adding the capitilized strings to the empty list above
        empty_name.append(cap_first) 
        empty_name.append(cap_last)
      
        
        # now we have a name correctly cased!
        final_name = " ".join(empty_name)
        
        # changing from index position to ranking
        true_rank = ranking + 1 
        
        #printing the inputted players stats
        print(data.loc[ranking + 1])
        return f"{final_name} is ranking number {true_rank} on the overall WAR list out of the 767 qualifiers since 2010"
    




def continued():
    final_name = " ".join(empty_name)
    ans = ""
    while not (ans == "yes" or ans == "no"):
        ans = input(f"Would you like to find a new player, Yes or No? To continue with {final_name} enter No.").lower()
    if ans == "yes":
        print(player_input())
        print(continued())
    else:
        return final_name
    
def explain_war162():
    # calling the name were using
    final_name = " ".join(empty_name)
    
    #putting name to lowercase so that i can grab the index position from my "lower list" way above
    lower_name = final_name.lower()
    
    # now we have index position to use so we can get the players data
    ranking = lower_list.index(lower_name)
    
    games = data.iloc[ranking]["G"]
    
    w_162 = data.iloc[ranking]["WAR_162"]
    
    w_600 = data.iloc[ranking]["WAR_600"]
    #illistation of GP war600 and war162
    print(f"To test how effective {final_name} is when he is on the field for a single game or single plate appearence, we need to analyze \nhow much WAR {final_name} has accumulated, versus how many games he has played. {final_name} has \nappeared in {games} games since 2010. {final_name} averages {w_162} WAR for every 162 Games Played, \nand {w_600} WAR for every 600 Plate Appearences.")
    
def pa_or_g():
    final_name = " ".join(empty_name)
    ans = ""
    
    while not (ans == "g" or ans == "pa"):
        ans = input(f"Lets see where {final_name} stacks up per Game or per PA. To continue, enter either G or PA, to see {final_name}'s ranking in either cateogry compared to his peers.").lower()
    
    # war/162 below
    if ans == "g":
        
        #sorting by war/162
        views162 = data.sort_values(by = "WAR_162", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank162 = views162[views162['Name'] == final_name].index[0] + 1
        
        # final statement
        print("\n\n" + f"{final_name} is ranking number {true_rank162} on the overall WAR per Game leaderboard out of the 767 qualifiers since 2010.")
    else:
        
        #sorting by war/600
        views600 = data.sort_values(by = "WAR_600", ascending = False, ignore_index = True)
        
         # crazy way ridiculous way to get index position on new rankings
        true_rank600 = views600[views600['Name'] == final_name].index[0] + 1
        
        # final statement
        print("\n\n" + f"{final_name} is ranking number {true_rank600} on the overall WAR per Plate Appearence leaderboard out of the 767 qualifiers since 2010.")
    
    
def stat_explanations():
    stat = ""
    
    while not (stat == "g" or stat == "pa"  or stat == "hr" or stat == "avg" or stat == "wrc+" or stat == "war" or stat == "war162" or stat == "war600"):
         stat = input("Please enter the abbreviation for the stat you would like explained").lower()
        
        
    if stat == "g":
        print("\nA total count of the number of games in which a player has appeared.\n")
    elif stat == "pa":
        print("\na player's turn at the plate, the total of which for any player includes all official at-bats plus appearances that resulted in a walk, sacrifice, etc.\n")
        
    elif stat == "hr":
        print("\na fair hit that allows the batter to make a complete circuit of the bases without stopping and score a run\n")
        
    elif stat == "avg":
        print("\nthe average performance of a batter, expressed as a ratio of a batter's safe hits per official times at bat.\n")
    
    elif stat == "wrc+":
        print("\nWeighted Runs Created (wRC) is an improved version of Bill James’ Runs Created (RC) statistic, which attempted to quantify a player’s total offensive value and measure it by runs. wRC+ takes the statistic Runs Created and adjusts that number to account for important external factors -- like ballpark or era. It's adjusted, so a wRC+ of 100 is league average and 150 would be 50 percent above league average.\n")
        
    elif stat == "war":
        print("\nWAR measures a player's value in all facets of the game by deciphering how many more wins he's worth than a replacement-level player at his same position\n")

    elif stat == "war162":
        print("\nWar on a per game basis, multiplied by 162 to be interpreted as an average full season value\n")

    else:
        print("\nWar on a per plate appearence basis, multiplied by 600 to be interpreted as an average full season value\n")
  
        
        
        
def continued2():
    final_name = " ".join(empty_name)
    ans = ""
    
    
    # while loop with all possible acceptable inputs
    while not (ans == "g" or ans == "pa" or ans == "hr" or ans == "avg" or ans == "wrc+" or ans == "war" or ans == "war162" or ans == "war600" or ans == "new" or ans == "exit" or ans == "?"):
        print("G - (Games) \nPA - (Plate Appearences) \nHR - (Home Runs) \nAVG - (Batting Average) \nWRC+ - (Weighted Runs Created Plus) \nWAR - (Wins Above Replacement) \nWAR162 - (Wins Above Replacement per game) \nWAR600 - (Wins Above Replacement per Plate Appearences)")
        ans = input(f"If you would like to see where {final_name} ranks in any of the above statistical categories, please enter the listed abrreviaton for the category here, to see a new player, enter New, to close the program enter exit. If you would like an explanation of any of the above statistcs please enter '?' below)").lower()
        
    # starting with games leaderboard
    if ans == "g":
        
    #sorting by games
        games_leaders = data.sort_values(by = "G", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_games = games_leaders[games_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_games} on the overall Games Played leaderboard out of the 767 qualifiers since 2010."
    
    #plate appearnces
    elif ans == "pa":
        
        #sorting by pa
        pa_leaders = data.sort_values(by = "PA", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_pa = pa_leaders[pa_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_pa} on the overall Plate Appearences leaderboard out of the 767 qualifiers since 2010."
    
    
    #home runs
    elif ans == "hr":
        
        #sorting by hr
        hr_leaders = data.sort_values(by = "HR", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_hr = hr_leaders[hr_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_hr} on the overall Home Runs leaderboard out of the 767 qualifiers since 2010."
    
    
    # batting average
    elif ans == "avg":
        
        #sorting by avg
        avg_leaders = data.sort_values(by = "AVG", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_avg = avg_leaders[avg_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_avg} on the overall Batting Average leaderboard out of the 767 qualifiers since 2010."
    
    # WRC+
    elif ans == "wrc+":
        
        #sorting by wrc+
        wrc_leaders = data.sort_values(by = "wRC+", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_wrc = wrc_leaders[wrc_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_wrc} on the overall Weighted Runs Created Plus leaderboard out of the 767 qualifiers since 2010."
    
    #WAR
    elif ans == "war":
        war_leaders = data.sort_values(by = "WAR", ascending = False, ignore_index = True)
        
        true_rank_war = war_leaders[war_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_war} on the overall Wins Above Replacement leaderboard out of the 767 qualifiers since 2010."
    
    
    #war 162
    elif ans == "war162":
        
        #sorting by war162
        war162_leaders = data.sort_values(by = "WAR_162", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_war162 = war162_leaders[war162_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_war162} on the overall Wins Above Replacement per Game leaderboard out of the 767 qualifiers since 2010."
    
    # war 600    
    elif ans == "war600":
        
        #sorting by pa
        war600_leaders = data.sort_values(by = "WAR_600", ascending = False, ignore_index = True)
        
        # crazy way ridiculous way to get index position on new rankings
        true_rank_war600 = war600_leaders[war600_leaders['Name'] == final_name].index[0] + 1
        
        return f"{final_name} is ranking number {true_rank_war600} on the overall Wins Above Replacement per Plate Appearence leaderboard out of the 767 qualifiers since 2010."
    
    elif ans == "new":
        n_p = new_player()
        print(n_p)
    
    elif ans == "?":
        s_e = stat_explanations()
        print(s_e)
        c22 = continued2()
        print(c22)
    else:
        sys.exit("Program finished")
    
    
    
    
    
def new_player():
    p_i = player_input()
    print(p_i)
    
    print("\n")
    
    c = continued()
    print(c)
    #why does it say none here
    
    print("\n")
    
    e_w162 = explain_war162()
    print(e_w162)
        #why does it say none here
        
    print("\n")
    
    pa_o_g = pa_or_g()
    print(pa_o_g)
    #why does it say none here
    print("\n")
    
    
    c2 = continued2()
    print(c2)
    
    print("\n")
    f = finished()
    print(f)
    
    
def finished():
    final_name = " ".join(empty_name)
    ans = ""
    while not (ans == "new" or ans == "exit" or ans == "different"):
        ans = input(f"If you like to view a different statistic for {final_name}, enter 'different'. If you would like to start over with a new player, enter 'new'.  If you would like to close the program enter 'exit'.").lower()
    
    ### same player different stat
    if ans == "different":
        c2 = continued2()
        print(c2)
        f = finished()
        print(f)
    
    #### new player
    elif ans == "new":
        n_p = new_player()
        print(n_p)
    
    ## close program
    elif ans == "exit":
        sys.exit("Program Finished")
    
        
    
    
    
    
    
def the_finale():
    
    
    # why does it say none here?
    w_w_w = what_is_war()
    print(w_w_w)
    
    print("\n")
    
    l_w = leaders_war()
    print(l_w)
    
    print("\n")
    
    p_i = player_input()
    print(p_i)
    
    print("\n")
    
    c = continued()
    print(c)
    #why does it say none here
    
    print("\n")
    
    e_w162 = explain_war162()
    print(e_w162)
        #why does it say none here
        
    print("\n")
    
    pa_o_g = pa_or_g()
    print(pa_o_g)
    #why does it say none here
    print("\n")
    
    
    c2 = continued2()
    print(c2)
    
    print("\n")
    f = finished()
    print(f)
    
the_finale()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    