# DESCRIÇÃO EM LÍNGUA PORTUGUESA
## Descrição do problema
Moçambique, designado como República de Moçambique é um pais localizado no sudoeste do continente africano - áfrica austral, com 11 províncias, cuja capital é a província de Maputo. Faz fronteira com a Tanzânia ao norte; Malawi e Zâmbia a noroeste; Zimbabwe a oeste e Essuatíni e África do Sul a sudoeste.
Como alguns dos países em desenvolvimento Moçambique têm passado por reformas que visam torná-lo um país aberto. Muitas iniciativas locais foram até então feitas no sentido de tornar Moçambique um pais acessível à nível de informação revelante ao público no geral, entretanto muito ainda há por fazer, como qualquer parte do mundo.
No âmbito da pandemia COVID-19 algumas iniciativas foram criadas pelo governo moçambicano tais como o **website COVID-19 Fica Atento** (https://covid19.ins.gov.mz), o **Dashboard da COVID-19** (https://experience.arcgis.com/experience/28d6725c51e545af8583f91c5494c624), o **chatbot WhatsApp** (https://api.whatsapp.com/send?phone=258843318727&text=Olá), a **plataforma de Auto-Avaliação de Risco** (http://riscocovid19.misau.gov.mz).
Estas plataformas são muitas delas modernas e acessíveis para o público no geral, entretanto falta um repositório central no qual a informação (retrospectiva e actual) sobre a actualização diária da COVID-19 será armazenada para acesso ao público e/ou uso em diversas frentes.
Para propôr uma solução que visa resolver o problema de disponibilização da informação da COVID-19 em Moçambique apresento o **Portal da COVID-19 em Moçambique**.

## Proposta de Solução: Portal da COVID-19 em Moçambique (PCM)
O PCM é um portal que dispõe de uma base de dados central que armazena informações acerca dos pacientes da COVID-19 em Moçambique.
Esta plataforma é baseada na web, desenvolvida por um investigador de Tecnologias de Informação e Comunicação (TIC) chamando Júlio Rafael, e faz parte do projecto de final do curso CS50 (https://cs50.harvard.edu/x/2020/) da Universidade de Harvard.
Nesta plataforma é possível registar dados sobre os casos da COVID-19, tais como: Testados, Positivos, Negativos, Óbitos, Recuperados, a respectiva localização, entre outros dados relevantes do(s) paciente(s),

O PCM possui uma interface pública onde qualquer pessoa pode visualizar e ter a oportunidade de visualizar os dados actualizados da COVID-19 e uma parte administrativa na qual é efectuar a gestão (back-office) da plataforma.

## PCM foi criado usando as seguintes tecnologias:
Esta aplicação usa:
- **No  Beck-end:** Python, com o framework Flask;
- **No Front-end:** HTML, CSS, Javascript e estilização com Bootstrap
- **Persistência de dados: ** SQLite

## Créditos para:
- **Imagem de perfil:** @user3802032 (https://www.freepik.com/user3802032)
- **Interface da parte administrativa inspirada em: ** Vali Bootstrap Admin (https://github.com/pratikborsadiya/vali-admin)

## Como correr:
cd project
flask run