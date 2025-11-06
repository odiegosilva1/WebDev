
# 🚀 API de Produtos

Uma API simples para gerenciamento de produtos desenvolvida em Python com FastAPI e Flask.

## 📋 Sobre o Projeto

Esta API permite operações básicas de CRUD (Create, Read, Update, Delete) para gerenciamento de produtos. O projeto está atualmente em fase de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

- **Python** 3.x
- **FastAPI** - Framework principal para a API
- **Flask** - Framework adicional utilizado no projeto
- **Uvicorn** - Servidor ASGI para execução
- **Pydantic** - Validação de dados

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando a API

### Desenvolvimento com FastAPI:
```bash
uvicorn main:app --reload
```

### Desenvolvimento com Flask:
```bash
python app.py
```

A API estará disponível em: `http://localhost:8000` (FastAPI) ou `http://localhost:5000` (Flask)

## 📚 Endpoints da API

### Produtos
- `GET /products` - Lista todos os produtos
- `GET /products/{id}` - Busca um produto específico
- `POST /products` - Cria um novo produto
- `PUT /products/{id}` - Atualiza um produto
- `DELETE /products/{id}` - Remove um produto

## 🎯 Status do Projeto

⚠️ **EM DESENVOLVIMENTO**

Este projeto está em fase ativa de desenvolvimento. Novas funcionalidades e melhorias estão sendo implementadas.

### Próximas Implementações:
- [ ] Autenticação de usuários
- [ ] Banco de dados permanente
- [ ] Testes automatizados
- [ ] Documentação completa
- [ ] Deploy em produção

## 🤝 Contribuição

Como o projeto está em desenvolvimento, contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📝 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Nota**: Esta é uma versão inicial da API e pode conter bugs. Use em ambiente de desenvolvimento.
