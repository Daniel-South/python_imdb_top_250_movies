"""
FILE:		convert_movie_list_to_excel.py
AUTHOR:		Daniel South
DATE:		2024-03-19

DESCRIPTION:	Save a list of the top 250 rated movies from IMDB in an Excel file.

INPUT FILE:	im250.txt

OUTPUT FILE:	Top_250_Films_in_Excel.xlsx

PROGRAM LOG MESSAGES:

*** Reading the Text File of Best Movies from IMDB ***
*** Checking data integrity ***
*** Assembling the information into a Dictionary ***
*** Creating a DataFrame from the Dictionary ***
     IMDB Rank                     Title  Year MPAA Rating Run Time Avg Critic Rating                                           Starring
0            1  The Shawshank Redemption  1994           R   2h 22m               9.3                                        Tim Robbins
1            2             The Godfather  1972           R   2h 55m               9.2                                      Marlon Brando
2            3           The Dark Knight  2008       PG-13   2h 32m               9.0  Morgan Freeman, Gary Oldman, Christian Bale, M...
3            4     The Godfather Part II  1974           R   3h 22m               9.0                                          Al Pacino
4            5              12 Angry Men  1957    Approved   1h 36m               9.0  Henry Fonda, Martin Balsam, Jack Klugman, Lee ...
..         ...                       ...   ...         ...      ...               ...                                                ...
245        246                  The Help  2011       PG-13   2h 26m               8.1  Viola Davis, Bryce Dallas Howard, Octavia Spen...
246        247     It Happened One Night  1934      Passed   1h 45m               8.1                  Clark Gable and Claudette Colbert
247        248                  Drishyam  2015   Not Rated   2h 43m               8.2  Tabu, Ajay Devgn, Shriya Saran, Ishita Dutta, ...
248        249        Dances with Wolves  1990       PG-13    3h 1m               8.0                                      Kevin Costner
249        250                   Aladdin  1992           G   1h 30m               8.0  Robin Williams, Jonathan Freeman, Gilbert Gott...

[250 rows x 7 columns]
*** Write the DataFrame to an Excel file ***
*** The movie data has been exported file Top_250_Films_in_Excel.xlsx ***


"""


import pandas as pd
from pandas import DataFrame

top_250_films_text_file = "im250.txt"
output_excel_file       = "Top_250_Films_in_Excel.xlsx"
elements_expected       = 250


def check_list_len(list_object, list_name):
	list_len = len(list_object)
	if list_len != elements_expected:
		print(f"Warning: {list_name} has {list_len} elements!")



# Initialize lists to capture components of each film in the text file

actor_list   = []
rank_list    = []
title_list   = []
year_list    = []
runtime_list = []
rating_list  = []
acclaim_list = []


print("*** Reading the Text File of Best Movies from IMDB ***")

movie_file = open(top_250_films_text_file, "r")

line_type = "actor"

for in_line in movie_file:
	line = in_line.strip()

	if line == "":
		#print("blank line")
		line_type = "actor"

	elif line_type == "actor":
		position_of_in = line.rfind(" in ")

		if position_of_in > 0:
			film_actors = line[:position_of_in]
		else:
			film_actors = ""

		actor_list.append(film_actors)
		line_type = "title"

	elif line_type == "title":
		first_dot   = line.find(".")
		first_space = line.find(" ") + 1

		film_rank  = int( line[:first_dot] )
		film_title = line[first_space:]
		#print(film_rank + " .... " + film_title)

		rank_list.append(film_rank)
		title_list.append(film_title)
		line_type = "year"

	elif line_type == "year":
		year_list.append( int(line) )
		#print("year", line)
		line_type = "runtime"

	elif line_type == "runtime":
		runtime_list.append(line)
		#print("run time", line)
		line_type = "rating"

	elif line_type == "rating":
		rating_list.append(line)
		line_type = "acclaim"

	elif line_type == "acclaim":
		acclaim_list.append(line)
		line_type = "other"

movie_file.close()



print("*** Checking data integrity ***")

check_list_len(actor_list,   "actor_list")
check_list_len(rank_list,    "rank_list")
check_list_len(title_list,   "title_list")
check_list_len(year_list,    "year_list")
check_list_len(runtime_list, "runtime_list")
check_list_len(rating_list,  "rating_list")
check_list_len(acclaim_list, "acclaim_list")


print("*** Assembling the information into a Dictionary ***")

movie_dict = {  "IMDB Rank"         : rank_list,
		"Title"             : title_list,
		"Year"              : year_list,
		"MPAA Rating"       : rating_list,
		"Run Time"          : runtime_list,
		"Avg Critic Rating" : acclaim_list,
		"Starring"          : actor_list
}


print("*** Creating a DataFrame from the Dictionary ***")

movie_df = DataFrame(movie_dict)

print(movie_df)


print("*** Write the DataFrame to an Excel file ***")

movie_df.to_excel( output_excel_file, sheet_name="Top 250 Movies", index=False )

print(f"*** The movie data has been exported file {output_excel_file} ***")

