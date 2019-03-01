### twitter-excuse

We write random excuse in Twitter

"Excuse" and "Hashtag" is stored locally in file *./excuses/data.py*

To run on your machine, create a *.env* file next to the *main.py* and write in this file:

>TOKEN = "123456789-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
>
>TOKEN_KEY = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
>
>CON_SEC = "aaaaaaaaaaaaaaaaaaaaaaaaa"
>
>CON_SEC_KEY = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"

It is also necessary edit **LOG_FILE_PATH** and setup a file for log in global **/var/log/** folder.

You can independently reconfigure the logging system. It's here is present only for debugging and my interest.

Instead of excuses you can write anything, everything depends on your imagination. The variable **reason** is filled through the library with utilities, where it adds excuses and my hashtags. 

Before running, please, edite a **data.py** for entering your excuses and hashtags.

Based on [https://bash.im/quote/436725](https://bash.im/quote/436725) (on Russian) and [https://github.com/NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts) (on English)
