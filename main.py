
from googletrans import Translator
import os

translator = Translator()

directory_in_str = "dirname"

directory = os.fsencode(directory_in_str)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".srt") and not ( (filename.startswith("arabic.")) or (filename.startswith("S01E0"))  ):

        with open(directory_in_str + "/" + filename, "r") as f:
            lines = f.readlines()
            lines[0] ="1\n"
            start_stop = 0 # flag
            for i in range(len(lines)):

                if( start_stop and (lines[i].__len__() != 1) ):
                    #print(str(i)+"#"+lines[i]+"---"+str(lines[i].__len__()))
                    try:
                        lines[i] = str (translator.translate(lines[i], src='en', dest='ar').text) +"\n"
                    except:
                        print(i)

                for j in range(lines[i].__len__()):
                    if (lines[i][j] == ">"):
                        start_stop = 1
                        break

                if (lines[i] == "\n"):
                    start_stop = 0

                print(i)
        with open(directory_in_str + "/" + "arabic."+ filename, "w", encoding='utf-8') as ff:
            for line in lines:
                ff.write(line)
