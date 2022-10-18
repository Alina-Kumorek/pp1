amount = 15.84
vat = round(0.23 * amount, 2)

msg = "Amount  :" + str(amount).rjust(6) + " zł\nVAT 23% :" + str(vat).rjust(6) + " zł"

print(msg)