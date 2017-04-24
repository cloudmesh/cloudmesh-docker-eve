""" run with

python setup.py install; pip install . ; nosetests -v --nocapture tests/test_docker.py
python setup.py install; pip install . ; nosetests -v --nocapture tests/test_docker.py:Test_docker.test_001


"""
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import HEADING
import os


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
    '''
    def test_0001(self):
        HEADING("Install docker on hosts")
        result = os.popen("cd config/ansible && ansible-playbook yaml/docker-chameleon.yml")
        assert "Fail" not in result  # need to make real assertion
    '''
    def test_001(self):
        HEADING("Add docker hosts")
        result = run("cms docker host docker1 docker1:4243")
        assert "Host" in result  # need to make real assertion

    def test_002(self):
        HEADING("Add docker hosts")
        result = run("cms docker host docker2 docker2:4243")
        assert "Host" in result  # need to make real assertion

    def test_003(self):
        HEADING("list docker hosts")
        result = run("cms docker host list")
        assert "Ip" in result  # need to make real assertion

    def test_004(self):
        HEADING("refresh docker images")
        result = run("cms docker image refresh")
        assert "Ip" in result  # need to make real assertion
		
    def test_005(self):
        HEADING("list docker images")
        result = run("cms docker image list")
        assert "Ip" in result  # need to make real assertion

    def test_006(self):
        HEADING("refresh docker images")
        result = run("cms docker container refresh")
        assert "Ip" in result  # need to make real assertion
		
    def test_007(self):
        HEADING("list docker containers")
        result = run("cms docker container list")
        assert "Ip" in result  # need to make real assertion

    def test_008(self):
        HEADING("create docker container")
        result = run("cms docker container create test1 elasticsearch:docker")
        assert "Container" in result  # need to make real assertion

    def test_009(self):
        HEADING("start docker container")
        result = run("cms docker container start test1")
        assert "Container" in result  # need to make real assertion

    def test_010(self):
        HEADING("list docker containers after start")
        result = run("cms docker container list")
        assert "Ip" in result  # need to make real assertion

    def test_011(self):
        HEADING("stop docker container")
        result = run("cms docker container stop test1")
        assert "Container" in result  # need to make real assertion

    def test_012(self):
        HEADING("delete docker container")
        result = run("cms docker container delete test1")
        assert "Container" in result  # need to make real assertion

    def test_013(self):
        HEADING("list docker containers")
        result = run("cms docker container list")
        assert "Ip" in result  # need to make real assertion

    def test_014(self):
        HEADING("refresh docker networks")
        result = run("cms docker network refresh")
        assert "Ip" in result  # need to make real assertion
		
    def test_015(self):
        HEADING("list docker networks")
        result = run("cms docker network list")
        assert "Ip" in result  # need to make real assertion
