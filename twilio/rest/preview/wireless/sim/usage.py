# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UsageList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sim_sid):
        """
        Initialize the UsageList

        :param Version version: Version that contains the resource
        :param sim_sid: The sim_sid

        :returns: twilio.rest.preview.wireless.sim.usage.UsageList
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageList
        """
        super(UsageList, self).__init__(version)

        # Path Solution
        self._solution = {'sim_sid': sim_sid, }

    def get(self):
        """
        Constructs a UsageContext

        :returns: twilio.rest.preview.wireless.sim.usage.UsageContext
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageContext
        """
        return UsageContext(self._version, sim_sid=self._solution['sim_sid'], )

    def __call__(self):
        """
        Constructs a UsageContext

        :returns: twilio.rest.preview.wireless.sim.usage.UsageContext
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageContext
        """
        return UsageContext(self._version, sim_sid=self._solution['sim_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.UsageList>'


class UsagePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the UsagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param sim_sid: The sim_sid

        :returns: twilio.rest.preview.wireless.sim.usage.UsagePage
        :rtype: twilio.rest.preview.wireless.sim.usage.UsagePage
        """
        super(UsagePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.sim.usage.UsageInstance
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageInstance
        """
        return UsageInstance(self._version, payload, sim_sid=self._solution['sim_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.UsagePage>'


class UsageContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sim_sid):
        """
        Initialize the UsageContext

        :param Version version: Version that contains the resource
        :param sim_sid: The sim_sid

        :returns: twilio.rest.preview.wireless.sim.usage.UsageContext
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageContext
        """
        super(UsageContext, self).__init__(version)

        # Path Solution
        self._solution = {'sim_sid': sim_sid, }
        self._uri = '/Sims/{sim_sid}/Usage'.format(**self._solution)

    def fetch(self, end=values.unset, start=values.unset):
        """
        Fetch a UsageInstance

        :param unicode end: The end
        :param unicode start: The start

        :returns: Fetched UsageInstance
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageInstance
        """
        params = values.of({'End': end, 'Start': start, })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UsageInstance(self._version, payload, sim_sid=self._solution['sim_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.UsageContext {}>'.format(context)


class UsageInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sim_sid):
        """
        Initialize the UsageInstance

        :returns: twilio.rest.preview.wireless.sim.usage.UsageInstance
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageInstance
        """
        super(UsageInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sim_sid': payload.get('sim_sid'),
            'sim_unique_name': payload.get('sim_unique_name'),
            'account_sid': payload.get('account_sid'),
            'period': payload.get('period'),
            'commands_usage': payload.get('commands_usage'),
            'commands_costs': payload.get('commands_costs'),
            'data_usage': payload.get('data_usage'),
            'data_costs': payload.get('data_costs'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sim_sid': sim_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UsageContext for this UsageInstance
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageContext
        """
        if self._context is None:
            self._context = UsageContext(self._version, sim_sid=self._solution['sim_sid'], )
        return self._context

    @property
    def sim_sid(self):
        """
        :returns: The sim_sid
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def sim_unique_name(self):
        """
        :returns: The sim_unique_name
        :rtype: unicode
        """
        return self._properties['sim_unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def period(self):
        """
        :returns: The period
        :rtype: dict
        """
        return self._properties['period']

    @property
    def commands_usage(self):
        """
        :returns: The commands_usage
        :rtype: dict
        """
        return self._properties['commands_usage']

    @property
    def commands_costs(self):
        """
        :returns: The commands_costs
        :rtype: dict
        """
        return self._properties['commands_costs']

    @property
    def data_usage(self):
        """
        :returns: The data_usage
        :rtype: dict
        """
        return self._properties['data_usage']

    @property
    def data_costs(self):
        """
        :returns: The data_costs
        :rtype: dict
        """
        return self._properties['data_costs']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, end=values.unset, start=values.unset):
        """
        Fetch a UsageInstance

        :param unicode end: The end
        :param unicode start: The start

        :returns: Fetched UsageInstance
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageInstance
        """
        return self._proxy.fetch(end=end, start=start, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.UsageInstance {}>'.format(context)
