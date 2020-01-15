from inputs import ouvir_microfone
from output import output_speech

output_speech("""Iniciando sessão de reconhecimento.
              Diga-me 
              <break time="300ms"/> qual o seu nome.""")

nome_cliente = ouvir_microfone()

output_speech("""Bom dia, 
              <break time="300ms"/> {0}, 
              <break time="300ms"/> como posso te ajudar?""".format(nome_cliente))
