import json
import requests
import sys
from tabulate import tabulate
from pyfiglet import Figlet
import sys
import random
import env

api = env.API_KEY

def main_menu():
    print(Figlet().renderText("MovieBuddy")) #logo at start
    print("\nHow can I help you? ")
    print("1. Let me search movies by name")
    print("2. I don't know what to watch! Help me find a random movie from top 500")
    print("3. Upcoming movie releases")
    print("0. Exit\n")
    
    while True:
         choice = input() 
    
         if choice == '1':
            search_movie()
         elif choice == "0":
             sys.exit()
         elif choice == "3":
             popular_releases()  
         elif choice == "2":
             find_a_movie()      
         else:
             print("Invalid input, choose again")
    
def search_movie():
        moviename = input("Enter movie name:\n")
        response = requests.get(f"https://api.simkl.com/search/movie?q={moviename}&page=1&limit=20&extended=full&client_id={api}").json()
        outcome = [] #a blank table containg values from APi in json
    
        for movie in response: 
           title = movie["title"] 
           year = movie["year"] if "year" in movie is not None else "N/A"
           votes = movie["ratings"]["imdb"]["votes"] if "ratings" in movie and "imdb" in movie["ratings"] and movie["ratings"]["imdb"]["votes"] is not None else "N/A"
           IMDBrating = movie["ratings"]["imdb"]["rating"] if "ratings" in movie and "imdb" in movie["ratings"] and movie["ratings"]["imdb"]["rating"] is not None else "N/A"
           outcome.append([title, year, IMDBrating, votes]) #checking if the corresponding values does exist and are not empty, and appending them to table
        if not outcome: #if the table is empty
             print("No movies found.")
        else:     
             print(tabulate(outcome, headers=["Title", "Year", "IMDB rating", "Votes"]))  
    
        while True:
             choice = input("\nEnter 1 to search again, 2 to return to main menu, or 0 to exit\n")
        
             if choice == '2':
                main_menu()
             elif choice == "1":
                search_movie()
             elif choice == "0":
                sys.exit()
        
             else:
                 print("Invalid input, choose again")
                 
def popular_releases():
        response = requests.get("https://data.simkl.in/calendar/movie_release.json").json()
        outcome = [] #a blank table containg values from APi in json
        place = 0 #a way to number the list, as the values in API doesn't contain it - every next movie has following number, capping at 10
        for movie in response:
           if place == 50:
               break
           place += 1
           title = movie["title"]
           release = movie["release_date"]
           IMDBrating = movie["ratings"]["imdb"]["rating"] if "ratings" in movie and "imdb" in movie["ratings"] and movie["ratings"]["imdb"]["rating"] is not None else "N/A"
           outcome.append([place, title, release]) #checking if the corresponding values does exist and are not empty, and appending them to table
        print(tabulate(outcome, headers=["Place", "Title","Relase date",])) 
           
        while True:
              choice = input("\nEnter 1 to return to main menu, or 0 to exit3\n")
         
              if choice == '1':
                 main_menu()
              elif choice == "0":
                 sys.exit()
              else:
                  print("Invalid input, choose again")
    
def find_a_movie():

    movie_types = { #a dictionary containg supported movie genres
       "1": "Action",
       "2": "Adventure",
       "3": "Comedy",
       "4": "Drama",
       "5": "Fantasy",
       "6": "Science-Fiction",
       "7": "Thriller",
       "8": "War",
       "9": "Random"
   }

    print("\nWhat type of movie would you like to watch?")
    for key, value in movie_types.items(): #a way to print genres in numerical way with corresponding values
        print(f"{key}. {value}")

    print("\nEnter 0 to return to main menu")
    movietype = input()
    
    if movietype in movie_types:
        if movietype == "0":   
           main_menu()
        print(f"You chose: {movie_types[movietype]}")
        
    else:
        print("Invalid input, choose again ")
        find_a_movie()
    
    while True:
             #since the random movie finder in API doesn't contain any information 
             #another request has to be made using ID gathered in first request
             response = requests.get(f"https://api.simkl.com/search/random?type=movie&genre={movie_types[movietype]}&rank_limit=500&client_id={api}").json()
             movie_id = response["simkl_id"]   
             secondresponse = requests.get(f"https://api.simkl.com/movies/{movie_id}?extended=full&client_id={api}").json()
             title = secondresponse["title"]
             year = secondresponse["year"]
             IMDBrating = secondresponse["ratings"]["imdb"]["rating"] if "ratings" in secondresponse and secondresponse["ratings"]["imdb"]["rating"] is not None else "N/A"
             overview = secondresponse["overview"] if "overview" in secondresponse is not None else "N/A"
             director = secondresponse["director"] if "director" in secondresponse is not None else "N/A"
             country = secondresponse["country"] if "country" in secondresponse is not None else "N/A"
             genres = secondresponse["genres"] if "genres" in secondresponse is not None else "N/A"  
             
             print(f"\nTitle: {title}")
             print(f"Director: {director}")
             print(f"Year: {year}")
             print(f"IMDB Rating: {IMDBrating}")
             print(f"Country: {country}")
             print(f"Overview: {overview}")
             print("Genres:", ", ".join(genres)) #as the genres from APi is in list form, to have it in pretty format, join function is used
     
             
             
             while True: 
                  choice = input("\nEnter 1 to search again, 2 to return to choose another genre, 3 to return to main menu or 0 to exit\n")
             
                  if choice == '3':
                     main_menu()
                  elif choice == "2":
                     find_a_movie()
                  elif choice == "0":
                     sys.exit()
                  elif choice == "1":
                      break
                  else:
                      print("Invalid input, choose again")
                      continue
    
if __name__ == "__main__":
    main_menu()


    
