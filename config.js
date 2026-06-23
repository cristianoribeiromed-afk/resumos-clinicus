// CONFIGURAÇÕES EDITÁVEIS — mude aqui sem tocar no resto do site
const CONFIG = {
  whatsappNumero: "5547991572214", // DDI 55 (Brasil) + DDD 47 + número. Troque aqui se mudar.
  nomeMarca: "Resumos Clinicus",
  pixChave: "cristianoribeiromed@gmail.com", // chave PIX (email)
  pixNome: "Cristiano Ribeiro da Silva",       // precisa bater com o nome no banco
  pixCidade: "Blumenau",                       // cidade da conta bancária
  mensagemWhatsappTemplate: (nome, item, preco) =>
    `Olá! Acabei de pagar *${item}*${preco ? " (Gs. " + preco + ")" : ""}. Meu nome é ${nome || "___"} e meu email é ___. Segue o comprovante:`
};
