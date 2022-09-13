#15913 de 16132 (219)

from criptoexchange.models import TodoCoinApiIO, Cambio
from config import apikey

def test_todocoin():
    todas = TodoCoinApiIO()
    assert isinstance(todas, TodoCoinApiIO)
    todas.trae(apikey)
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 220

def test_cambio_OK():
    btcEur = Cambio("BTC")
    assert btcEur.tasa is None
    assert btcEur.horafecha is None
    btcEur.actualiza(apikey)
    assert btcEur.tasa > 0
    assert isinstance(btcEur.horafecha, str)

def test_cambio_no_OK():
    noOk= Cambio("kktua")
    assert noOk.tasa is None
    assert noOk.horafecha is None
