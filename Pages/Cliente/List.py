import streamlit as st
import Controllers.ClienteController as ClienteController
import Pages.Cliente.Aplicardados as ap

def List():
   colms = st.columns((1, 1, 1, 1, 1, 2, 3, 1, 1))
   campos = ['Num','Cliente', 'Numero','Status', 'Tipo', 'Categoria', 'Movimentacao','Excluir', 'Alterar']
   for col, campos_nome in zip(colms, campos):
       col.write(campos_nome)

   for item in ClienteController.SelecionarTodos():
      col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((1, 1, 1, 1, 1, 2, 3, 1, 1))

      col1.write(item.id)
      col2.write(item.cliente)
      col3.write(item.numero)
      col4.write(item.status)
      col5.write(item.tipo)
      col6.write(item.categoria)
      col7.write(item.movimentacao)
      button_space_excluir = col8.empty()
      on_click_exluir = button_space_excluir.button("Excluir",'btnExcluir' + str(item.id))
      button_space_alterar = col9.empty()
      on_click_alterar = button_space_alterar.button("Alterar", "btnAlterar" + str(item.id))

      if on_click_exluir:
        ClienteController.Excluir(item.id)
        button_space_excluir.button("Excluido!", "btnExcluir" + str(item.id))

      if on_click_alterar:
        ap.Incluirclienteeditado(item.id)
        button_space_alterar.button("Alterado!", "btnAlterar" + str(item.id))
