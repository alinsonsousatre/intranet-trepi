from plone import api
from plone.dexterity.fti import DexterityFTI
from Products.ZCatalog.CatalogBrains import AbstractCatalogBrain
from trepi.intranet.content.area import Area
from zope.component import createObject


# from AccessControl import Unauthorized
# from .exceptions import AccessControl_Unauthorized
import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def area_payload() -> dict:
    """Return a payload to create a new area."""
    return {
        "type": "Area",
        "id": "ti",
        "title": "Tecnologia da Informação",
        "description": ("Área responsável por TI"),
        "email": "ti@tre-pi.jus.br",
        "telefone": "(61) 3210.1234",
    }


class TestArea:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
            "trepi.intranet.behavior.contato",
            "trepi.intranet.behavior.endereco",
            "volto.blocks",
            "plone.constraintypes",
            "volto.preview_image",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    def test_create(self, area_payload):
        # with pytest.raises(AccessControl_Unauthorized, match=r"Cannot create Area"):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=self.portal, **area_payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Area)

    def test_subscriber_added_with_description_value(self, area_payload):
        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=container,
                **area_payload,
            )
        assert area.exclude_from_nav is False

    def test_subscriber_added_without_description_value(self, area_payload):
        from copy import deepcopy

        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            payload = deepcopy(area_payload)
            payload["description"] = ""
            area = api.content.create(container=container, **payload)
        assert area.exclude_from_nav is True

    def test_subscriber_modified_with_description_value(self, area_payload):
        from copy import deepcopy
        from zope.event import notify
        from zope.lifecycleevent import ObjectModifiedEvent

        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            payload = deepcopy(area_payload)
            payload["description"] = ""
            api.content.create(container=container, **payload)
        with api.env.adopt_roles(["Manager"]):
            brains: list[AbstractCatalogBrain] = api.content.find(portal_type="Area")
            assert len(brains) > 0
            for brain in brains:
                area_modificada: Area = brain.getObject()
                area_modificada.description = "teste com descricao"
                # area_modificada.reindexObject()
                notify(ObjectModifiedEvent(area_modificada))
                assert area_modificada.exclude_from_nav is False
                break

    def test_subscriber_modified_without_description_value(self, area_payload):
        from zope.event import notify
        from zope.lifecycleevent import ObjectModifiedEvent

        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            api.content.create(
                container=container,
                **area_payload,
            )
        with api.env.adopt_roles(["Manager"]):
            brains: list[AbstractCatalogBrain] = api.content.find(portal_type="Area")
            assert len(brains) > 0
            for brain in brains:
                area_modificada: Area = brain.getObject()
                area_modificada.description = ""
                notify(ObjectModifiedEvent(area_modificada))
                assert area_modificada.exclude_from_nav is True
                break
