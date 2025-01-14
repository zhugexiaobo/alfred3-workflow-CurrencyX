# -*- coding:utf-8 -*-
import json,sys
from workflow import Workflow3


def main(wf):
    wf.add_item(title="First of all, register a free API ID", subtitle='Each free API id has 1000 requests per month', valid='yes')
    wf.add_item(title="There are 7 formats you can use.", subtitle='For the following example, the base currency is USD.')
    wf.add_item(title='cy', subtitle='Convert 1 USD(the base currency) to other currencies on the panel. ')
    wf.add_item(title='cy 5.5', subtitle='Convert 5.5 USD(the base currency) to other currencies on the panel')
    wf.add_item(title='cy BTC', subtitle='Convert 1 BTC to other currencies on the panel')
    wf.add_item(title='cy 5.5BTC', subtitle='Convert 5.5 BTC to other currencies on the panel')
    wf.add_item(title='cy 5.5 BTC', subtitle='Convert 5.5 USD(the base currency) to BTC')
    wf.add_item(title='cy 5.5 BTC CNY', subtitle='Convert 5.5 BTC to CNY')
    wf.add_item(title='cy BTC CNY', subtitle='Convert 1 BTC to CNY')
    wf.add_item(title='cy-add THB', subtitle='Add THB to the panel')
    wf.add_item(title='cy-del THB', subtitle='Remove THB from the panel')
    wf.add_item(title='cy-base ETH', subtitle='Set ETH as the base currency')
    wf.add_item(title='cy-update', subtitle='Update currencies list from remote')
    wf.add_item(title='cy-help', subtitle='How to use?')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))