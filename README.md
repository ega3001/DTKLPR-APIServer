**Service for license plates detection**

- HowTo:
    - How to build
        - Run from project root folder: `sh scripts/install_deps.sh`
    - How to run
        - Before start ensure you have installed specific recognition sdk library!
        - Install supervisor: `sudo apt-get install supervisor`
        - Copy-paste `supervisor.cfg` to `/etc/supervisor/conf.d` folder
        - Run: `supervisorctl reload`
    - How to build and run
        - Run: `sh buildNstart.sh`

After starting app you able to see API docs via: `http://{URL}:{port}/docs#`

**Warning: Application config required!**

- Available parameters explanation:
    - SERVER_PORT - Port for run server
    - SERVER_HOST - Server host address
    - APP_NAME - application name for local storage naming
    - PARSE_TIMEOUT - Local faces DB updating frequency
    - DTKLP_BUFFER_SIZE - buffer size for using in DTKLP wrapper
    - DTKLP_LIB_PATH - path to DTKLP sdk lib
    - DTKLP_KEY - license key for DTKLP engine 
    - PARSE_URL - Parse server url which storing face templates
    - PARSE_MASTER_KEY - Master key for Parse connection
    - PARSE_APP_ID - Parse application id 

- Useful links:
    - https://www.dtksoft.com/lprsdk
    - https://www.dtksoft.com/docs/lprsdk
    - https://docs.parseplatform.org/rest/guide/
