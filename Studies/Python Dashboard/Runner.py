import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "BookHome.py"]
sys.exit(stcli.main())