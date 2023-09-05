import pandas as pd
import inquirer

#select file to work with
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

Tk().withdraw()
filelocation = askopenfilename()# show an "Open" dialog box and return the path to the selected file
print("File selected: " + filelocation)

#Reads selected CSV file
df = pd.read_csv(filelocation)
labels0 = df.columns.tolist()

#Read file for headers, ask for selections
ListSelection = [
    inquirer.Checkbox("HeaderChoices",
                    message="Select Headers to generate a simplified list: ",
                    choices=labels0,
                         ),
        ]
selected_columns = inquirer.prompt(ListSelection)

#selected columns are saved as a dict, useable for limiting columns
print(df.loc[:, df.columns.isin(list(selected_columns['HeaderChoices']))])

#now from these values, filter all data within selected columns based on filter criteria
FilterSelection = [
    inquirer.List("Filter",
                    message="To remove duplicates, select silter criteria to sort by: ",
                    choices=labels0,
                         ),
        ]
Filter = inquirer.prompt(FilterSelection)

df_clean = df.drop_duplicates(subset=[Filter['Filter']])

#now remove all columns EXCEPT for the specified ones
df_filtered = df_clean[selected_columns['HeaderChoices']]

#Define save path to create new CSV or excel file
filesave = asksaveasfilename()
df_filtered.to_csv(filesave)