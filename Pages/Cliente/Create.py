import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

def Incluircliente():
    st.title("CADASTRAR CLIENTES")
    with st.form(key="Include_cliente"):
        input_cliente = st.text_input(label="Insira o  nome do Cliente:")
        input_numero = st.number_input(label="Insira o numero do container", format="%d", step=1)
        input_status = st.selectbox(label="status", options=['VAZIO', 'CHEIO'])
        input_tipo = st.selectbox(label="TIPO", options=['20', '40'])
        input_categoria = st.selectbox(label="CATEGORIA", options=['IMPORTACAO', 'EXPORTACAO'])
        input_movimentacao = st.selectbox(label="MOVIMENTACAO",options=['EMBARQUE', 'DESCARGA', 'GATE IN', 'GATE OUT', 'REPOSICIONAMENTO', 'PESAGEM', 'SCANNER'])
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_button_submit:
        ClienteController.Incluir(cliente.Cliente(0, input_cliente, input_numero, input_status, input_tipo, input_categoria, input_movimentacao))
        st.success("Cliente Cadastrado!")