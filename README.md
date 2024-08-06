# IG11SOUNDSPLEETER

**IG11SOUNDSPLEETER** é uma aplicação web que permite o upload de uma música para separar a voz dos instrumentos. A aplicação usa Flask no backend para processar os arquivos de áudio e JavaScript no frontend para interagir com o usuário.

## Funcionalidades

* Upload de arquivos de áudio.
* Processamento de áudio para separar a voz dos instrumentos.
* Download dos arquivos de áudio separados.
* Alternância de tema entre claro e escuro.
* Suporte para alternância de idioma entre português e inglês.

## Estrutura do Projeto

ig11soundspleeter/
│
├── client/
│   ├── assets/
│   │   ├── day.png
│   │   ├── moon.png
│   │   ├── pt.png
│   │   └── en.png
│   │
│   ├── css/
│   │   ├── style.scss
│   │   ├── style.scss
│   │   └── style.css
│   │
│   ├── js/
│   │   └── index.js
│   │
│   └── index.html
│
├── server/
│   ├── app.py
│   ├── setupLinux.sh
│   ├── setupMac.sh
│   ├── setup.bat
│   └── requirements.txt
├── LICENSE
└── README.md

## Tecnologias Utilizadas

* **Backend** : Flask
* **Frontend** : JavaScript, HTML, CSS
* **Estilização** : SCSS
* **Imagens** : PNG para ícones de tema e idioma

## Estrutura do Projeto

## Instalação

1. Clone o repositório:

`    git clone https://github.com/edvanioFC/ig11SoundSpleeter.git`

    Entre no diretório

    `cd ig11soundspleeter`

2. Crie um ambiente virtual, ative-o e instale as bibliotecas manualmente(ou execute o script apropriado para o teu sistema). Processo manual:

   `  python -m venv env`

   linux/mac

   ` source venv/bin/activate`

   Windows

`venv\Scripts\activate`

    `pip install -r requirements.txt`

## Executando a Aplicação

1. Inicie o servidor Flask:

   `python app.py`
2. Abra seu navegador e acesse `http://127.0.0.1:5009`.

## Uso

1. Faça o upload de um arquivo de áudio.
2. Clique no botão "Processar" para iniciar o processamento do áudio.
3. Após o processamento, os arquivos separados (voz e instrumentos) estarão disponíveis para download.
4. Use os botões de alternância de tema e idioma para personalizar a interface conforme sua preferência.

## Contribuição

1. Fork este repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](). consulte [LICENSE](https://github.com/edvanioFC/ig11SoundSpleeter/blob/main/LICENSE)

## Contato

Para mais informações, entre em contato com [edvanioFC](https://github.com/edvanioFC).
