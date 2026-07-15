// CONFIGURAÇÕES EDITÁVEIS — mude aqui sem tocar no resto do site
const CONFIG = {
  whatsappNumero: "5567992443248", // DDI 55 (Brasil) + DDD 47 + número. Troque aqui se mudar.
  nomeMarca: "ClinicusMed",
  pixChave: "cristianoribeiromed@gmail.com", // chave PIX (email) — mantido como reserva/fallback
  pixNome: "Cristiano Ribeiro da Silva",       // precisa bater com o nome no banco
  pixCidade: "Blumenau",                       // cidade da conta bancária
  clinicusApiUrl: "https://clinicus-ten.vercel.app", // backend que gera o checkout do Mercado Pago
  mensagemWhatsappTemplate: (nome, item, preco) =>
    `Olá! Acabei de pagar *${item}*${preco ? " (Gs. " + preco + ")" : ""}. Meu nome é ${nome || "___"} e meu email é ___. Segue o comprovante:`
};
