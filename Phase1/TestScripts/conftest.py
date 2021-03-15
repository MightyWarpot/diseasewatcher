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
import pytest 
from API_Source_Code.src.server import app  

@pytest.fixture(scope='module')
def url():
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client