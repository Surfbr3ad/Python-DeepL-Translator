# Python-DeepL-Translator
The program translates csv-files via the DeepL API using python.



This is my first python project as a beginner ;-)

Since I was looking for code to just translate article descriptions etc. through the DeepL API with Python and did not find what I was looking for, I tried it myself.

I know this code is neither perfect nor very pretty, but it´s my first one and it is working fine for me :o)

The program will read a csv-file, create a dictionary for each line using the first value as the key (values will be in a list) and send each dictionary through the DeepL API (except for the key value and the first value of each list, since I did not need them to be translated). Afterwards the program will write the new dictionary row by row in a new csv file including the original header of the table.

The program works like this:

    You have to insert your DeepL API Code first. You get it from the official DeepL website (either free or with the pro version)
    Make sure, that the source file* is edited in line 18
    Make sure, that the source and target language is correct in line 10
    You can change the file name of the output in line 68 where the csv-writer starts

Maybe this code example to connect to the DeepL API with python will help you, too. It saved me a lot of time.

*The source file, in my case, consisted of 7 columns. I did not need the first one again, since it was used as the key for each dictionary, since this value is unique in my case (article SKU) and this is why I start with the 2nd value in line 27 instead of the first one.
