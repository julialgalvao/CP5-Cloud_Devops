# CP05 — Pipeline DevSecOps

**FIAP · Engenharia de Software — Disciplina: DevSecOps and Cloud Computing**

### Integrantes do grupo
| Nome | RM |
|------|----|
| Julia Leite Galvão | RM550201 |
| Camilly Breitbach Ishida | RM551474 |
| Aline Fernandes Zeppelini | RM97966 |

---

## Objetivo

Após o vazamento de uma chave de API em um commit público, foi exigido um
**pipeline de segurança obrigatório** no GitHub Actions. Este repositório
implementa esse pipeline, que roda automaticamente a cada *push* e *pull request*
e **barra** três classes de problema antes que cheguem à branch principal:

1. **Segredos** expostos no código ou no histórico de commits;
2. **Código vulnerável** (análise estática de segurança);
3. **Imagens Docker** com CVE crítico.

## Estrutura do projeto

```
.
├── .github/workflows/security.yml   # pipeline de segurança (3 barreiras)
├── Dockerfile                       # imagem do site (alvo da análise de CVE)
├── site/index.html                  # site estático publicado pela imagem
├── app.py                           # aplicação de apoio
└── .gitignore
```

## As três barreiras de segurança

| Ferramenta | Tipo | O que protege |
|-----------|------|---------------|
| **Gitleaks** | Secret scanning | Varre código e histórico atrás de chaves, tokens e senhas. Falha o pipeline quando encontra um padrão de credencial, impedindo que um segredo vazado chegue à branch principal. |
| **Semgrep** | SAST (análise estática) | Lê o código-fonte sem executá-lo e o compara com regras de padrões inseguros, sinalizando vulnerabilidades (ex.: execução arbitrária de código) antes de irem para produção. |
| **Trivy** | Scan de imagem | Escaneia a imagem Docker construída a partir do `Dockerfile` e cruza seus pacotes com bancos de CVE conhecidos, falhando quando há vulnerabilidade de severidade **CRÍTICA**. |

## Como o pipeline funciona

O workflow [`.github/workflows/security.yml`](.github/workflows/security.yml)
define três *jobs* independentes — `gitleaks`, `semgrep` e `trivy` — disparados
em todo *push* e *pull request*. Se qualquer barreira detectar um problema, o
*job* correspondente falha (fica vermelho na aba **Actions**) e sinaliza o risco,
cumprindo o papel de controle de segurança obrigatório exigido pela organização.
