import services.database as db
import models.Cliente as cliente
import models.ECliente as ecliente


def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO crud2 (cliente, numero, status, tipo, categoria, movimentacao) 
    VALUES (?,?,?,?,?,?) """, cliente.cliente, cliente.numero, cliente.status, cliente.tipo, cliente.categoria, cliente.movimentacao).rowcount
    db.cnxn.commit()


def SelecionarTodos():
    db.cursor.execute("SELECT * FROM crud2 ")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

    return costumerList

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM crud2 WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()


#dados = format( cliente.Cliente(cliente,numero,status,cliente.tipo,cliente.categoria,cliente.movimentacao,cliente.id))


def Alterar(ecliente):
    count = db.cursor.execute("""
    UPDATE [dbo].[crud2]
    SET [cliente] = '{}'
    ,[numero] = {}
    ,[status] = '{}'
    ,[tipo] = {}
    ,[categoria] = '{}'
    ,[movimentacao] = '{}'
     WHERE id = {} """,format(f'{ecliente.eid},{ecliente.ecliente},{ecliente.enumero},{ecliente.estatus},{ecliente.estatus},{ecliente.etipo},{ecliente.ecategoria},{ecliente.emovimentacao}')).rowcount
    db.cnxn.commit()


