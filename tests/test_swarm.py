""" run with

python setup.py install; pip install . ; nosetests -v --nocapture tests/swarm/test_swarm .py
python setup.py install; pip install . ; nosetests -v --nocapture tests/swarm /test_swarm .py:Test_swarm .test_001

nosetests -v --nocapture tests/cm_basic/test_var.py

or

nosetests -v tests/cm_basic/test_var.py

"""
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import HEADING


def run(command):
    print(command)
    parameter = command.split(" ")
    shell_command = parameter[0]
    args = parameter[1:]
    result = Shell.execute(shell_command, args)
    print(result)
    return result


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Test_swarm(object):
    """
    cms swarm  service list
    cms swarm  node list
    cms swarm network list    
    """

    def setup(self):
        pass

    def test_003(self):
        HEADING("list swarm  services")
        result = run("cms swarm service list")
        print(result)
        assert "cms" in result  # need to make real assertion

    def test_004(self):
        HEADING("list swarm nodes")
        result = run("cms swarm node list")
        print(result)
        assert "cms" in result  # need to make real assertion

    def test_005(self):
        HEADING("list swarm network")
        result = run("cms swarm network list")
        print(result)
        assert "cms" in result  # need to make real assertion
