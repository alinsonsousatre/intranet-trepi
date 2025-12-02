from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from trepi.intranet import _
from zope import schema
from zope.interface import implementer


class IArea(model.Schema):
    """Definição de uma Área."""

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "telefone",
        ],
    )

    email = Email(
        title=_("Email"),
        required=True,
    )

    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
    )

    model.fieldset(
        "endereco",
        _("Endereço"),
        fields=["endereco", "complemento", "cidade", "estado", "cep"],
    )

    endereco = schema.Text(
        title=_("Endereço"), description=_("Informe o endereço"), required=True
    )

    complemento = schema.Text(title=_("Complemento"), required=False)

    cidade = schema.TextLine(title=_("Cidade"), required=True)

    estado = schema.TextLine(title=_("Estado"), required=True)

    cep = schema.TextLine(title=_("CEP"), required=False)


@implementer(IArea)
class Area(Container):
    """Uma Área no TRE-PI."""
