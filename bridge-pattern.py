from abc import ABC


class PaymentInterface(ABC):
    def make_payment(self, amount):
        raise NotImplementedError()


class EpaycoPaymentProvider(PaymentInterface):
    def make_payment(self, amount):
        print(f"===== Epayco payment with amount: {amount}")


class PayuPaymentProvider(PaymentInterface):
    def make_payment(self, amount):
        print(f">>>>> PayU payyment with amount: {amount}")


def make_payment_util(provider, amount):
    # Esta función, recibe un provider dinámicamente y ejecuta una función, definida por la Interfaz "PaymentInterface".
    provider.make_payment(amount=amount)


if __name__ == "__main__":
    # Definimos los dos proveedores en dos varaibles diferentes
    provider1 = EpaycoPaymentProvider()
    provider2 = PayuPaymentProvider()

    # Llamamos el método make payment util, que recibe "dinámicamente" el proveedor.
    make_payment_util(provider=provider1, amount=300)
    make_payment_util(provider=provider2, amount=300)

    # El patrón de diseño se cumple usando las interfaces, métodos dinámicos y pasando el provider como referencia
    # e instancia diferente a medida que varíe la necesidad.
