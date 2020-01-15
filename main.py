from inputs import ouvir_microfone
from output import output_speech

output_speech("""Para qual apartamento você quer interfonar""")

numero_apartamento = ouvir_microfone()

output_speech("""Você disse: apartamento {0}, confirma?""".format(numero_apartamento))

confirmacao = ouvir_microfone()

if confirmacao == "sim":
    output_speech("Confirmado")
elif confirmacao == "não":
    output_speech("Então, fale novamente.")
else:
    output_speech("Não entendi denovo, desisto.")