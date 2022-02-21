# URL Extractor for WhatsApp Chats

This repo contains codes developed in **R** and **Python** for extracting URLs sent in a Whatsapp Chat.

After cloning this repo, make sure to create a new folder called "**data**" to store the exported WhatsApp chat data (**chat_data**) and to also store the time the last chat was sent. (**last_date**). All .**txt** files

![](C:/Users/Admin/AppData/Local/RStudio/tmp/paste-2C5C306A.png)

## Instructions for Python

After creating the data folder, run the url_extractor.py file.

```{python}
python url_extractor.py

```

## Instructions for R

After creating the data folder, open the `learning-targets` project file and run

```{r}
targets::tar_make()

```

Exported URLs are located at the `processed_links` folder for both R and Python.

R Exports

| datetime             | author                      | url                                                                                                                                                          |
|----------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2020-04-12T21:43:32Z | +234 \*\*\* \*\*\* \*\*\*\* | <https://databricks.com/sparkaisummit/north-america-2020>                                                                                                    |
| 2020-04-12T23:31:32Z | +234 \*\*\* \*\*\* \*\*\*\* | <https://info.microsoft.com/CE-AzureINFRA-WBNR-FY20-04Apr-21-MicrosoftAzureVirtualTrainingDayFundamentalsMaster-SRDEM17525_LP01Registration-ForminBody.html> |
| 2020-04-13T15:39:32Z | +234 \*\*\* \*\*\* \*\*\*\* | <https://www.myjobmag.com/jobs/microsoft-nigeria-software-engineering-internship-program?utm_source=email&utm_medium=email&utm_campaign=email>               |

: R Export

Python Exports

+----+-----------------------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id | datetime              | author                      | message                                                                                                                                                                                                        | url                                                                                                                                                          |
+====+=======================+=============================+================================================================================================================================================================================================================+==============================================================================================================================================================+
| 73 | 12/4/2020 10:43:00 PM | +234 \*\*\* \*\*\* \*\*\*\* | Registration is free! This year's summit is virtual. <https://databricks.com/sparkaisummit/north-america-2020>                                                                                                 | <https://databricks.com/sparkaisummit/north-america-2020>                                                                                                    |
+----+-----------------------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 82 | 4/21/2020 1:00:00 PM  | +234 \*\*\* \*\*\* \*\*\*\* | 00 Join this free virtual session. To create your vision for tomorrow, you need to understand what the cloud                                                                                                   | <https://info.microsoft.com/CE-AzureINFRA-WBNR-FY20-04Apr-21-MicrosoftAzureVirtualTrainingDayFundamentalsMaster-SRDEM17525_LP01Registration-ForminBody.html> |
|    |                       |                             |                                                                                                                                                                                                                |                                                                                                                                                              |
|    |                       |                             | ...                                                                                                                                                                                                            |                                                                                                                                                              |
|    |                       |                             |                                                                                                                                                                                                                |                                                                                                                                                              |
|    |                       |                             | computing, networking, storage and security basis <https://info.microsoft.com/CE-AzureINFRA-WBNR-FY20-04Apr-21-MicrosoftAzureVirtualTrainingDayFundamentalsMaster-SRDEM17525_LP01Registration-ForminBody.html> |                                                                                                                                                              |
+----+-----------------------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 85 | 4/13/2020 4:39:00 PM  | +234 \*\*\* \*\*\* \*\*\*\* | <https://www.myjobmag.com/jobs/microsoft-nigeria-software-engineering-internship-program?utm_source=email&utm_medium=email&utm_campaign=email>                                                                 | <https://www.myjobmag.com/jobs/microsoft-nigeria-software-engineering-internship-program?utm_source=email&utm_medium=email&utm_campaign=email>               |
+----+-----------------------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Python Export
