from turing.turing import Turing
from ikearobot.ikea_robot import IkeaRobot
class NluProcessor(object):
    def process(self, request):
        rst=self.ikea_robot.request(request)

        if(rst.strip()==''):
            return self.turing.request(request)
        else:
            return 'result from ikea_robot'

    def __init__(self):
        self.ikea_robot=IkeaRobot()
        self.turing=Turing()