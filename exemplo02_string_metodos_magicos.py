
SuperDev
exemplo02_string_metodos_magicos.py
def remover_espacos_comeco_string():
    texto = "    Minha casa é amarela   "
    # Remover os espaços da esquerda(começo) da string
    texto_removido_espacos_comeco = texto.lstrip()
    print("Texto: '" + texto_removido_espacos_comeco + "'")


def remover_espacos_final_string():
    texto = "   Minha casa é amarela   "
    # Remover os espaços da direita(final) da string
    texto_removido_espacos_final = texto.rstrip()
    print("Texto: '" + texto_removido_espacos_final + "'")


def remover_espacos_comeco_final_string():
    texto = "   Minha casa é amarela   "
    # Remover os espaços da esquerda(comeco) e direita(final) da string
    texto_removido_espacos_comeco_final = texto.strip()
    print("Texto: '" + texto_removido_espacos_comeco_final + "'")


def substituir_parte_string():
    texto = "EU tenho um gato."
    # Substituir o EU para Eu
    texto = texto.replace("EU", "Eu")
    # Substituir o ponto final por nada
    texto = texto.replace(".", "")
    print("Texto: " + texto)


def substituir_valor():
    valor_entrada: str = "R$ 2.395,33" # Alterar a string para '2395.33'
    valor_entrada_sanitizada: str = valor_entrada.replace(".", "") # "R$ 2.395,33" => "R$ 2395,33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.replace(",", ".") # "R$ 2395,33" => "R$ 2395.33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.replace("R$", "") # "R$ 2395.33" => " 2395.33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.strip() # " 2395.33" => "2395.33"

    valor: float = float(valor_entrada_sanitizada)
    print("Valor: ", valor)
# como formatar float no formato real pt-br em python


def verificar_comeca_com_enzo():
    texto = "Enzo da Silva"
    if texto.startswith("Enzo"): # começa com 'Enzo'
        print("Geração Alpha")
    else:
        print("Outra geração")


def verificar_termina_com_silva_ou_souza():
    texto = "Enzo da Souza"
    if texto.endswith("Silva") or texto.endswith("Souza") : # termina 'Silva' ou "Souza"
        print("Brasileiro")
    else:
        print("Estrangeiro")


def verificar_se_contem():
    # produto = "Toddy com pão e linguiça blumenau"
    # produto = "Pão de queijo e Toddy"
    # produto = "Pizza, Toddy e Açaí"
    # produto = "Nescau é top!"
    produto = "Água é top!"
    if "Toddy" in produto:
        print("Viva o toddy")
    elif "Nescau" in produto:
        print("Trocar por Toddy o verdadeiro achocolatado")
    else:
        print("Sei lá")


def verificar_se_nao_contem():
    produto = "Aipim com frango"
    # produto = "Toddy"
    if "Toddy" not in produto: # se 'Toddy' não está no texto
        print("Ta safe pode comer:", produto)
    else:
        print("Ta errado, deixa o toddy de lado")


def transformar_letras_minusculas():
    carro = "Gol Quadrado cINzA "
    # lower é utilizado para converter em letra minúscula
    carro = carro.lower() # "Gol Quadrado cINzA " => "gol quadrado cinza "
    carro = carro.strip()
    if carro == "gol quadrado cinza":
        print("É VW")
    else:
        print("Não é VW")


def transformar_letras_maisculas():
    carro = "Gol Quadrado cINzA "
    # lower é utilizado para converter em letra minúscula
    carro = carro.upper() # "Gol Quadrado cINzA " => "GOL QUADRADO CINZA "
    carro = carro.strip() # "GOL QUADRADO CINZA " => "GOL QUADRADO CINZA"
    if carro == "GOL QUADRADO CINZA":
        print("É VW")
    else:
        print("Não é VW")
    

def converter_data():
    data = "10/07/2025"
    partes = data.split("/") # 0 - "10", 1 - "03", 2 = "2025"
    dia = int(partes[0]) # 10
    mes = int(partes[1]) # 03
    ano = int(partes[2]) # 2025

    if ano == 2025:
        print("Ano do SuperDev")
    else:
        print("Não é o ano")
    
    if mes == 1:
        mes_extenso = "Janeiro"
    elif mes == 2:
        mes_extenso = "Fevereiro"
    elif mes == 3:
        mes_extenso = "Março"
    elif mes == 4:
        mes_extenso = "Abril"
    elif mes == 5:
        mes_extenso = "Maio"
    elif mes == 6:
        mes_extenso = "Junho"
    elif mes == 7:
        mes_extenso = "Julho"
    elif mes == 8:
        mes_extenso = "Agosto"
    elif mes == 9:
        mes_extenso = "Setembro"
    elif mes == 10:
        mes_extenso = "Outubro"
    elif mes == 11:
        mes_extenso = "Novembro"
    elif mes == 12:
        mes_extenso = "Dezembro"
    else:
        mes_extenso = "Mês inválido"


    print("Blumenau, " + str(dia) + " de " + mes_extenso.lower() + " de " + str(ano))
    

def extrair_data_hora():
    texto = "20/02/1996 23:49:13"
    partes_data_hora = texto.split(" ") # duas posições: 0 "20/02/1996" 1 "23:49:13"
    partes_data = partes_data_hora[0].split("/") # 20/02/1996 => 0 20, 1 02, 2 1996
    partes_hora = partes_data_hora[1].split(":") # 23:49:13
    dia = partes_data[0] # 20
    mes = partes_data[1] # 02
    ano = partes_data[2] # 1996

    hora = partes_hora[0]
    minuto = partes_hora[1]
    segundo = partes_hora[2]
    print(dia)
    print(mes)
    print(ano)
    print(hora)
    print(minuto)
    print(segundo)


def extrair_da_string(): # subtring
    #       0123456789
    data = "19/04/2020"
    dia = data[0:2] # pegou posição 0 e 1
    mes = data[3:5] # pegou posição 3 e 4
    ano = data[6:10] # pegou a posição 6, 7, 8 e 9
    print(dia, mes, ano)


def verificar_tamanho_string():
    texto = "    Eu estou com fome   "
    texto = texto.strip()
    quantidade_caracteres = len(texto) # length: comprimento
    print("Texto: '" + texto + "'")
    print("Quantidade de caracteres: ", quantidade_caracteres)


def solicitar_nome():
    nome = input("Digite o nome: ").strip()
    while len(nome) < 3 or len(nome) > 50:
        print("Nome deve conter no mínimo 3 caracteres e no máximo 50")
        nome = input("Digite o nome: ").strip()

# texto.lstrip() remover os espaços do início
# texto.rstrip() remover os espaços do final
# texto.strip() remover os espaços do início e do final
# texto.replace("antigo", "novo") substruir o que está no antigo por o novo
# texto.startswith("texto começo") verificar que começa com  
# texto.endswith("texto final") verificar que termina com
# texto.lower() transformar letra minúscula
# texto.upper() transformar letra maiúscula
# len(texto) obter a quantidade de caracteres

if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_nome()
exemplo-requisicoes.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/80793a8067.js" defer crossorigin="anonymous"></script>
</head>

<body>
    <header class="bg-dark p-2">
        <a href="exemplo-requisicoes.html" class="btn btn-outline-info"><i class="fas fa-home"></i> Home</a>
    </header>

    <div class="text-end mt-3 me-3">
        <button class="btn btn-primary" id="consultar-empresas">
            <i class="fas fa-spinner"></i> Consultar Empresa
        </button>
        <a href="cadastro.html" class="btn btn-primary"><i class="fas fa-plus"></i> Cadastrar Empresa</a>
    </div>

    <div class="p-3">
        <table class="table table-bordered table-hover" id="tabela-empresas">
            <thead class="table-success">
                <tr>
                    <th>Código</th>
                    <th>Nome</th>
                    <th>CNPJ</th>
                    <th>Ação</th>
                </tr>
            </thead>
            <tbody>
                
            </tbody>
        </table>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
    <script src="scripts/requisicoes/exemplo-apagar.js"></script>
    <script src="scripts/requisicoes/exemplo-listar-todos.js"></script>
</body>

</html>
exemplo-cadastrar.js
let urlAPI = "https://public.franciscosensaulas.com"
const campoCnpj = document.getElementById('campoCNPJ');
const mascara = {
    mask: "00.000.000/0000-00"
};
const mask = IMask(campoCnpj, mascara);


let botaoSalvar = document.getElementById("btn-salvar");
botaoSalvar.addEventListener('click', salvar);


async function salvar(e) {
    e.preventDefault(); // form não deve ser enviado, interrompe o envio do formulário 
    let campoNome = document.getElementById("campoNome");
    let nome = campoNome.value
    if (nome.length < 3) {
        alert("Nome deve conter no mínimo 3 caracteres");
        return; // Faz com que o código abaixo não seja executado, ou seja, encerrando a execução dessa função
    }

    if (nome.length > 20) {
        alert("Nome deve conter no máximo 20 caracteres");
        return;
    }

    let cnpj = campoCnpj.value;

    const dados = {
        nome: nome,
        cnpj: cnpj
    }
    let url = `${urlAPI}/api/v1/empresa`;
    const resposta = await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(dados)
    });

    if(resposta.ok == false){
        alert("Não foi possível cadastrar")
    }else{
        location.href = '/exemplo-requisicoes.html';
    }
} 
exemplo-listar-todos.js
let tabelaEmpresas = document.getElementById("tabela-empresas");
let botaoConsultarEmpresas = document.getElementById("consultar-empresas");

let urlAPI = "https://public.franciscosensaulas.com"

function atribuirCliqueBotoesApagar() {
    // pegar a lista de elementos que contém a class="botao-apagar"
    let botoesApagar = document.getElementsByClassName("botao-apagar");
    // foreach percorre cada um dos elementos da lista
    Array.from(botoesApagar).forEach((botao) => {
        // cada um dos botões atribuiremos o evento de click que executará a função apagar
        botao.addEventListener('click', apagar);
    });
}

// Função responsável por questionar o usuário se o mesmo deseja realmente apagar aquele registro
async function apagar() {
    Swal.fire({
        title: "Deseja apagar o cadastro da empresa 'Weg'?",
        text: "Você não poderá reverter isso!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sim apagar!",
        cancelButtonText: "Não",
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            apagarEmpresa();
        }
    });
}

async function apagarEmpresa() {
    let id = 54;
    let url = `${urlAPI}/api/v1/empresa/${id}`
    console.log(url);
    
    const resposta = await fetch(url, {method: "DELETE"});
    if(resposta.ok == false){
        alert("Não foi possível apagar");
        return;
    }

    Swal.fire({
        title: "Apagado!",
        text: "Empresa removida com sucesso!",
        icon: "success"
    });
    consultarEmpresas();
}

// Função responsável por fazer o request(requisição) para carregar os dados da empresa
async function consultarEmpresas() {
    // debugger;
    // let url = urlAPI + "/api/v1/empresa"
    let url = `${urlAPI}/api/v1/empresa`
    // fetch vai realizar a requisição, na variável resposta teremos os dados do response como: status, response em si(dados que o back-end retornou)  
    const resposta = await fetch(url);
    // Verificar se a requisição falhou por algum motivo
    if (resposta.ok == false) {
        alert("Não foi possível carregar os dados")
    }

    // Obter o response da requisição, que neste cenário será uma lista de objetos
    const empresas = await resposta.json();

    let tbody = tabelaEmpresas.querySelector("tbody");
    tbody.innerHTML = "";

    empresas.forEach(empresa => {
        const colunas = `
        <td>${empresa.id}</td>
        <td>${empresa.nome}</td>
        <td>${empresa.cnpj}</td>
        <td>
        <a href="editar.html" class="btn btn-warning"><i class="fas fa-pencil"></i> Editar</a>
        <button class="btn btn-danger botao-apagar"><i class="fas fa-trash"></i> Apagar</button>
        </td>`
        const linha = document.createElement("tr");
        linha.innerHTML = colunas;

        tbody.appendChild(linha);

        console.log(empresa);    
    });

    atribuirCliqueBotoesApagar();

}

botaoConsultarEmpresas.addEventListener("click", consultarEmpresas);
Batatinha

**Batatinha quando nasce**  
É para a lua que se vai  
Batatinha quando nasce  
É para a lua que se vai  
Batatinha quando nasce  
É para a lua que se vai  
E o moço que vai à luta  
Também tem que saber aonde vai

E a batatinha  
Vai também aonde vai  
E a batatinha  
Vai também aonde vai  
E a batatinha  
Vai também aonde vai  
E o moço que vai à luta  
Também tem que saber aonde vai
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="scripts/requisicoes/exemplo-listar-todos.js"></script>
    <script src="scripts/requisicoes/exemplo-cadastrar.js"></script>
    <script src="scripts/requisicoes/exemplo-editar.js"></script>
    <script src="scripts/requisicoes/exemplo-apagar.js"></script>
</body>
</html>
const cars = [
            {
                model: "Volkswagen Gol",
                year: 2022,
                price: 75000,
                mileage: 15000,
                fuel: "Flex",
                brand: "volkswagen",
                image: "https://picsum.photos/300/200?car=1"
            },
            {
                model: "Fiat Argo",
                year: 2020,
                price: 68000,
                mileage: 25000,
                fuel: "Gasolina",
                brand: "fiat",
                image: "https://picsum.photos/300/200?car=2"
            },
            {
                model: "Ford Ka",
                year: 2019,
                price: 45000,
                mileage: 40000,
                fuel: "Flex",
                brand: "ford",
                image: "https://picsum.photos/300/200?car=3"
            },
            {
                model: "Chevrolet Onix",
                year: 2021,
                price: 82000,
                mileage: 18000,
                fuel: "Flex",
                brand: "chevrolet",
                image: "https://picsum.photos/300/200?car=4"
            },
            {
                model: "Volkswagen T-Cross",
                year: 2023,
                price: 135000,
                mileage: 5000,
                fuel: "Gasolina",
                brand: "volkswagen",
                image: "https://picsum.photos/300/200?car=5"
            },
            {
                model: "Fiat Toro",
                year: 2022,
                price: 145000,
                mileage: 12000,
                fuel: "Diesel",
                brand: "fiat",
                image: "https://picsum.photos/300/200?car=6"
            },
            {
                model: "Ford Ranger",
                year: 2020,
                price: 185000,
                mileage: 35000,
                fuel: "Diesel",
                brand: "ford",
                image: "https://picsum.photos/300/200?car=7"
            },
            {
                model: "Chevrolet Cruze",
                year: 2021,
                price: 110000,
                mileage: 22000,
                fuel: "Flex",
                brand: "chevrolet",
                image: "https://picsum.photos/300/200?car=8"
            },
            {
                model: "Volkswagen Polo",
                year: 2019,
                price: 65000,
                mileage: 45000,
                fuel: "Flex",
                brand: "volkswagen",
                image: "https://picsum.photos/300/200?car=9"
            },
            {
                model: "Fiat Mobi",
                year: 2023,
                price: 55000,
                mileage: 8000,
                fuel: "Gasolina",
                brand: "fiat",
                image: "https://picsum.photos/300/200?car=10"
            },
            {
                model: "Ford EcoSport",
                year: 2018,
                price: 70000,
                mileage: 60000,
                fuel: "Flex",
                brand: "ford",
                image: "https://picsum.photos/300/200?car=11"
            },
            {
                model: "Chevrolet Tracker",
                year: 2022,
                price: 125000,
                mileage: 15000,
                fuel: "Flex",
                brand: "chevrolet",
                image: "https://picsum.photos/300/200?car=12"
            },
            {
                model: "Volkswagen Virtus",
                year: 2021,
                price: 95000,
                mileage: 25000,
                fuel: "Gasolina",
                brand: "volkswagen",
                image: "https://picsum.photos/300/200?car=13"
            },
            {
                model: "Fiat Cronos",
                year: 2020,
                price: 72000,
                mileage: 30000,
                fuel: "Flex",
                brand: "fiat",
                image: "https://picsum.photos/300/200?car=14"
            },
            {
                model: "Ford Mustang",
                year: 2022,
                price: 350000,
                mileage: 8000,
                fuel: "Gasolina",
                brand: "ford",
                image: "https://picsum.photos/300/200?car=15"
            },
            {
                model: "Chevrolet S10",
                year: 2021,
                price: 220000,
                mileage: 28000,
                fuel: "Diesel",
                brand: "chevrolet",
                image: "https://picsum.photos/300/200?car=16"
            },
            {
                model: "Volkswagen Nivus",
                year: 2023,
                price: 140000,
                mileage: 3000,
                fuel: "Flex",
                brand: "volkswagen",
                image: "https://picsum.photos/300/200?car=17"
            },
            {
                model: "Fiat Ducato",
                year: 2019,
                price: 165000,
                mileage: 55000,
                fuel: "Diesel",
                brand: "fiat",
                image: "https://picsum.photos/300/200?car=18"
            },
            {
                model: "Ford Fusion",
                year: 2020,
                price: 115000,
                mileage: 32000,
                fuel: "Flex",
                brand: "ford",
                image: "https://picsum.photos/300/200?car=19"
            },
            {
                model: "Chevrolet Montana",
                year: 2022,
                price: 98000,
                mileage: 12000,
                fuel: "Flex",
                brand: "chevrolet",
                image: "https://picsum.photos/300/200?car=20"
            }
        ];
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/index.css">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/nav.css">
    <link rel="stylesheet" href="css/footer.css">
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>MyCar</h1>
            <p>Encontre o seu carro ideal</p>
        </div>
    </header>

    <nav>
        <div class="container">
            <div class="hamburguer"></div>
            <ul class="nav-links">
                <li><a href="comprar.html"></a>Comprar</li>
                <li><a href="vender.html"></a>Vender</li>
                <li><a href="financiamento.html"></a>Financiamento</li>
                <li><a href="#contato"></a>Contato</li>
            </ul>
        </div>
    </nav>

    <script src="https://kit.fontawesome.com/80793a8067.js" crossorigin="anonymous"></script>
    <script src="js/index.js"></script>
</body>
</html>
css/clip-path.css
main{
    max-width: 800px;
    margin: auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

img{
    width: 100%;
    transition: clip-path 1s ease-in-out;
}

img.polygon{
    /* pontos: canto superior esquerdo, superior direito, inferior direito, inferior esquerdo */


    /* cada ponto é composto por x(horizontal) e y(vertical) */
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
img.polygon:hover{
    /* 
        Ao passar o mouse transforma em um losango
        pontos:: topo central, centro direito, centro inferior e centro esquerdo
     */
    clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
}

img.circle{
    /* 
        20% de raio
        50% posição horizontal do centro do círculo
        50% posição vertical do centro do círculo
     */
     clip-path: circle(20% at 50% 50%);
}
img.circle:hover{
    /* 
        50% de raio
        50% posição horizontal do centro do círculo
        50% posição vertical do centro do círculo
     */
     clip-path: circle(50% at 50% 50%);
}
clip-path.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/clip-path.css">
</head>
<body>
    <main>
        <h1>O que é Clip-path?</h1>
        <p>O clip-path é uma propriedade que permite criar formas complexas cortando elementos de acordo com um caminho específico. É util para criar layouts e efeitos visuais interessantes.</p>

        <h2>Como funciona o cli-path</h2>
        <p>O <code>clip-path</code> define uma área visível de um elemento, escondendo o que está fora dessa área. Existe várias formas de usar o <code>clip-path</code> como:</p>
        <ul>
            <li>
                <code>polygon()</code>: Define uma forma usando uma lista de coordenadas que formam um polígono.
                <img src="https://www.sabornamesa.com.br/media/k2/items/cache/bf1e20a4462b71e3cc4cece2a8c96ac8_XL.jpg" alt="" class="polygon">
            </li>
            <li>
                <code>circle()</code>: Define uma forma circular.
                <img src="https://conteudo.imguol.com.br/2014/07/07/pizza-brasileira-1404756799998_1920x1080.jpg" alt="" class="circle">
            </li>
            <li>
                <code>ellipse()</code>: Define uma forma elíptica.
                <img src="https://img.freepik.com/fotos-premium/um-cachorro-quente-com-um-cachorro-quente-em-um-fundo-branco_899870-9156.jpg" alt="" class="ellipse">
            </li>
            <li>
                <code>inset()</code>: Define um retângulo interno com um margem opcional.
                <img src="https://sabores-new.s3.amazonaws.com/public/2024/11/Lasanha_tradicional.jpg" alt="" class="inset">
            </li>
        </ul>
    </main>
</body>
</html>
transform-skew.css
.box {
    transition: transform 0.3s ease;
}

.skew-x {
    background-color: #3498db;
}

.skew-x:hover {
    transform: skewX(20deg);
}

.skew-y {
    background-color: #e73c3c;
}

.skew-y:hover {
    transform: skewY(20deg);
}

.skew-x-y {
    background-color: #2ecc71;
}

.skew-x-y:hover {
    transform: skew(20deg, 10deg);
}
flex-align-content.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/flex-shrink.css">
</head>
<body>
    <h1>Exemplo de flex-shrink</h1>
    <p>
        <span class="negrito">Como funciona?</span> Quando a soma dos tamanhos iniciais (flex-basis) excede o espaço disponível no container, os itens são "comprimidos" de acordo com o valor de <code>flex-shrink</code>. Um item com <code>flex-shrink: 2</code> vai encolher o dobro em relação a um item com <code>flex-shrink: 1</code>. Já um item com <code>flex-shrink: 0</code> não encolhe.
    </p>

    <main>
        <div class="item item-1">Item 1 (shrink: 1)</div>
        <div class="item item-2">Item 2 (shrink: 0)</div>
        <div class="item item-3">Item 3 (shrink: 2)</div>
    </main>
</body>
</html>
main {
    display: flex;
    border: 2px solid #333;
    padding: 10px;
    margin: 20px;
    height: 150px;
    width: 600px;
}

.item {
    background-color: #4CAF50;
    color: #fff;
    padding: 20px;
    margin: 5px;
    text-align: center;
    font-size: 1rem;
    flex-basis: 250px;
    /* Tamanho inicial de cada item */
}

@media (max-width: 680px){
    main{
        width: 400px;
    }

    .item{
        flex-basis: 150px;
    }
}

@media (max-width: 400px) {
    main{
        width: 200px;
        gap: 8px;
    }

    .item{
        flex-basis: 50px;
        padding: 5px;
        margin: 0px;
    }
}



/* Valores distintos de flex-shrink */
.item-1 {
    flex-shrink: 1;
}

.item-2 {
    flex-shrink: 0;
}

.item-3 {
    flex-shrink: 2;
}
flex-align-items.css
 /* Estilos gerais para cada contêiner */
 .container {
     display: flex;
     /* Ativa o Flexbox */
     border: 2px solid #333;
     /* Borda para visualização */
     padding: 10px;
     /* Espaço interno */
     margin: 20px 0;
     /* Espaçamento entre seções */
     height: 200px;
     /* Altura fixa para melhor visualização vertical */
     /* Por padrão, flex-direction: row, logo o eixo transversal é vertical */
 }

 /* Itens internos */
 .item {
     background-color: #4CAF50;
     color: #fff;
     padding: 20px;
     margin: 5px;
     text-align: center;
     font-size: 1rem;
 }

 /* Exemplos de align-items */
 .flex-start {
     align-items: flex-start;
 }

 .flex-end {
     align-items: flex-end;
 }

 .center {
     align-items: center;
 }

 .baseline {
     align-items: baseline;
 }

 .stretch {
     align-items: stretch;
 }

 /* Diferentes tamanhos de fonte para demonstrar 'baseline' */
 .item:nth-child(1) {
     font-size: 1.2rem;
 }

 .item:nth-child(2) {
     font-size: 1rem;
 }

 .item:nth-child(3) {
     font-size: 1.4rem;
 }
flex-align-items.html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Exemplos de align-items</title>
  
  <link rel="stylesheet" href="flex-align-items.css">
</head>
<body>

  <h1>Exemplos de align-items</h1>
  <p>
    <span class="negrito">O que é align-items?</span><br>
    É a propriedade que determina como os itens em um contêiner flex são alinhados ao longo do eixo transversal. Se o contêiner estiver em orientação <code>row</code>, esse alinhamento acontece verticalmente.
  </p>

  <!-- 1. flex-start -->
  <section>
    <h2>align-items: flex-start</h2>
    <p>
      <span class="negrito">Descrição:</span> Alinha os itens ao início do contêiner
      (parte superior, no caso de um eixo horizontal principal).
    </p>
    <div class="container flex-start">
      <div class="item">Item 1</div>
      <div class="item">Item 2</div>
      <div class="item">Item 3</div>
    </div>
  </section>

  <!-- 2. flex-end -->
  <section>
    <h2>align-items: flex-end</h2>
    <p>
      <span class="negrito">Descrição:</span> Alinha os itens ao final do contêiner
      (parte inferior, no caso de um eixo horizontal principal).
    </p>
    <div class="container flex-end">
      <div class="item">Item 1</div>
      <div class="item">Item 2</div>
      <div class="item">Item 3</div>
    </div>
  </section>

  <!-- 3. center -->
  <section>
    <h2>align-items: center</h2>
    <p>
      <span class="negrito">Descrição:</span> Alinha os itens ao centro do eixo vertical.
    </p>
    <div class="container center">
      <div class="item">Item 1</div>
      <div class="item">Item 2</div>
      <div class="item">Item 3</div>
    </div>
  </section>

  <!-- 4. baseline -->
  <section>
    <h2>align-items: baseline</h2>
    <p>
      <span class="negrito">Descrição:</span> Alinha os itens pela linha de base do texto (útil quando os itens têm tamanhos de fonte diferentes).
    </p>
    <div class="container baseline">
      <div class="item">Item 1<br>(Fonte 1.2rem)</div>
      <div class="item">Item 2<br>(Fonte 1rem)</div>
      <div class="item">Item 3<br>(Fonte 1.4rem)</div>
    </div>
  </section>

  <!-- 5. stretch -->
  <section>
    <h2>align-items: stretch</h2>
    <p>
      <span class="negrito">Descrição:</span> Os itens se esticam para preencher todo o espaço disponível no eixo transversal (desde que nenhum valor fixo de altura seja definido para o item).
    </p>
    <div class="container stretch">
      <div class="item">Item 1</div>
      <div class="item">Item 2</div>
      <div class="item">Item 3</div>
    </div>
  </section>

</body>
</html>
flex-direction.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="flex-direction.css">
</head>
<body>
    <h1>Exemplos de flex-direction</h1>
    <section>
        <h2>flex-direction: none</h2>
        <p>
            <span class="negrito">Descrição:</span> Os itens são organizados horizontalmente, do lado esquerdo para o direito.
        </p>
        <div class="container row">
            <div class="item">Item 1</div>
            <div class="item">Item 2</div>
            <div class="item">Item 3</div>
        </div>

    </section>
</body>
</html>
css/login.css
:root {
    --bg-color: #f0f2f5;
    --container-bg: #fff;
    --text-color: #333;
    --primary-color: #1a73e8;
    --input-bg: #fff;
    --input-border: #dadce0;
    --placeholder-color: #666;
    --shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    --secondary-text: #5f6368;
}

[data-theme="dark"] {
    --bg-color: #121212;
    --container-bg: #1e1e1e;
    --text-color: #fff;
    --primary-color: #64B5F6;
    --input-bg: #2d2d2d;
    --input-border: #333;
    --placeholder-color: #888;
    --shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    --secondary-text: #b0b0b0;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    transition: background 0.3s ease, color 0.3 ease;
}

body {
    background: var(--bg-color);
    display: flex;
    justify-content: center;
    /* */
    align-items: center;
    /* */
    min-height: 100vh;
    color: var(--text-color);
}

main {
    background-color: var(--container-bg);
    padding: 2rem;
    border-radius: 8px;
    box-shadow: var(--shadow);
    width: 100%;
    max-width: 400px;
    border: 1px solid var(--input-border);
}

.login-header {
    text-align: center;
    margin-bottom: 2rem;
}

.login-header h1 {
    color: var(--primary-color);
    margin-bottom: 0.5rem;
}

.login-header p {
    color: var(--secondary-text);
}

.form-group {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--secondary-text);
    font-weight: 500;
}

input {
    width: 100%;
}
footer/sem-semantico.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="header">
        <h1>Bem vindo ao sistema da ProWay</h1>
    </div>

    <div class="container">
        <h2>Nossos serviços</h2>
        <p>Oferecemos uma variedade de cursos para atender a sua necessidade.</p>
    </div>

    <div class="footer">
        <p>&copy; 2025 ProWay. Todos os direitos reservados.</p>
        <a href="mailto:proway@proway.com.br">proway@proway.com.br</a>
        <a href="(47) 98801-6336">(47) 98801-6336</a>
        <a href="https://br.linkedin.com/company/prowayinfo" target="_blank">Linkedin</a>
        <a href="https://github.com/franciscosensaulas" target="_blank">GitHub</a>
    </div>
</body>
</html>
aside/sem-semantico.css
body{
    display: flex;
    flex-direction: row;
}

.sidebar-esquerda{
    width: 250px;
    height: 100vh;
    background-color: #333;
    color: #000;
    padding: 15px;
}

.sidebar-esquerda ul {
    list-style: none;
    padding: 0;
}

.sidebar-esquerda ul li{
    padding: 10px;
    cursor: pointer;
}
.sidebar-esquerda ul li:hover{
    background-color: #575757;
}

.hidden-items{
    display: none;
}

.toggle-button{
    background-color: #444;
    border: none;
    color: #FFF;
    padding: 10px;
    width: 100%;
    text-align: left;
    cursor: pointer;
}

.toggle-button:hover{
    background-color: #575757;
}
aside/sem-semantico.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="sem-semantico.css">
    <link rel="stylesheet" href="../css-reset.css">
</head>
<body>
    <div class="sidebar-esquerda">
        <!-- ul>li*3>(button.toggle-button)+(ul.hidden-items>li*3) -->
        <ul>
            <li>
                <button class="toggle-button" data-submenu="submenu-calcados">Calçados</button>
                <ul class="hidden-items" id="submenu-calcados">
                    <li>Tênis</li>
                    <li>Sandália</li>
                    <li>Crocs</li>
                </ul>
            </li>
            <li>
                <button class="toggle-button" data-submenu="submenu-camisetas">Camisetas</button>
                <ul class="hidden-items" id="submenu-camisetas">
                    <li>Adidas</li>
                    <li>Nike</li>
                    <li>Tommy</li>
                </ul>
            </li>
            <li>
                <button class="toggle-button" data-submenu="submenu-giftcards">GitCards</button>
                <ul class="hidden-items" id="submenu-giftcards">
                    <li>Netflix</li>
                    <li>Pokemon</li>
                    <li>Valorant</li>
                </ul>
            </li>
        </ul>
    </div>
    <script src="sem-semantico.js"></script>
</body>
</html>
logo
https://ibb.co/PYRGVnc

https://github.com/franciscosensaulas/proway-super-dev-2024

<a href="/login">
    <i class="fa-solid fa-user"></i> Login
</a>


<script src="https://kit.fontawesome.com/128a5c22cc.js" crossorigin="anonymous"></script>
sem-semantico.css
.botao-pesquisa,
.botao-entrar {
    font-family: "Nosifer", serif;
    font-weight: 400;
    font-style: normal;
    background-color: transparent;
    border: none;
    color: #FFF;
}

.botao-entrar:hover,
.botao-pesquisa:hover{
    cursor: pointer;
}

.botao-entrar:hover{
    color: #ec332e;
    border: 1px solid #ec332e;
    border-radius: 5px;
}

body {
    margin: 0;
    padding: 0;
}

div.header {
    background-color: #000;
    height: 50px;
}

div.header div.botoes-direita {
    display: inline;
    float: right;
    padding: 10px;
}

div.header img.logo {
    height: 50px;
}
sem-semantico.html
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Header - Sem Semântico</title>
    <link rel="stylesheet" href="sem-semantico.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nosifer&display=swap" rel="stylesheet">
</head>

<body>
    <div class="header">
        <a href="sem-semantico">
            <img src="logo.png" alt="Logo da nike em cor preta" class="logo">
        </a>
        <div class="botoes-direita">
            <button class="botao-pesquisa">Pesquisar</button>
            <button class="botao-entrar">Entrar</button>
        </div>
    </div>
</body>

</html>
tags-depreciadas.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <center>Meu texto <font face="Arial" size="4" color="blue">centralizado</font></center>
    <div class="sidebar">
        <marquee width="200">Essa é uma mensagem extremamente importante! Cuidado não utilize marquee</marquee>
    </div>
    <div>
        <p>
            <b>Importante:</b> Isso é negrito utilizando a tag <code>&lt;b&gt;</code>
        </p>
        <p>
            <u>Nota:</u> Isso é underline utilizando a tag <code>&lt;u&gt;</code>
        </p>
    </div>
    <table border="1">
        <thead>
            <tr bgcolor="blue">
                <th width="100">Código</th>
                <th width="300">Nome</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Uva</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Abacaxi</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
index.css
.centralizado {
    /* como centralizar texto */
    text-align: center;
}

.titulo-realce {
    /* como alterar fonte do texto css */
    font-family: Arial, Helvetica, sans-serif;
    /* como alterar tamanho fonte do texto css */
    font-size: 24px;
    font-size: 1.5rem; /* 1 rem equivale a 16px, ou seja, 1.5 rem dá 24px */
    /* como alterar a cor do texto css */
    color: #0000ff;
}

.negrito {
    /* definir o texto como negrito css */
    font-weight: bold;
}

.underline {
    /* definir o texto como underline css */
    text-decoration: underline;
}

.marquee-container{
    overflow: hidden;
    width: 300px;
    white-space: nowrap;
    box-sizing: border-box;
}

.marquee{
    animation: scrolling-text 10s linear infinite;
    display: inline-block;
    width: inherit;
}

@keyframes scrolling-text {
    0%{
        text-indent: 100%;
    }

    100%{
        text-indent: -100%;
    }
}

table,
tr,
td,
th{
    /* definir a borda da tabela css */
    border-style: solid;
    border-width: 1px;
    border-color: #0000ff;
    /* versão simplificada procurar por 'border short hand' */
    border: 1px solid #000;
}

table thead tr{
    /* definir o fundo como azul css */
    background-color: #0000ff;
}

.coluna-codigo{
    /* definir o tamanho da coluna da tabela css */
    width: 100px;
}

.coluna-nome{
    width: 200px;
}
index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- carregar arquivo de css no html -->
    <link rel="stylesheet" href="index.css">
</head>

<body>
    <h1 class="centralizado">Meu texto <span class="titulo-realce">centralizado</span></h1>
    <div class="marquee-container">
        <span class="marquee">Essa uma mensagem extremamente importante! Cuidado não utilize a tag marquee</span>
    </div>
    <div>
        <p>
            <span class="negrito">Importante:</span> Isso é negrito utilizando o css <code>font-weight: bold</code>
        </p>
        <p>
            <span class="underline">Nota: </span> Isso é underline utilizando o css
            <code>text-decoration: underline</code>
        </p>
    </div>
    <table>
        <thead>
            <tr>
                <th>Código</th>
                <th>Nome</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Uva</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Abacaxi</td>
            </tr>
        </tbody>
    </table>
</body>

</html>
exemplo07-criar-elementos.js
let botaoCriarCampos = document.querySelector("#criar-campo");

// Escopo dele é global
let numeroDaSorte = 0;

function criarCampo() {
  // Criar uma tag label
  let labelNumero = document.createElement("label");
  labelNumero.innerText = "Digite um número";
  // Link da label com o input
  labelNumero.htmlFor = "numero-sorte";

  // Criando uma tag input
  let campoNumero = document.createElement("input");
  // Definir que será um campo de número
  campoNumero.type = "number";
  campoNumero.id = "numero-sorte";
  // campoNumero.step = "0.01";

  // Adicionar o evento de apertar a tecla do enter, chamando a função para verificar
  // se o usuário descobriu o número da sorte
  campoNumero.addEventListener("keydown", (evento) => {
    if (evento.key === "Enter") {
      validarNumeroDigitado(evento);
    }
  });

  // Obter o body da página
  let body = document.querySelector("body");
  // Adicionar a label no body
  body.appendChild(labelNumero);
  // Adicionar o campo no body
  body.appendChild(campoNumero);

  // Definir o foco no campo do número
  campoNumero.focus();

  // Chamar função que gerará o número da sorte para o usuário descobrir
  gerarNumeroDaSorte();
  // Chamar função que desabilitará o botão de criar campo
  desabilitarBotao();
}

function validarNumeroDigitado(event) {
  // event é uma forma de obtermos a tag html que ocorreu aquele evento
  let campoNumero = event.target;
  // Obter o número que o usuário digitou
  let numeroDigitou = parseInt(campoNumero.value);

  if (numeroDigitou === numeroDaSorte) {
    alert("Acertou o número da sorte");
    return;
  }

	let diferenca;
	// Verificar se o número digitado é maior que o número da sorte, isso 
	// é necessário pois a diferença não deve ser negativa
	if(numeroDigitou > numeroDaSorte){
		// Subtrair do número digitado o número da sorte
		diferenca = numeroDigitou - numeroDaSorte;
	}else{
		// Subtrair do número da sorte o número digitado
		diferenca = numeroDaSorte - numeroDigitou;
	}

	console.log("Diferença: " + diferenca + "\nNúmero da sorte: " + numeroDaSorte);
	let mensagem = "";
	if(diferenca <= 3){
		mensagem = "Pelando";
	}else if(diferenca <= 8){
		mensagem = "Quente";
	} else if(diferenca <= 35){
		mensagem = "Frio";
	}else{
		mensagem = "Congelando";
	}
	alert(mensagem);
	campoNumero.focus();
}

function desabilitarBotao() {
  // Desabilitar o botão para o usuário n criar multiplos campos
  botaoCriarCampos.disabled = true;
  // Forma alternativa de desabilitar o botão
  // botaoCriarCampos.setAttribute("disabled", "disabled");
}

function gerarNumeroDaSorte() {
  // Gerar um número aleatório decimal ex.: 0.9581490129697068
  let numeroAleatorioDecimal = Math.random();
  // 95.81490129697068
  numeroAleatorioDecimal = numeroAleatorioDecimal * 100;
  // Obter somente o 95
  let numeroAleatorioInteiro = Math.round(numeroAleatorioDecimal);
  // Armazenar na variável numeroDaSorte(espoco global) o valor da variável que tem o scopo da função
  numeroDaSorte = numeroAleatorioInteiro;
}

botaoCriarCampos.onclick = criarCampo;
exemplo07-criar-elementos.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


    <button id="criar-campo">Criar campo</button>
    <script src="exemplo07-criar-elementos.js"></script>
</body>
</html>
exemplo06-calcular-folha-pagamento.css
.ocultar {
    display: none;
}
.campos {
    display: flex;
    gap: 5px;
    flex-direction: row;
}
.campos div{
    flex-grow: 1;
}
.campos label {
    display: block;
}
.campos input[type=text],
.campos input[type=number],
.campos select {
    width: 100%;
    border: 1px solid #ccc;
    border-radius: 2px;
    box-sizing: border-box;
    padding: 6px 6px;
}

.campos-modalidade div{
    display: flex;
    gap: 0;
}

.campos-modalidade span{
    display: block;
}

.campos-referencia{
    display: flex;
    gap: 10px;
    flex-grow: 1;
}

.campos-referencia-beneficios{
    display: flex;
}

.campos-referencia div{
    display: flex;
    flex-direction: column;
}

.campos-referencia select{
    border: 1px solid #ccc;
    border-radius: 2px;
    padding: 6px 6px;
    box-sizing: border-box;
}

.beneficios-titulo{
    font-weight: bold;
}

.campos-beneficios{
    flex-grow: 1;
}

.beneficios{
    justify-content: flex-end;
    align-items: start;
}

.beneficios div{
    display: flex;
    flex-direction: row;
}

.beneficio-plano-saude{
    display: flex;
    flex-direction: column;
}

.button-calcular{
    display: flex;
    justify-content: flex-end;
}
.button-calcular button{
    padding: 3px 6px;
    border-radius: 3px;
    border: 1px solid green;
    background-color: green;
    color: white;
}

.button-calcular button:hover{
    cursor: pointer;
}
exemplo06-calcular-folha-pagamento.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="exemplo06-calcular-folha-pagamento.css">
</head>

<body>
    <div class="campos">
        <div>
            <label for="campo-nome">Nome</label>
            <input type="text" id="campo-nome" required minlength="10" maxlength="60">
        </div>

        <div>
            <label for="campo-cargo">Cargo</label>
            <select id="campo-cargo" onchange="preencherSalarioBaseValorHora()">
                <option value="" disabled selected>Selecione uma opção</option>
                <option value="Assistente">Assistente</option>
                <option value="Junior">Junior</option>
                <option value="Pleno">Pleno</option>
                <option value="Senior">Senior</option>
            </select>
        </div>
    </div>

    <div class="campos">
        <div>
            <label for="campo-matricula">Matricula</label>
            <input type="number" id="campo-matricula">
        </div>
        <div class="campos-modalidade">
            <span>Modalidade</span>
            <div>
                <input type="radio" id="campo-modalidade-horista" name="modalidade" value="horista"
                    onchange="apresentarDivModalidade()">
                <label for="campo-modalidade-horista">Horista</label>
                <input type="radio" id="campo-modalidade-mensalista" name="modalidade" value="mensalista"
                    onchange="apresentarDivModalidade()">
                <label for="campo-modalidade-mensalista">Mensalista</label>
            </div>
        </div>
    </div>

    <div class="campos-referencia-beneficios">
        <div class="campos-referencia">
            <div>
                <label for="campo-mes-referencia">Mês Referência</label>
                <select id="campo-mes-referencia">
                    <option value="janeiro">Janeiro</option>
                    <option value="fevereiro">Fevereiro</option>
                    <option value="marco">Março</option>
                    <option value="abril">Abril</option>
                    <option value="maio">Maio</option>
                    <option value="junho">Junho</option>
                    <option value="julho">Julho</option>
                    <option value="agosto">Agosto</option>
                    <option value="setembro">Setembro</option>
                    <option value="outubro">Outubro</option>
                    <option value="novembro">Novembro</option>
                    <option value="dezembro">Dezembro</option>
                </select>
            </div>

            <div>
                <label for="campo-ano-referencia">Ano Referência</label>
                <select id="campo-ano-referencia">
                    <option value="2024">2024</option>
                    <option value="2025">2025</option>
                </select>
            </div>

            <div class="">
                <label for="campo-plano-saude">Plano de Saúde</label>
                <select id="campo-plano-saude">
                    <option value="Sem">Sem</option>
                    <option value="Básico">Básico</option>
                    <option value="Intermediário">Intermediário</option>
                    <option value="Completo">Completo</option>
                </select>
            </div>
            <div class="beneficios">
                <div>
                    <input type="checkbox" id="campo-plano-odontologico" name="campo-plano-odontologico" value="sim">
                    <label for="campo-plano-odontologico">Plano Odontologico</label>
                </div>
                <div>
                    <input type="checkbox" id="campo-auxilio-creche" name="campo-auxilio-creche" value="sim">
                    <label for="campo-auxilio-creche">Auxílio Creche</label>
                </div>
            </div>
        </div>
    </div>


    <div id="modalidade-horista" class="ocultar">
        <div>
            <span for="campo-valor-hora">Valor Hora</span>
            <span id="campo-valor-hora-value">R$ 0,00</span>
        </div>

        <div>
            <label for="campo-quantidade-horas">Quantidade horas</label>
            <input type="number" id="campo-quantidade-horas" min="1" max="300">
        </div>
    </div>

    <div id="modalidade-mensalista" class="ocultar">
        <div>
            <span id="campo-salario-base">Salário Base</span>
            <span id="campo-salario-base-value">R$ 0,00</span>
        </div>
    </div>

    <div class="button-calcular">
        <button onclick="calcular()">Calcular</button>
    </div>

    <script src="exemplo06-calcular-folha-pagamento.js"></script>
</body>

</html>
exemplo06-calcular-folha-pagamento.js
// Função responsável por apresentar ou ocultar as divs relacionadas à modalidade selecionada.
function apresentarDivModalidade() {
    // Obtém o valor do input 'modalidade' que está marcado (selecionado).
    let campoModalidade = document.querySelector("input[name='modalidade']:checked");
    let modalidade = campoModalidade.value;

    // Obtém as referências para as divs de 'mensalista' e 'horista'.
    let divMensalista = document.querySelector("#modalidade-mensalista");
    let divHorista = document.querySelector("#modalidade-horista");

    // Se a modalidade selecionada for 'horista', exibe a div de 'horista' e oculta a de 'mensalista'.
    if (modalidade === "horista") {
        divHorista.classList.remove("ocultar"); // Exibe a div de 'horista'.
        divMensalista.classList.add("ocultar"); // Oculta a div de 'mensalista'.

    // Se a modalidade selecionada for 'mensalista', exibe a div de 'mensalista' e oculta a de 'horista'.
    } else if (modalidade === "mensalista") {
        divMensalista.classList.remove("ocultar"); // Exibe a div de 'mensalista'.
        divHorista.classList.add("ocultar"); // Oculta a div de 'horista'.
    }
}

// Função responsável por preencher os valores do salário base e do valor da hora com base no cargo selecionado.
function preencherSalarioBaseValorHora() {
    // Obtém os elementos do DOM que contêm os campos para cargo, salário base e valor da hora.
    let campoCargo = document.querySelector("#campo-cargo");
    let campoSalarioBase = document.querySelector("#campo-salario-base-value");
    let campoValorHora = document.querySelector("#campo-valor-hora-value");

    // Obtém o valor do cargo selecionado.
    let cargo = campoCargo.value;
    let salario = 0; // Inicializa o salário com 0.

    // Formata os valores em moeda brasileira (R$).
    let formatadorMoeda = new Intl.NumberFormat('pt-BR', {
        style:'currency', // Define o estilo como moeda.
        currency: 'BRL'   // Define a moeda como Real (R$).
    });

    // Define o salário de acordo com o cargo selecionado.
    if (cargo === "Assistente") {
        salario = 1700.00; // Salário para o cargo 'Assistente'.
    } else if (cargo === "Junior") {
        salario = 2500; // Salário para o cargo 'Junior'.
    } else if (cargo === "Pleno") {
        salario = 4500; // Salário para o cargo 'Pleno'.
    } else {
        salario = 8000; // Salário para cargos superiores (outros casos).
    }

    // Exibe o salário formatado no campo de 'salário base'.
    campoSalarioBase.innerText = formatadorMoeda.format(salario);

    // Calcula o valor da hora dividindo o salário por 220 (quantidade de horas trabalhadas por mês).
    let valorHora = salario / 220;

    // Exibe o valor da hora formatado no campo de 'valor hora'.
    campoValorHora.innerText = formatadorMoeda.format(valorHora);
}

// Função responsável por calcular o salário baseado no valor da hora e quantidade de horas trabalhadas.
function calcular() {
    // Obtém o valor do campo que exibe o valor da hora e o campo que contém a quantidade de horas.
    let spanValorHora = document.querySelector("#campo-valor-hora-value");
    let campoQuantidadeHoras = document.querySelector("#campo-quantidade-horas");

    // Obtém o valor do campo 'valor hora' (em formato de texto), e remove o símbolo 'R$' e a vírgula.
    let valorHoraString = spanValorHora.innerText;
    valorHoraString = valorHoraString.replace("R$", "").replace(",", ".").trim();

    // Converte o valor da hora para número (float).
    let valorHora = parseFloat(valorHoraString);

    // Converte a quantidade de horas para número inteiro.
    let quantidadeHoras = parseInt(campoQuantidadeHoras.value);

    // Calcula o salário multiplicando o valor da hora pela quantidade de horas trabalhadas.
    let salario = valorHora * quantidadeHoras;

    // Exibe o salário calculado em uma janela de alerta.
    alert("Salário: " + salario);
}

function obterSalarioPorCargo(){
    
}
exemplo06-calcular-folha-pagamento.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="exemplo06-calcular-folha-pagamento.css">
</head>

<body>
    <div>
        <label for="campo-nome">Nome</label>
        <input type="text" id="campo-nome" required minlength="10" maxlength="60">
    </div>

    <div>
        <label for="campo-cargo">Cargo</label>
        <select id="campo-cargo">
            <option value="" disabled selected>Selecione uma opção</option>
            <option value="Assistente">Assistente</option>
            <option value="Junior">Junior</option>
            <option value="Pleno">Pleno</option>
            <option value="Senior">Senior</option>
        </select>
    </div>

    <div>
        <label for="campo-matricula">Matricula</label>
        <input type="number" id="campo-matricula">
    </div>

    <div>
        <label for="campo-mes-referencia">Mês Referência</label>
        <select id="campo-mes-referencia">
            <option value="janeiro">Janeiro</option>
            <option value="fevereiro">Fevereiro</option>
            <option value="marco">Março</option>
            <option value="abril">Abril</option>
            <option value="maio">Maio</option>
            <option value="junho">Junho</option>
            <option value="julho">Julho</option>
            <option value="agosto">Agosto</option>
            <option value="setembro">Setembro</option>
            <option value="outubro">Outubro</option>
            <option value="novembro">Novembro</option>
            <option value="dezembro">Dezembro</option>
        </select>
    </div>

    <div>
        <label for="campo-ano-referencia">Ano Referência</label>
        <select id="campo-ano-referencia">
            <option value="2024">2024</option>
            <option value="2025">2025</option>
        </select>
    </div>

    <div>
        <span>Modalidade</span>
        <input type="radio" id="campo-modalidade-horista" name="modalidade" value="horista">
        <label for="campo-modalidade-horista">Horista</label>
        <input type="radio" id="campo-modalidade-mensalista" name="modalidade" value="mensalista">
        <label for="campo-modalidade-mensalista">Mensalista</label>
    </div>

    <div id="modalidade-horista" class="ocultar">
        <div>
            <span for="campo-valor-hora">Valor Hora</span>
            <span id="campo-valor-hora-value">R$ 0,00</span>
        </div>
        
        <div>
            <label for="campo-quantidade-horas">Quantidade horas</label>
            <input type="number" id="campo-quantidade-horas" min="1" max="300">
        </div>
    </div>

    <div id="modalidade-mensalista" class="ocultar">
        <div>
            <span id="campo-salario-base">Salário Base</span>
            <span id="campo-salario-base-value">R$ 0,00</span>
        </div>
    </div>

    <script src="exemplo06-calcular-folha-pagamento.js"></script>
</body>

</html>
exemplo02-if.js
// Solicitar para o usuário o nome
let nome = prompt("Digite o nome")

// Solicitar para o usuário a quantidade
let quantidade = parseInt(prompt("Digite a quantidade"))

// Solicitar para o usuário o preço
let preco = parseFloat(prompt("Digite o preço"))

// parseInt faz a conversão do que o usuário preenche(vem como string) para int
// parseFloat faz a conversão do que o usuário preenche(vem como string) para float (números reais, ex.: 2940.30)
let totalParcial = quantidade * preco
let desconto = 0

// Se a quantidade for menor que 100 dar um desconto de R$ 5,00
if (quantidade < 100){
    desconto = 5.00
} else if(quantidade < 500) { // Quantidade menor 500 dar um desconto de R$ 35,42
    desconto = 35.42
} else { // Senão o desconto será de R$ 70,00
    desconto = 70.00
}
let totalPedido = (quantidade * preco) - desconto
alert(
    "Produto:" + nome +
    "\nQuantidade: " + quantidade + 
    "\nPreço unitário: " + preco +
    "\nDesconto: " + desconto + 
    "\nTotal Pedido: " + totalPedido);

// Operadores relacionais
// ===  Igual
// <    Menor
// <=   Menor ou igual
// >    Maior
// >=   Maior ou igual
// !=   Diferente

exemplo03-if.js
let cargo = prompt("Digite o seu cargo");
let anosCasa = parseInt(prompt("Digite a quantidade de anos de casa"));

let salario = 0;
if (cargo === "Desenvolvedor Júnior") {
    salario = 2200.00;
} else if (cargo === "Desenvolvedor Pleno") {
    salario = 5000.00;
} else if (cargo === "Desenvolvedor Senior") {
    salario = 8000.00;
} else if (cargo === "Especialista I") {
    salario = 12000;
} else if (cargo === "Especialista II") {
    salario = 17000;
}
// 1 ano  => 50%
// 2 anos => 75%
// 3 anos => 100%
// 5 anos => 125%
// 7 anos => 150% 7,8,9 anos
// 10 anos => 200% 

let percentualPlr = 0;
if (anosCasa === 1) {
    percentualPlr = 0.5;
} else if (anosCasa === 2) {
    percentualPlr = 0.75;
} else if (anosCasa <= 4) {
    percentualPlr = 1;
} else if (anosCasa <= 6) {
    percentualPlr = 1.25;
} else if (anosCasa <= 9) {
    percentualPlr = 1.50;
} else {
    percentualPlr = 2.00;
}

let plr = salario * percentualPlr;
alert(
    "Cargo: " + cargo +
    "\nAnos de casa: " + anosCasa +
    "\nSalário: " + salario +
    "\nPercentual PLR: " + percentualPlr +
    "\nPLR: " + plr);