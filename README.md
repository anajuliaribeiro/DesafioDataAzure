<div id="top"></div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>ÍNDICE</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o Projeto</a>
      <ul>
        <li><a href="#built-with">Linguagens Utilizadas</a></li>
      </ul>
      <ul>
        <li><a href="#built-with">Tecnologias Implantadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Iniciando</a>
      <ul>
        <li><a href="#prerequisites">Pré requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#Preview">Preview</a></li>
    <li><a href="#contact">Equipe </a></li>
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

Bem Vindxs à resolução do Desafio Final Data Azure do treinamento + G1rl P0w3r !

Mas qual era mesmo o desafio ? 
Desenvolver uma aplicação em Python para carga de arquivos em um banco de dados SQL e gerar relatórios estatísticos visando a descoberta de fraudes em cartão de crédito.

Os arquivos finais da resolução são (não vá rodar um teste ein ?! ) :smile: :
* requirements.txt
* Banco_desafio.sql
* migracaoBD_2.py (contido na pasta Scripts_Python)
* funcao_separar_telefone.py (contido na pasta Scripts_Python)
* validcao_TransacoesIN.py (contido na pasta Scripts_Python)
* validcao_TransacoesOUT.py (contido na pasta Scripts_Python)

Agora que você já sabe quais arquivos vamos utilizar, prontos para começar ?

<p align="right">(<a href="#top">back to top</a>)</p>

### Linguagens Utilizadas

* Python
* SQL

### Tecnologias Implantadas

* Azure VM 
* Power BI 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Iniciando
### Pré requisitos
* Python3 e PIP 
* SQL Server 

### Instalação
_Como instalar e rodar esse projeto._

1. Clone este repositorio 
   ```sh
   git clone https://github.com/1-Dev-as-Accenture/DesafioDataAzure
   ```
2. Execute o comando de instalação dos requisitos
_Este arquivo será responsável por instalar os nossos pacotes adicionais do python_
   ```sh
    pip install -r requirements.txt
   ```
3. Execute o arquivo Banco_desafio.sql no seu SGBD
_Este arquivo é responsável por criar a estrutura de banco de dados que precisaremos para instanciar nossos dados_

4. Execute o arquivo migracaoBD_2.py
_Ao executar este arquivo, o prompt de comando solicitará seus dados de acesso (servidor de banco de dados, usuário, se senha) - Sem essas informações não será possível conectar inicialmente no banco_

   ```sh
    python migracaoBD_2.py
   ``` 
5. Execute o arquivo validacao_TransacoesIN.py
   ```sh
    python validacao_TransacoesIN.py
   ``` 
6. Execute o arquivo validacao_TransacoesOUT.py
   ```sh
    python validacao_TransacoesOUT.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Preview
_A dose of what will be seen_



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Equipe 
[![LinkedIn][linkedin-shield]][linkedin-url]

* Ana Julia Ribeiro
* Adriana da Silva Jacinto
* Bianca Alonso
* Inês Lima
* Luana Miranda
* Maria Beatriz Araújo Mota
* Stephany Mendes Oliveira 




<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
