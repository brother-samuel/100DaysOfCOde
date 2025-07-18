import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_list = data['Primary Fur Color']
fur_count = fur_list.value_counts(dropna=False)
# fur_count.to_csv("squirrels.csv")
print(fur_count.to_frame())