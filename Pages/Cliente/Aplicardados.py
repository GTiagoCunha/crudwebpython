import streamlit as st
import Controllers.ClienteController as ClienteController
import models.ECliente as ecliente


def Incluirclienteeditado(id):

    st.title("ALTERAR CLIENTE")
    with st.form(key="Alter_cliente"):
        eid = st.write(id)
        input_ecliente = st.text_input(label="Insira o  nome do Cliente:")
        input_enumero = st.number_input(label="Insira o numero do container", format="%d", step=1)
        input_estatus = st.selectbox(label="status", options=['VAZIO', 'CHEIO'])
        input_etipo = st.selectbox(label="TIPO", options=['20', '40'])
        input_ecategoria = st.selectbox(label="CATEGORIA", options=['IMPORTACAO', 'EXPORTACAO'])
        input_emovimentacao = st.selectbox(label="MOVIMENTACAO",options=['EMBARQUE', 'DESCARGA', 'GATE IN', 'GATE OUT', 'REPOSICIONAMENTO', 'PESAGEM', 'SCANNER'])

        input_button_submit = st.form_submit_button("ALTERAR")

    if input_button_submit:
        ClienteController.Alterar(ecliente.ECliente(eid,input_ecliente, input_enumero, input_estatus, input_etipo, input_ecategoria,
        input_emovimentacao))
        st.success("Cliente alterado")







