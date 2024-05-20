import configparser
from typing import get_type_hints, Union

from src.errors import AppConfigError


class AppConfig:
    """
    Map environment variables to class fields according to these rules:
      - Field won't be parsed unless it has a type annotation
      - Field will be skipped if not in all caps
      - Class field and environment variable name are the same
    """
    SERVER_PORT: int
    SERVER_HOST: str
    APP_NAME: str
    PARSE_TIMEOUT: int
    DTKLP_BUFFER_SIZE: int
    DTKLP_LIB_PATH: str
    DTKLP_KEY: str
    PARSE_URL: str
    PARSE_MASTER_KEY: str
    PARSE_APP_ID: str

    def _read_cfg(self):
        config = configparser.ConfigParser()
        config.read('cfg.ini')
        return config['SETTINGS']

    def _parse_bool(self, val: Union[str, bool]) -> bool:
        return val if type(val) == bool else val.lower() in ['true', 'yes', '1']
    
    def __init__(self):
        file_cfg = self._read_cfg()
        for field in self.__annotations__:
            if not field.isupper():
                continue
            
            if field not in file_cfg:
                raise AppConfigError('The {} field is required'.format(field))

            try:
                var_type = get_type_hints(AppConfig)[field]
                if var_type == bool:
                    value = self._parse_bool(file_cfg[field])
                else:
                    value = var_type(file_cfg[field])

                self.__setattr__(field, value)
            except ValueError:
                raise AppConfigError('Unable to cast value of "{}" to type "{}" for "{}" field'.format(
                    file_cfg[field],
                    var_type,
                    field
                )
            )

    def __repr__(self):
        return str(self.__dict__)


Config = AppConfig()
