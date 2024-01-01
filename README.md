## video-compress

### instructions for use
- Copy the `config-dev.json` file to `config.json` and fill in the custom `access_token`;
- After `http-client.env.json` is configured, debug the interface in `test_main.http`, where the value of `access_token` is the same as that in `config.json`;

### running in docker

[click here to see docker instructions](docker/README.md)


### local source code running

- python version
`python3.10.13`

- install dependencies
```shell
pip install -r requirements.txt
```

- run
```shell
uvicorn run main:app --reload --host 0.0.0.0 --port 8000
```


### parameter description

- [parameter description of system configuration](config-dev.json)
```text
{
  "access_token": "",  // custom api request token optional parameter
}
```

### Gradio-UI
[click here for gradio ui readme md](gradio_ui/README.md)
![gradio_ui](/screenshots/gradio-ui.png)


### technical exchange
- [Join Discord >>](https://discord.com/invite/eRuSqve8CE)
- WeChat：`SamgeApp`


### disclaimer
This program is for technical communication only, and all behaviors of users have nothing to do with the author of this project.
