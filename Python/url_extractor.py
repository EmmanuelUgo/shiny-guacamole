from numpy import extract
import pandas as pd
from dateutil.parser import parse

## 

def is_date(string, fuzzy=False):

    """
    Verifies if a particular string can be a date 
    """
    try:
        parse(string, fuzzy = fuzzy)
        return True
    except ValueError:
        return False



def url_extract():

    """
    This function automatically loads the chat data saved at raw_data/chat_data.txt
    and extracts the urls from the chats then exports it to processed_links/.

    It also keeps record of the latest date so that when ran on a new chat history,
    it automatically filters off old record and saves the new record in this format.
    '{earliest date}to{latest date}.csv'.

    To use this function, make sure the new chat data is renamed to 'chat_data.txt' and
    is saved in the raw_data/ directory.
    """
    
    file = open("raw_data/chat_data.txt", encoding = "utf8")

    last_date = open("raw_data/latest_date.txt", encoding = "utf8")

    print("Reading whatsapp data\n")
    

    chats = file.readlines()
    last_record = last_date.readlines()

    print(f"Last chat was recorded at: {last_record[0]} \n")

    lines = []

    for line in chats:
        line_list = line.replace("\n", "").split(",")
        
        if is_date(line_list[0]):
            lines.append([line_list[0], ("".join(line_list[1:]))])
            
        else:
            lines[-1][-1] = lines[-1][-1] + ' ' + line.replace("\n","")

    tidy_format = pd.DataFrame(lines, columns = ['date','message'])

    print("Extracting date...\n")

    time_msg = tidy_format["message"].str.split("-", n = 1, expand = True)
    tidy_format["time"] = time_msg[0]
    tidy_format["message"] = time_msg[1]

    print("Extracting time...\n")

    user_msg = tidy_format["message"].str.split(":", n = 1, expand = True)
    tidy_format["author"] = user_msg[0]
    tidy_format["message"] = user_msg[1]

    print("Extracting author and message...\n")

    tidy_format['id'] = range(1, 1+len(tidy_format))
    tidy_format['datetime'] = pd.to_datetime(tidy_format.date + tidy_format.time, errors='coerce')

    tidy_format = tidy_format[["id","datetime","author","message"]]

    print("Preparing dataframe...\n")

    if max(tidy_format.datetime) <= pd.to_datetime(last_record[0]):
        
        print("Records are upto date!\nCheck if you updated the chat data at raw_data/chat_data.txt")

    else:

        new_records = tidy_format[tidy_format.datetime > last_record[0]]

        latest_date = max(new_records.datetime)

        print("Updating latest date..\n")
        
        with open('raw_data/latest_date.txt', 'w') as f:
            f.write(str(latest_date))

        pattern = r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"

        print("Extracting links...\n")

        urls_extract = new_records.message.str.extractall(pattern)

        url_id = []

        for i in range(0,len(urls_extract)):
            
            add_list = urls_extract.index[[i]][0][0] + 1
            
            url_id.append(add_list)

        urls_extract['id'] = url_id

        links_tbl = pd.merge(new_records, urls_extract, on = "id", how = "inner")

        links_tbl.columns = ['id', 'datetime', 'author', 'message', 'url']

        print("Links extracted, saving links...\n")

        start = str(min(new_records.datetime)).split(" ")[0]
        
        end = str(max(new_records.datetime)).split(" ")[0]

        links_tbl.to_csv(f"processed_links/{start}to{end}.csv")

        print(f"Saved sucessfully to processed_links/{start}to{end}.csv")


url_extract()
    