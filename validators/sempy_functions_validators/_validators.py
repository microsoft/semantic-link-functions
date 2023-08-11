from sempy.fabric import FabricSeries
from sempy.functions import semantic_property


class ValidatorsCard:
    """
    A collection of validators for credit card numbers.

    Parameters
    ----------
    series : FabricSeries
        The series this collection is applied on.
    """

    def __init__(self, series: FabricSeries):
        self.series = series

    def is_amex(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is an American Express card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is an American Express card number.
        """
        from validators.card import amex
        return self.series.apply(lambda v: bool(amex(v))).rename(f"amex({self.series.name})")

    def is_card_number(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a valid card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a valid card number.
        """
        from validators.card import card_number
        return self.series.apply(lambda v: bool(card_number(v))).rename(f"card_number({self.series.name})")

    def is_diners(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a Diners Club card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a Diners Club card number.
        """
        from validators.card import diners
        return self.series.apply(lambda v: bool(diners(v))).rename(f"diners({self.series.name})")

    def is_discover(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a Discover card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a Discover card number.
        """
        from validators.card import discover
        return self.series.apply(lambda v: bool(discover(v))).rename(f"discover({self.series.name})")

    def is_jcb(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a JCB card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a JCB card number.
        """
        from validators.card import jcb
        return self.series.apply(lambda v: bool(jcb(v))).rename(f"jcb({self.series.name})")

    def is_mastercard(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a Mastercard card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a Mastercard card number.
        """
        from validators.card import mastercard
        return self.series.apply(lambda v: bool(mastercard(v))).rename(f"mastercard({self.series.name})")

    def is_unionpay(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a UnionPay card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a UnionPay card number.
        """
        from validators.card import unionpay
        return self.series.apply(lambda v: bool(unionpay(v))).rename(f"unionpay({self.series.name})")

    def is_visa(self) -> FabricSeries:
        """
        Return a boolean series indicating if the credit card number is a Visa card number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the credit card number is a Visa card number.
        """
        from validators.card import visa
        return self.series.apply(lambda v: bool(visa(v))).rename(f"visa({self.series.name})")


class Validatorsi18n:
    """
    A collection of validators for international business numbers.

    Parameters
    ----------
    series : FabricSeries
        The series this collection is applied on.
    """

    def __init__(self, series: FabricSeries):
        self.series = series

    def is_es_cif(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Spanish CIF.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Spanish CIF.
        """
        from validators.i18n.es import es_cif
        return self.series.apply(lambda v: bool(es_cif(v))).rename(f"is_es_cif({self.series.name})")

    def is_es_doi(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Spanish DOI.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Spanish DOI.
        """
        from validators.i18n.es import es_doi
        return self.series.apply(lambda v: bool(es_doi(v))).rename(f"is_es_doi({self.series.name})")

    def is_es_nie(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Spanish NIE.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Spanish NIE.
        """
        from validators.i18n.es import es_nie
        return self.series.apply(lambda v: bool(es_nie(v))).rename(f"is_es_nie({self.series.name})")

    def is_es_nif(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Spanish NIF.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Spanish NIF.
        """
        from validators.i18n.es import es_nif
        return self.series.apply(lambda v: bool(es_nif(v))).rename(f"is_es_nif({self.series.name})")

    def is_fi_business_id(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Finnish business id.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Finnish business id.
        """
        from validators.i18n.fi import fi_business_id
        return self.series.apply(lambda v: bool(fi_business_id(v))).rename(f"is_fi_business_id({self.series.name})")

    def is_fi_ssn(self) -> FabricSeries:
        """
        Return a boolean series indicating if the value is a valid Finnish social security number.

        Returns
        -------
        FabricSeries
            Return a boolean series indicating if the value is a valid Finnish social security number.
        """
        from validators.i18n.fi import fi_ssn
        return self.series.apply(lambda v: bool(fi_ssn(v))).rename(f"is_fi_ssn({self.series.name})")


class Validators:
    """
    A collection of validators for various types of data.

    Parameters
    ----------
    series : FabricSeries
        The series this collection is applied on.
    """

    def __init__(self, series: FabricSeries):
        self.series = series

    def is_email(self) -> FabricSeries:
        """
        Validate if each email is valid or not.

        Returns
        -------
        FabricSeries
            The resulting series containing true/false/none.
        """
        from validators.email import email
        return self.series.apply(lambda v: bool(email(v))).rename(f"is_email({self.series.name})")

    def is_domain(self) -> FabricSeries:
        """
        Validate if each domain is valid or not.

        Returns
        -------
        FabricSeries
            The resulting series containing true/false/none.
        """
        from validators.domain import domain
        return self.series.apply(lambda v: bool(domain(v))).rename(f"is_domain({self.series.name})")

    def is_iban(self) -> FabricSeries:
        """
        Validate if each IBAN is valid or not.

        Returns
        -------
        FabricSeries
            The resulting series containing true/false/none.
        """
        from validators.iban import iban
        return self.series.apply(lambda v: bool(iban(v))).rename(f"is_iban({self.series.name})")

    @property
    def card(self) -> ValidatorsCard:
        """
        Allow validation of creditcard numbers.
        """
        return ValidatorsCard(self.series)

    @property
    def i18n(self) -> Validatorsi18n:
        """
        Allow validation of business IDs.
        """
        return Validatorsi18n(self.series)


@semantic_property("validators", pip_packages=["validators"], series_type=str)
def validators(series: FabricSeries) -> Validators:
    """
    Allow validation of common data types (e.g. email, domain, iban, creditcard numbers) using the `validators <https://python-validators.github.io/validators/>`_ package.

    Note: this property automatically shows up in :class:`sempy.fabric.FabricDataFrame` (e.g. df.validators) if the column requirements are met.

    Parameters
    ----------
    series : FabricSeries
        The series this function is applied on.

    Returns
    -------
    Validators
        The validator object grouping all data type specific functions.
    """
    return Validators(series)
