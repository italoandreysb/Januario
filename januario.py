# -*- coding: utf-8 -*-
import streamlit as st
import google.generativeai as genai
from my_keys import GOOGLE_API_KEY #Esta linha importa minha API KEY, pode comentar ou remover

#O arquivo que contém minha GOOGLE_API_KEY não está no github, para utilizar esta aplicação descomente a linha abaixo e insira sua API_KEY 
#GOOGLE_API_KEY="INSIRA_SUA_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Configurando temperamento
generation_config = {
    "candidate_count": 1,
    "temperature": 1,
}

# Optando por segurança padrão
safety_settings = {
  
}

# Escolhendo a versão do modelo a ser utilizado
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# Habilitando histórico da conversa
chat = model.start_chat(history=[])


# Característica do januario:
chat.send_message("Responda as próximas perguntas naturalmente, conforme eu as envio, \
                   Responda como uma pessoa nascida no nordeste do brasil com o sotaque forte, \
                   Variando o dialeto, sem explicar o motivo ou traduzir textos, \
                   Seu nome é Januario,\
                   Você é da área de Tecnologia, do segmento de infraestrutura de redes\
                   Não utilize negrito para destacar os termos, \
                   Não precisa digitar a palavra resposta")

# loop de conversação:
prompt = ""
print("Pode prosear!(falar) ")
while prompt != "fim":
  prompt = input("Você: \n")
  response = chat.send_message(prompt)
  print("\n","Januário: ","\n", response.text, "\n")
