# Plano de Implementacao de Testes FastAPI

## Objetivo

Adicionar uma suite de testes backend com pytest em um diretorio dedicado tests/, cobrindo todas as rotas existentes do FastAPI e documentando/validando os comportamentos atuais (incluindo a validacao de inscricao duplicada e o novo endpoint de remocao de participantes), com todos os casos estruturados no padrao AAA (Arrange-Act-Assert).

## Etapas

1. Preparacao de dependencias e estrutura base
2. Atualizar requirements.txt para incluir pytest.
3. Criar diretorio tests/ e convencao de arquivos por rota.
4. Infra compartilhada de testes
5. Criar tests/conftest.py com fixture de TestClient e isolamento de estado do dicionario activities.
6. Definir convencao AAA para todos os testes (blocos Arrange, Act e Assert).
7. Cobertura completa das rotas
8. Testar GET / com validacao de redirect.
9. Testar GET /activities com validacao de estrutura JSON.
10. Testar POST /activities/{activity_name}/signup para sucesso, atividade inexistente e payload invalido.
11. Testar DELETE /activities/{activity_name}/participants para sucesso, atividade inexistente e participante ausente.
12. Verificacao e estabilidade
13. Executar pytest -v e corrigir falhas de import/estado.
14. Reexecutar pytest para confirmar comportamento deterministico.

## Decisoes

- Escopo incluido: testes backend FastAPI em diretorio separado tests/.
- Escopo incluido: adicao de pytest em requirements.txt.
- Decisao de estilo: todos os testes seguem AAA de forma explicita e consistente.
- Escopo incluido: aprimoramentos no frontend (UI/UX) para exibir e remover participantes.
## Verificacao

1. Instalar dependencias do projeto.
2. Rodar pytest -v na raiz.
3. Rodar novamente pytest -v para validar isolamento de estado.