# python_imdb_top_250_movies
Save IMDB's list of the 250 movies to an Excel file

Movie website IMDB posts a lists of the Top 250 movies of all time.

If we paste the list directly into Excel, it would take a lot of manual work to format it. For an even larger data set, manual formatting would be all but impossible.

If we save the data to a text file, we can use a Python program to format it and export it as an Excel document.

The text file reveals that the data is organized in a regular pattern. The only variation is that some movies have a list of actors in starring roles, while other movies don't list any actors. Our program can handle this condition as it processes the text file.

--

TEXT FILE CONTENTS:  
Tim Robbins in The Shawshank Redemption (1994)  
1. The Shawshank Redemption  
1994  
2h 22m  
R  
9.3  
 (2.9M)  
  
Marlon Brando in The Godfather (1972)  
2. The Godfather  
1972  
2h 55m  
R  
9.2  
 (2M)  

etc.

--

Our program, convert_movie_list_to_excel.py will read the text file and create an Excel file with the data arranged in columns.

As the progrm works, it creates the following log messages including a head and a tail of the data set that will be written to the Excel file.

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

--

TO EXECUTE THE PROGRAM:

INPUT FILE: im250.txt

OUTPUT FILE: Top_250_Films_in_Excel.xlsx

COMMAND LINE:

python convert_movie_list_to_excel.py

--

AUTHOR:  Daniel South, 19 March 2024

