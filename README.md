#MovieBuddy
Video Demo: https://youtu.be/_jj9skI_IRM
Description:
Introducing MovieBuddy, a command-line movie companion. The program utilizes the API provided by the Tracking Service simkl.com. MovieBuddy offers a range of features for movie enthusiasts, providing a functional toolset.

Upon initiation, MovieBuddy presents a logo in ASCII art style, using the Figlet library. After that, a menu with functions is presented. The program's functions are diverse, allowing users to find movies by name, explore upcoming releases, or discover a random selection from the top 500 based on chosen genres or at random. User can choose an option inputing 1,2,3 or 0(for exit). Using any other input will result in "Invalid input, choose again" message, prompting to choose again.

Notable feature is the search functionality, allowing users to input a movie name and receive detailed information in an organized table using the tabulate library. This provides essential details such as release year, IMDb rating, and the number of votes. The program allows to choose the movie again within same genre, or go back to choose another one, using loops.

The "Upcoming Releases" feature offers a sneak peek into the latest and near-future movie releases. A table presents an overview of the nearest 50 movies from the "Coming Soon" list on simkl.com, displaying titles and release dates.

MovieBuddy's "Find a Movie" tool locates a movie from the top 500, considering chosen genres or opting for a random selection. Details provided include director information, release year, IMDb rating, and an overview. This tool is designed for times when you're unsure what to watch or prefer a surprise. The program allows to choose the movie again within same genre, or go back to choose another one, using loops.

Behind the scenes, MovieBuddy interacts with the Simkl API, utilizing the "requests" library for up-to-date and accurate information. The program employs a loop for user interaction, prompting input and navigating through functionalities until the user chooses to exit. Additionally, basic error handling is incorporated, including checks for a valid API key and handling connection errors.

Note: The API_KEY function retrieves the variable from the env.py file. While my private API key is included in this private folder, in a public release, it will be replaced with "enter_key_here" to prompt users to input their API key. Failure to do so will trigger an error message instructing users to refer to the README for guidance.
