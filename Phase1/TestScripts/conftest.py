import pytest
from time import sleep
import signal
from subprocess import Popen, PIPE
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append('...')
sys.path.append('../../')
sys.path.append('../../../')
sys.path.append('../../../../')
sys.path.append('C:\\Python38\\Lib\\site-packages')
from API_Source_Code.src.server import app

@pytest.fixture
def url():  # pragma: no cover
	# url_re = re.compile(r' \* Running on ([^ ]*)')
	server = Popen(["python3", "../API_Source_Code/src/server.py"], stderr=PIPE, stdout=PIPE)
	local_url = 'http://127.0.0.1:8000/'
	yield local_url

	# line = server.stderr.readline()
	# local_url = url_re.match(line.decode())

	server.send_signal(signal.SIGINT)
	waited = 0
	while server.poll() is None and waited < 5:
		sleep(0.1)
		waited += 0.1
	if server.poll() is None:
		server.kill()
