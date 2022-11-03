from uuid import uuid4

from django.test import TestCase
from model_mommy import mommy

from core.models import Feature, Role, TeamMember, get_file_path
from core.models import Service


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f"{uuid4()}.png"
        return

    def test_get_file_path(self):
        file = get_file_path(None, 'teste.png')
        self.assertTrue(len(file) == len(self.filename))
        return


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service: Service = mommy.make(Service)
        return

    def test_str(self):
        self.assertEqual(str(self.service), self.service.title)


class RoleTestCase(TestCase):

    def setUp(self):
        self.role: Role = mommy.make(Role)
        return

    def test_str(self):
        self.assertEqual(str(self.role), self.role.role_name)


class TeamMemberCase(TestCase):

    def setUp(self):
        self.team_member: TeamMember = mommy.make(TeamMember)
        return

    def test_str(self):
        self.assertEqual(str(self.team_member), f"{self.team_member.name} - {self.team_member.role}")


class FeatureCase(TestCase):

    def setUp(self):
        self.feature: Feature = mommy.make(Feature)
        return

    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.name)
