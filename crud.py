import streamlit as st
import Pages.Cliente.Create as pageincluircliente
import Pages.Cliente.List as pagelistcliente

st.sidebar.title("MENU")
Page_cliente = st.sidebar.selectbox("Cliente",['Incluir', 'Consultar'])

if Page_cliente == 'Consultar':
    pagelistcliente.List()

if Page_cliente == 'Incluir':
    pageincluircliente.Incluircliente()







