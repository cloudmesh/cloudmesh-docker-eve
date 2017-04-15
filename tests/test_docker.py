""" run with

python setup.py install; pip install . ; nosetests -v --nocapture tests/docker/test_docker.py
python setup.py install; pip install . ; nosetests -v --nocapture tests/docker/test_docker.py:Test_docker.test_001

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
class Test_docker(object):
    """

    """

    def setup(self):
        pass

    def test_003(self):
        HEADING("list docker images")
        result = run("cms docker image list")
        print(result)
        assert "cms" in result  # need to make real assertion

    def test_004(self):
        HEADING("list docker images")
        result = run("cms docker container list")
        print(result)
        assert "cms" in result  # need to make real assertion

    def test_005(self):
        HEADING("list docker images")
        result = run("cms docker network list")
        print(result)
        assert "cms" in result  # need to make real assertion
