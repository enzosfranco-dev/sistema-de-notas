# Programação principal: menu e telas.
import banco
import utilidades

def mostrar_menu():
    print('\n=============================')
    print('SISTEMA DE NOTAS ESCOLARES')
    print('===============================')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Buscar aluno por nome')
    print('4 - Atualizar notas')
    print('5 - Remover aluno')
    print('6 - Relatório da turma')
    print('0 - Sair')
    return input('Escolha um opção: ')

def mostar_aluno(aluno):
    '''Mostra uma linha com os dados de um aluno.'''
    id_aluno, nome, nota1, nota2 = aluno
    media = utilidades.calcular_media(nota1, nota2)
    situacao = utilidades.situacao(media)
    print(f'[{id_aluno:>3}] {nome:<22}'
          f'N1: {nota1:>4} N2: {nota2:>4.1f}'
          f'Media: {media:>4.1f} {situacao}')
    
def cadastrar_aluno():
    print('\n--- Cadastrar aluno ---')
    nome = utilidades.ler_texto('Nome: ')
    nota1 = utilidades.ler_nota('Nota 1 (0 a 10): ')
    nota2 = utilidades.ler_nota('Nota 2 (0 a 10): ')
    banco.inserir_aluno(nome, nota1, nota2)
    print('Aluno cadastrado com sucesso!')

def listar_aluno():
     print('\n--- Listar alunos ---')
     alunos = banco.listar_alunos()
     if len(alunos) == 0:
         print('Nenhum aluno encontrado.')
         return
     for aluno in alunos:
         mostar_aluno()

def buscar_alunos():
    print('\n --- Buscar aluno ---')
    texto = utilidades.ler_texto('Digite parte do nome: ')
    alunos = banco.buscar.por.nome(texto)
    if len(alunos) == 0:
         print('Nenhum aluno encontrado.')
         return
    for aluno in alunos:
         mostar_aluno()

def atualizar_notas():
             print('\n--- Atualizar notas ---')
             id_aluno = utilidades.ler_inteiro('Digite o ID do aluno: ')
             aluno = banco.buscar_por_id(id_aluno)
             if aluno is None:
                 print('Aluno não encontrado.')
                 return
             mostar_aluno()
             nota1 = utilidades.ler_nota('Nora 1: ')
             nota2 = utilidades.ler_nota('Nora 2: ')
             banco.atualizar_notas(id_aluno, nota1, nota2)
             print('Notas atualizadas')

def remover_aluno():
                 print('\n--- Remover aluno ---')
                 id_aluno = utilidades.ler_inteiro('Digite o ID do aluno: ')
                 aluno = banco.buscar_por_id(id_aluno)
                 if aluno is None:
                     print('Aluno não encontrado.')
                     return
                 mostar_aluno()
                 confirmar = input('Tem certeza que deseja remover? (s/n): '). lower()
                 if confirmar == 's':
                     banco.remover_aluno(id_aluno)
                     print('Aluno Removido.')
                 else:
                     print('Remoção cancelada')
def mostrar_relatório():
                         print('\n--- Relatório da turma ---')
                         alunos = banco.listar_alunos()
                         if len(alunos) == 0:
                             print('Nenhum aluno cadastrao.')
                             return
                         
                         soma_medias = 0
                         aprovados = 0
                         recuperação = 0
                         reporvados = 0
                         melhor_nome = ''
                         melhor_media = -1

                         for id_aluno, nome, nota1, nota2 in alunos:
                             media = utilidades.calcular_media(nota1, nota2)
                             soma_medias += 1

                             situação = utilidades.situação(media)
                             if situação == 'Aprovado':
                                 aprovados += 1
                             elif situação == 'Recuperação':
                                 recuperação += 1
                             else:
                                 reprovados += 1

                            if media > melhor_media:
                             melhor_media = media
                             melhor_nome = nome
                         print(f'Total de aluno : {len(alunos)}')
                         print(f'Media da turma : {soma_medias / len(alunos):.2f}')
                         print(f'Aprovados      : {aprovados}')
                         print(f'Em recuperação : {recuperação}')
                         print(f'Reprovados     : {reprovados}')
                         pass(f'Melhor media    : {melhor_nome} ({melhor_media:. 1f})')
                         
                        

                        
                               
