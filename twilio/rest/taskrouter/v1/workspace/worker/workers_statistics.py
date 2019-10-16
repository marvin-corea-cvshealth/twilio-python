# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class WorkersStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace that contains the Worker

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        """
        super(WorkersStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }

    def get(self):
        """
        Constructs a WorkersStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], )

    def __call__(self):
        """
        Constructs a WorkersStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsList>'


class WorkersStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkersStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The SID of the Workspace that contains the Worker

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsPage
        """
        super(WorkersStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkersStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        return WorkersStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsPage>'


class WorkersStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Worker to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        super(WorkersStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers/Statistics'.format(**self._solution)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset,
              task_channel=values.unset):
        """
        Fetch a WorkersStatisticsInstance

        :param unicode minutes: Only calculate statistics since this many minutes in the past
        :param datetime start_date: Only calculate statistics from on or after this date
        :param datetime end_date: Only calculate statistics from this date and time and earlier
        :param unicode task_queue_sid: The SID of the TaskQueue for which to fetch Worker statistics
        :param unicode task_queue_name: The friendly_name of the TaskQueue for which to fetch Worker statistics
        :param unicode friendly_name: Only include Workers with `friendly_name` values that match this parameter
        :param unicode task_channel: Only calculate statistics on this TaskChannel

        :returns: Fetched WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        params = values.of({
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'FriendlyName': friendly_name,
            'TaskChannel': task_channel,
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkersStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsContext {}>'.format(context)


class WorkersStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid):
        """
        Initialize the WorkersStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        super(WorkersStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'realtime': payload.get('realtime'),
            'cumulative': payload.get('cumulative'),
            'account_sid': payload.get('account_sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkersStatisticsContext for this WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        if self._context is None:
            self._context = WorkersStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    @property
    def realtime(self):
        """
        :returns: An object that contains the real-time statistics for the Worker
        :rtype: dict
        """
        return self._properties['realtime']

    @property
    def cumulative(self):
        """
        :returns: An object that contains the cumulative statistics for the Worker
        :rtype: dict
        """
        return self._properties['cumulative']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Worker
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Worker statistics resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset,
              task_channel=values.unset):
        """
        Fetch a WorkersStatisticsInstance

        :param unicode minutes: Only calculate statistics since this many minutes in the past
        :param datetime start_date: Only calculate statistics from on or after this date
        :param datetime end_date: Only calculate statistics from this date and time and earlier
        :param unicode task_queue_sid: The SID of the TaskQueue for which to fetch Worker statistics
        :param unicode task_queue_name: The friendly_name of the TaskQueue for which to fetch Worker statistics
        :param unicode friendly_name: Only include Workers with `friendly_name` values that match this parameter
        :param unicode task_channel: Only calculate statistics on this TaskChannel

        :returns: Fetched WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        return self._proxy.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            friendly_name=friendly_name,
            task_channel=task_channel,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsInstance {}>'.format(context)
