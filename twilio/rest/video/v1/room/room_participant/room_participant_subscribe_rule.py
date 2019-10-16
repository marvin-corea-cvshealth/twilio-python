# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SubscribeRulesList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, room_sid, participant_sid):
        """
        Initialize the SubscribeRulesList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource for the Subscribe Rules
        :param participant_sid: The SID of the Participant resource for the Subscribe Rules

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesList
        """
        super(SubscribeRulesList, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'participant_sid': participant_sid, }
        self._uri = '/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SubscribeRulesInstance

        :returns: Fetched SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def update(self, rules=values.unset):
        """
        Update the SubscribeRulesInstance

        :param dict rules: A JSON-encoded array of subscribe rules

        :returns: Updated SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        """
        data = values.of({'Rules': serialize.object(rules), })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribeRulesList>'


class SubscribeRulesPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SubscribeRulesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param room_sid: The SID of the Room resource for the Subscribe Rules
        :param participant_sid: The SID of the Participant resource for the Subscribe Rules

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesPage
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesPage
        """
        super(SubscribeRulesPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SubscribeRulesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        """
        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribeRulesPage>'


class SubscribeRulesInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, room_sid, participant_sid):
        """
        Initialize the SubscribeRulesInstance

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribe_rule.SubscribeRulesInstance
        """
        super(SubscribeRulesInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'participant_sid': payload.get('participant_sid'),
            'room_sid': payload.get('room_sid'),
            'rules': payload.get('rules'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        # Context
        self._context = None
        self._solution = {'room_sid': room_sid, 'participant_sid': participant_sid, }

    @property
    def participant_sid(self):
        """
        :returns: The SID of the Participant resource for the Subscribe Rules
        :rtype: unicode
        """
        return self._properties['participant_sid']

    @property
    def room_sid(self):
        """
        :returns: The SID of the Room resource for the Subscribe Rules
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def rules(self):
        """
        :returns: A collection of Subscribe Rules that describe how to include or exclude matching tracks
        :rtype: unicode
        """
        return self._properties['rules']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribeRulesInstance>'
