import pickle
import os
from collections import defaultdict
#1.News Data dictionary generation
news_dict = defaultdict(list)
for root, subFolders, files in os.walk("news"):
    if len(root.split("/")) != 3: #ignore outer dir in root's perspective
        continue
    date = root.split("/")[-1] #assign date accordingly
    if "bloomberg" in root:
        date = date.replace("-", "")
        for file in files:
            filepath = root + "/" + file
            if 'DS_Store' in filepath:
                continue
            with open(filepath) as news_article:
                for row, col in enumerate(news_article):
                    try:
                        if row == 0: #title
                            title = col[3:-1]
                            news_dict[date].append(title.lower())
                            break
                    except:
                        if row == 1:
                            title = col[:-1]
                            news_dict[date].append(title.lower())
                            break

    if "ReutersNews" in root:
        for file in files:
            filepath = root + "/" + file
            if 'DS_Store' in filepath:
                continue
            with open(filepath) as news_article:
                for row, col in enumerate(news_article):
                    if row == 0: #title
                        title = col[3:-1]
                        news_dict[date].append(title.lower())
                        break

with open('news_dict.pickle', 'wb') as handle:
    pickle.dump(news_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
