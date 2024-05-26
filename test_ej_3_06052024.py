def iva_total(montoFactura, iva=21):
    return montoFactura + (montoFactura * iva/100)

montoFactura = float(input("Ingrese el monto de la factura para calcular el monto total con iva: "))

print(f'Monto Factura con IVA default: $ {iva_total(montoFactura)}')
print(f'Monto Factura con IVA determinado: $ {iva_total(montoFactura,30)}')