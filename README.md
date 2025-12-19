# Fences Security Analysis – Trial & Licensing Weaknesses

## Visão geral

Este projeto tem caráter **educacional e técnico** e foi desenvolvido com o objetivo de **analisar falhas comuns de segurança em mecanismos de licenciamento baseados em estado local**.

O foco não é a quebra de um software específico, mas a **demonstração prática de como decisões arquiteturais frágeis permitem que um programa simples induza um software a reiniciar seu período de avaliação**, sem necessidade de engenharia reversa avançada ou modificação de binários.

O projeto foi pensado sob a ótica de **Red Team / análise defensiva**, visando estudo, documentação e melhoria de práticas de segurança.

---

## Escopo e modelo de ameaça (Threat Model)

O cenário analisado considera um atacante com as seguintes capacidades:

- Acesso local ao sistema operacional
- Nenhuma modificação direta no binário do software alvo
- Nenhum bypass de DRM em nível de kernel
- Nenhuma exploração de vulnerabilidades de memória
- Apenas interação com:
  - arquivos
  - fluxos normais de ativação
  - comportamento padrão do sistema

Esse modelo representa um **usuário comum**, não um atacante avançado — justamente onde muitos mecanismos de licenciamento falham.

---

## Arquitetura de licenciamento analisada (alto nível)

A análise revelou um modelo de licenciamento baseado principalmente em:

- **Artefatos locais persistentes**
- Estado de trial armazenado no sistema
- Validação de ativação previsível
- Ausência de verificação forte de integridade

Nesse modelo, o estado local é tratado como **fonte de verdade**, o que introduz fragilidades críticas quando não há mecanismos adicionais de proteção.

---

## Fluxo de funcionamento do projeto (visão técnica controlada)

Esta seção descreve o fluxo interno da aplicação, com o objetivo de demonstrar como decisões arquiteturais inseguras podem ser exploradas, sem fornecer instruções operacionais para reprodução do comportamento.

1. **Identificação do estado local do software:**

    O projeto inicia verificando a existência de artefatos locais utilizados pelo software analisado para representar o estado de ativação e uso do período de avaliação.
    Esses artefatos são tratados pelo sistema como fonte de verdade, sem validação externa adicional.

**Ponto de falha evidenciado:** confiança irrestrita em estado local persistente.

2. **Normalização do ambiente de execução**

    Ao identificar que o estado local representa um uso anterior, a aplicação força a criação de um novo contexto de execução logicamente equivalente a uma primeira utilização do software.
    
    Nenhum binário é modificado e nenhuma proteção é desativada — o comportamento explorado já é aceito pelo próprio fluxo normal da aplicação.
    
**Ponto de falha evidenciado:** ausência de vínculo forte entre estado local e identidade do sistema.

3. **Automação de interações legítimas**

    Com o ambiente normalizado, o projeto automatiza apenas interações já previstas pela interface oficial, simulando ações de um usuário comum.
    
    Essa etapa demonstra que o sistema não diferencia interação humana de automação, nem aplica controles adicionais em fluxos críticos.

**Ponto de falha evidenciado:** ausência de mecanismos anti-automação ou validação comportamental.

4. Dependência fraca de identidade

    O processo de ativação temporária aceita informações voláteis como suficientes para validar o período de avaliação, sem exigir associação persistente com hardware, conta autenticada ou identidade criptográfica.

**Ponto de falha evidenciado:** modelo de licenciamento desacoplado de identidade confiável.

5. Resultado observado

O software interpreta o novo contexto como uma execução legítima inicial, evidenciando que o mecanismo de proteção depende exclusivamente de fatores locais e previsíveis.

O projeto demonstra que complexidade técnica não é requisito para falhas graves, quando decisões arquiteturais inadequadas estão presentes.

---

## Classes de falhas de segurança identificadas

### 1. Confiança excessiva em estado local

O software assume que informações armazenadas localmente são íntegras e confiáveis.

  
 Desse modo qualquer dado local pode ser removido, recriado ou revertido sem que o software perceba, caso não exista verificação externa ou criptográfica.

---

### 2. Ausência de verificação de integridade forte

Os artefatos responsáveis por controlar o estado do trial não apresentam:

- Assinatura criptográfica robusta
- Detecção de rollback de estado
- Proteção contra recriação de contexto válido

Isso permite que estados antigos ou “limpos” sejam aceitos como legítimos.

---

### 3. Falta de vinculação entre licença e identidade

O estado de ativação não está fortemente vinculado a:

- hardware
- identidade criptográfica
- TPM
- fingerprint confiável do sistema

Sem essa vinculação, o software não consegue distinguir entre um ambiente novo e um ambiente artificialmente reinicializado.

---

### 4. Fluxo de ativação determinístico

O processo de ativação segue um fluxo previsível e automatizável.

Isso facilita:
- repetição de comportamento
- simulação de novos estados
- reinicialização lógica do trial

Não há desafios dinâmicos nem validações adaptativas.

---

## Como este projeto demonstra essas falhas

O código deste repositório **não explora vulnerabilidades de baixo nível**.

Ele apenas:
- automatiza interações legítimas do sistema operacional
- manipula estados locais tratados como confiáveis pelo software
- evidencia como a ausência de validações robustas permite a reinicialização do período de avaliação

O objetivo é **demonstrar o problema arquitetural**, não fornecer um exploit reutilizável, peço para que não deturpe o projeto para fins ilegais.

---

## Impacto de segurança

As falhas observadas permitem:

- Bypass do modelo de trial
- Reutilização indefinida do período de avaliação
- Quebra da confiança no mecanismo de licenciamento
- Replicação do mesmo problema em outros softwares com arquitetura similar

Esse tipo de falha é especialmente crítico por **não exigir conhecimento técnico avançado** para ser explorado.

---

## Recomendações defensivas

Algumas medidas que mitigariam esse tipo de problema:

- Vincular licenças a identidades criptográficas
- Assinar estados de ativação com verificação forte de integridade
- Implementar detecção de rollback
- Evitar confiança exclusiva em estado local
- Introduzir validações dinâmicas no fluxo de ativação

Essas práticas reduzem drasticamente a viabilidade desse tipo de bypass.

---

## Aviso legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais e de análise de segurança**.

O autor não se responsabiliza pelo uso indevido das informações aqui apresentadas.  
O objetivo é promover **boas práticas de segurança**, não violar termos de uso de softwares comerciais.

