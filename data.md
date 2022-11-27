Train Length: 291274 rows
Dev Length: 36409 rows
Test Length: 36410 rows

Structure of Data:

The data has 6 columns: Name, Song Title, Publication Date, Gender, Genre, and Lyrics. All columns contain various pieces of information of the songs, with the lyrics columns containing the full text of lyrics including line breaks.

Here's an example of the data: 
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+
|        | Name                | Song Title            | Publication Date   | Gender   |   Genre | Lyrics                       |
+========+=====================+=======================+====================+==========+=========+==============================+
| 362316 | Yes                 | A Venture             | 2003-01-14         | Male     |     nan | Once a peaceful man laid ... |
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+
| 168512 | King Tuff           | Hit & Run             | 2015-01-27         | Male     |     nan | Speeding down the road to... |
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+
| 104204 | Fairport Convention | Sir Patrick Spens     | 2007-08-13         | Mixed    |     nan | The King sits in Dunfirml... |
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+
| 341212 | Tom Waits           | Coney Island Baby     | 2004-10-01         | Male     |     nan | Every night she comes<br>... |
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+
| 277229 | Spock's Beard       | Get Out While You Can | 2015-08-21         | Male     |     nan | Beware the ghost that flo... |
+--------+---------------------+-----------------------+--------------------+----------+---------+------------------------------+

The data is stored in .csv files for the train, test, and dev data. 
A compressed archive with the train, dev, and test data can be accessed by anyone with a SEAS email here: https://drive.google.com/drive/folders/1LkA2fXmvBEl6Brj5jGjiENrB3xu6vdHE?usp=sharing 

The data was collected from the WASABI Song Corpus (http://wasabi.i3s.unice.fr), a large corpus enriched with metadata extracted from music databases on the Web as part of the Two Million Song Database project. Using the WASABI API (https://wasabi.i3s.unice.fr/apidoc/) we iterated through all artists on the database, checked if the song count for the artist was greater than 5, then extracted the name, title of song, publication date, gender of the artist or of the group, the genre, and the lyrics of the song. We eliminated duplicates, rows with no gender data, and rows with no publication date, leaving us 364k rows. 
