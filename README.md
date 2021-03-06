# g1 utilidades
 Esse repositório contém o código de uma aplicação que utiliza o Flask e possui ferramentas voltadas para o dia a dia dos repórteres da [editoria de tecnologia e de dados do g1](https://g1.globo.com/tecnologia/). 
 
A **[primeira ferramenta](https://g1utilidades.herokuapp.com/downdetector)** preenche informações inseridas pelo usuário para formar um texto. Ela cria notas rápidas caso alguma grande plataforma da web saia do ar ([exemplo no g1](https://g1.globo.com/tecnologia/noticia/2021/10/18/instagram-apresenta-instabilidade-para-fazer-posts-e-stories-nesta-segunda.ghtml)) – o usuário precisa preencher qual plataforma teria saído do ar, quantas reclamações foram registradas no site [Downdetector](https://downdetector.com.br/) e se o problema ocorre ao redor do mundo ou não. 

Existem 4 versões possíveis de texto: uma com contrações adaptadas para dias de final de semana (neste sábado, neste domingo); uma com contrações para dias de semana (nesta segunda, nesta terça); e outras duas que combinam essas duas condições com a condição de a instabilidade afetar somente o Brasil ou todo o mundo. O dia da semana e o horário são puxados automaticamente pelo programa.

A **[segunda ferramenta](https://g1utilidades.herokuapp.com/compartilhar)** devolve URLs para o compartilhamento no WhatsApp e no Telegram depois de o usuário incluir o link de sua reportagem. O g1 utiliza esses hiperliks em algumas notícias para que as pessoas dividam aquele material com seus contatos.

A **terceira ferramenta** monitora o canal de Jair Bolsonaro diariamente e dispara um e-mail caso um de seus vídeos seja removido.

A **quarta ferramenta** raspa os sites da Câmara dos Deputados e do Senado como cada legislador votou propostas discutidas nas casas e devolve uma tabela que é inserida no sistema da página **[o voto dos legisladores](https://interativos.g1.globo.com/politica/2019/como-votam)**. Para obter essa tabela, é preciso incluir o link com o resultado das votações na página correspondente para os [votos dos deputados](https://g1utilidades.herokuapp.com/votos-camara), dos [senadores em 1º turno](https://g1utilidades.herokuapp.com/votos-senadores-1turno) ou dos [senadores em 2º turno](https://g1utilidades.herokuapp.com/votos-senadores-2turno).
