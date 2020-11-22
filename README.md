# Nitter notify tool

This tools allow to monitor twitter post (via [nitter](https://nitter.net/) rss stream), this program is written in python and use [dunst](https://dunst-project.org/) as notify program.

Nitter allow an endpoints on https://nitter.net/{user}/rss, where user might be a list as: "a,b,c".

## Install instructions:

* Clone git repository

```bash
git clone https://github.com/manslaughter03/nitter-notification
```

* Install python package

```bash
python setup.py install --user
```

* Create your config file

```bash
mkdir ~/.config/nitter
cp example.config.yaml ~/.config/nitter/config.yaml
```

* Run

```bash
python -m nitter
```


## Install instructions as systemd service:

```bash
python setup.py install --user
cp nitter.service ~/.config/systemd/user/
systemctl --user enable nitter.service
systemctl --user start nitter.service
```
