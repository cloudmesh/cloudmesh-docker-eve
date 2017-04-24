""" run with

python setup.py install; pip install . ; nosetests -v --nocapture tests/test_swarm.py
python setup.py install; pip install . ; nosetests -v --nocapture tests/test_swarm.py:Test_swarm .test_001

nosetests -v --nocapture tests/test_swarm.py

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
class Test_swarm(object):
    """
    cms swarm  service list
    cms swarm  node list
    cms swarm network list    
    """

    def setup(self):
        pass

    """
    def test_001(self):
        HEADING("Install docker on hosts")
        result = os.popen("cd config/ansible && ansible-playbook yaml/docker-chameleon.yml")
        assert "Fail" not in result  # need to make real assertion
    """
    def test_002(self):
        HEADING("Add swarm hosts")
        result = run("cms swarm host docker3 docker3:4243")
        assert "Host" in result  # need to make real assertion

    def test_003(self):
        HEADING("Add swarm hosts")
        result = run("cms swarm host docker4 docker4:4243")
        assert "Host" in result  # need to make real assertion

    def test_004(self):
        HEADING("list swarm hosts")
        result = run("cms swarm host list")
        assert "Ip" in result  # need to make real assertion

    def test_005(self):
        HEADING("create swarm node")
        result = run("cms swarm create")
        assert "Ip" in result  # need to make real assertion

    def test_006(self):
        HEADING("list swarm nodes")
        result = run("cms swarm node list")
        print(result)
        assert "Ip" in result  # need to make real assertion
    '''
    def test_007(self):
        HEADING("list swarm attrbs")
        result = run("cms swarm attrbs")
        assert "Ip" in result  # need to make real assertion
    '''
    def test_008(self):
        HEADING("switch swarm hosts")
        result = run("cms swarm host docker3 docker3:4243")
        assert "Host" in result  # need to make real assertion

    def test_009(self):
        HEADING("Join swarm master as worker")
        result = run("cms swarm join docker4 Worker")
        assert "Node" in result  # need to make real assertion

    def test_010(self):
        HEADING("switch swarm hosts")
        result = run("cms swarm host docker4 docker4:4243")
        assert "Host" in result  # need to make real assertion

    def test_011(self):
        HEADING("Swarm Image refresh")
        result = run("cms swarm image refresh")
        assert "Ip" in result  # need to make real assertion

    def test_012(self):
        HEADING("Swarm Image list")
        result = run("cms swarm image list")
        assert "Ip" in result  # need to make real assertion

    def test_013(self):
        HEADING("Swarm service create")
        result = run("cms swarm service create elasticsearch elasticsearch:swarm")
        assert "Service" in result  # need to make real assertion

    def test_014(self):
        HEADING("Swarm service list")
        result = run("cms swarm service list")
        assert "Ip" in result  # need to make real assertion

    def test_015(self):
        HEADING("Swarm container refresh")
        result = run("cms swarm container refresh")
        assert "Ip" in result  # need to make real assertion

    def test_016(self):
        HEADING("Swarm container list")
        result = run("cms swarm container list")
        assert "Ip" in result  # need to make real assertion

    def test_017(self):
        HEADING("Swarm service refresh")
        result = run("cms swarm host list")
        result = run("cms swarm service refresh")
        assert "Ip" in result  # need to make real assertion

    def test_018(self):
        HEADING("Swarm service delete")
        result = run("cms swarm service delete elasticsearch")
        assert "Service" in result  # need to make real assertion

    def test_019(self):
        HEADING("refresh swarm networks")
        result = run("cms docker network refresh")
        assert "Ip" in result  # need to make real assertion
		
    def test_020(self):
        HEADING("list swarm networks")
        result = run("cms docker network list")
        assert "Ip" in result  # need to make real assertion

    def test_21(self):
        HEADING("swarm leave")
        result = run("cms swarm leave")
        assert "Swarm" in result  # need to make real assertion

    def test_22(self):
        HEADING("swarm leave")
        result = run("cms swarm host docker3 docker3:4243")
        result = run("cms swarm leave")
        assert "Swarm" in result  # need to make real assertion