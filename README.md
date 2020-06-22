## Kaiser Engineering Digital Dash GUI

#### Installing:

[![pipeline status](https://gitlab.com/kaiserengineering/DigitalDash_GUI/badges/poetry/pipeline.svg)](https://gitlab.com/kaiserengineering/DigitalDash_GUI/-/commits/master)

##### Install Deps ( >=Python3.7)


```sh
pip3 install -r requirements.txt
```

##### Running the DD:

```sh
 python3 main.py -d --file tests/data/rpm_increasing.csv -c etc/configs/single.json
```

###### Testing:

Auto CI is enabled for the DD but lets be good about running tests before every push!

```bash
    python3 -m pytest tests
```
