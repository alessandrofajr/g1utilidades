# g1utilidades
 Ferramentas e automações para o g1

# g1 utilidades
 Esse repositório contém o código de uma aplicação que utiliza o Flask e possui ferramentas voltadas para o dia a dia dos repórteres da [editoria de tecnologia do g1](https://g1.globo.com/tecnologia/). 
 
A primeira ferramenta preenche informações inseridas pelo usuário para formar um texto. Ela cria notas rápidas caso alguma grande plataforma da web saia do ar ([exemplo no g1](https://g1.globo.com/tecnologia/noticia/2021/10/18/instagram-apresenta-instabilidade-para-fazer-posts-e-stories-nesta-segunda.ghtml)) – o usuário precisa preencher qual plataforma teria saído do ar, quantas reclamações foram registradas no site [Downdetector](https://downdetector.com.br/) e se o problema ocorre ao redor do mundo ou não. Existem 4 versões possíveis de texto: uma com contrações adaptadas para dias de final de semana (neste sábado, neste domingo); uma com contrações para dias de semana (nesta segunda, nesta terça); e outras duas que combinam essas duas condições com a condição de a instabilidade afetar somente o Brasil ou todo o mundo.

A segunda ferramenta devolve URLs para o compartilhamento no WhatsApp e no Telegram depois de o usuário incluir o link de sua reportagem. O g1 utiliza em algumas notícias esse hiperlink para que as pessoas dividam aquele material com seus contatos.
