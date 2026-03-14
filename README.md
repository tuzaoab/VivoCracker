# VivoCracker
Programa simples feito em python para craquear senha e usuario do painel da Vivo.



## Guia de Utilização

Este tutorial descreve o procedimento para a interceptação de credenciais do Painel de Administração da Vivo.

### Pré-requisitos
* **Wireshark** (ou ferramenta de análise de pacotes equivalente) instalada.

---

### Procedimento Passo a Passo

#### 1. Seleção da Interface de Rede
Inicie o Wireshark e selecione a interface de rede onde o tráfego do painel administrativo está localizado (exemplo: `eth0`).

![Seleção de Interface](https://github.com/tuzaoab/67-MANGAS/blob/main/WIRESHARK1.png)

#### 2. Aplicação de Filtros de Captura
Para isolar o tráfego relevante e facilitar a análise, utilize o seguinte filtro de exibição:

tcp.port == 80

#### 3. Monitoramento e Captura de Pacotes
Após aplicar o filtro, mantenha o monitoramento ativo. O Wireshark começará a listar apenas o tráfego que trafega pela porta 80.

![Captura em Andamento](https://github.com/tuzaoab/67-MANGAS/blob/main/wireshark3.png)

Aguarde até que uma entrada com o método **POST** e o caminho do script de acesso apareça na lista:
`HTTP 716 POST /cgi-bin/te_acceso_router.cgi HTTP/1.1 (application/x-www-form-urlencoded)`

#### 4. Reconstrução do Fluxo HTTP
Ao identificar o pacote de autenticação mencionado acima, clique com o botão direito sobre ele. Navegue até a opção **Seguir (Follow)** e selecione **Fluxo HTTP (HTTP Stream)**.

![Seguir Fluxo HTTP](https://github.com/tuzaoab/67-MANGAS/blob/main/wireshark4.png)

#### 5. Extração das Credenciais
Uma nova janela será exibida contendo o conteúdo bruto da comunicação. Procure pela linha que contém as variáveis de login:

`curWebPage=%2Findex_cliente.asp&loginUsername=%7E%7Brvq&loginPassword=5b^D#A`

Copie os valores atribuídos aos campos **loginUsername** e **loginPassword** para utilizá-los como entrada no software.

