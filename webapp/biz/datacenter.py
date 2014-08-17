#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log
from entity import resModel

logger = Log().getLog()

class  DataCenterResourceAction(object):

    """获取数据数据中心的交易情绪指标接口"""
    @Router.route(url = r"datacenter/tradeactivity", method = Router._GET|Router._POST)
    def tradeactivity_action(self,req):
        resource_entity = self.tradeactivity_resource()
        return req.ok(resource_entity)

     """数据中心交易情绪查询"""
    def tradeactivity_resource(self):
        session = Session('master')
        logger.info('数据中心交易情绪查询查询！')
        resources = session.select(resModel.TradeActivity)
        return resources













