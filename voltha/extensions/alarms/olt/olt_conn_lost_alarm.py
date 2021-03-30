# Copyright 2017-present Adtran, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from voltha.protos.events_pb2 import AlarmEventType, AlarmEventSeverity, AlarmEventCategory
from voltha.extensions.alarms.adapter_alarms import AlarmBase


class OltConnLostAlarm(AlarmBase):
    def __init__(self, alarm_mgr, serial_number):
        super(OltConnLostAlarm, self).__init__(alarm_mgr, object_type='olt connection lost',
                                               alarm='OLT_CONNECTION_LOST',
                                               alarm_category=AlarmEventCategory.OLT,
                                               alarm_type=AlarmEventType.COMMUNICATION,
                                               alarm_severity=AlarmEventSeverity.CRITICAL)
        self._serial_number = serial_number

    def get_context_data(self):
        return {'olt-serial-number': self._serial_number}
