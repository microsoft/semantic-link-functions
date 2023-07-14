from sempy.fabric import FabricDataFrame


def test_function_validators():
    df = FabricDataFrame(
        {"contact_email": ["a@b.com", "d.com"],
         "amex": ["378282246310005", "4242424242424242"],
         "iban": ["DE29100500001061045672", "123456"],
         "es_nie": ["X0095892M", "X0095892X"]}
    )

    assert df["contact_email"].validators.is_email().tolist() == [True, False]
    assert df["amex"].validators.card.is_amex().tolist() == [True, False]
    assert df["iban"].validators.is_iban().tolist() == [True, False]
    assert df["es_nie"].validators.i18n.is_es_nie().tolist() == [True, False]

    assert "validators" in dir(df["contact_email"])
