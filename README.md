### twitter-excuse

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/twitter-excuse/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/twitter-excuse/RELEASE?label=RELEASE)

We write random excuse in Twitter

## Description

`EXCUSES` and `HASHTAGS` is stored locally in file [`twtrexcs/excuses/data.py`](twtrexcs/excuses/data.py)

To run on your machine, place a file `.env` in the root of repo and write in this file:
```bash
export TOKEN="123456789-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TOKEN_KEY="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
export CON_SEC="aaaaaaaaaaaaaaaaaaaaaaaaa"
export CON_SEC_KEY="qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
```

You can independently reconfigure the logging system. It's here is present only for debugging and my interest.

Instead of excuses you can write anything, everything depends on your imagination. The variable `reason` is filled through the library with utilities, where it adds excuses and my hashtags. 

Before running, please, edite a [`twtrexcs/excuses/data.py`](twtrexcs/excuses/data.py) for entering your excuses and hashtags.

## Running
```bash
git clone git@github.com:jtprogru/twitter-excuse.git
cd twitter-excuse
python3 -m venv venv
source venv/bin/activate
make install-deps
make twit
# alternative run
bash run.sh
```

## Author

Michael Savin aka [@jtprogru](https://github.com/jtprogru)

Based on [https://bash.im/quote/436725](https://bash.im/quote/436725) (on Russian) and [https://github.com/NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts) (on English)

## License

[WTFPL](LICENSE.md)
