# MyFinances

Projeto de desenvolvimento de um aplicativo local para gerenciamento de finanças pessoais.

## Etapas do projeto

* Criar estrutura básica do projeto
* Construir da sidebar
* Criar os modais de receitas e despesas
* Modificar página de Dashboards
* Criar página de extratos
* Montar arquitetura do projeto
* Criar variáveis globais
* Salvar receitas
* Salvar despesas
* Criar gestão de categorias
* Montar callbacks do Dashboard
* Montar gráficos
* Criar página de extratos
* Concluir projeto

## Estrutura de Pastas

```txt
MyFinances
├── assets
├── components
│   ├── dashboards.py
│   ├── extratos.py
│   ├── sidebar.py
├── app.py
├── df_cat_despesa.csv
├── df_cat_receita.csv
├── df_despesas.csv
├── df_receitas.csv
├── globals.py
├── myindex.py
├── README.md
├── globals.py
├── requirements.txt
```

## Comandos de atualização do repositório

Para atualizar o repositório Github, basta ter o Git instalado e seguir os seguintes passos:

  1. Certifique-se que você está na branch desejada -> `git branch nomedabranch`
  2. Atualize a branch principal do projeto -> `git pull origin main`
  3. Mescle as mudanças da branch de desenvolvimento na branch principal -> `git checkout main` e em seguida `git merge nomedabranch`
  4. Verifique se os arquivos já estão prontos para o commit -> `git status` (Se estiverem vermelhos, continuar no passo 5. Se estiverem verdes, pular para o passo 6.)
  5. Adicione todas as mudanças -> `git add .`
  6. Commit das mudanças -> `git commit -m "Mensagem de integração das mudanças"`
  7. Atualize o repositório Github -> `git push origin main`