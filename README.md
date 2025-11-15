# Payment Systems Lab

An exploration of payment systems, card processing, and financial technology concepts through Python. This repository contains practical implementations of core payment primitives and industry patterns.

## Explorations

### 💳 [card_validator](https://github.com/loralyn-milcarek/pay-lab/tree/main/card_validator)
A practical implementation of credit card validation covering Luhn checksum verification, card type identification via BIN prefix matching, and length validation per network. 

### 🔒 [tokenizer](https://github.com/loralyn-milcarek/pay-lab/tree/main/tokenizer)
A PCI-compliant tokenization system that replaces sensitive card numbers with secure, reversible tokens. Simulates how payment processors protect cardholder data by storing real PANs in an isolated vault while distributing non-sensitive tokens for transaction processing.

---

<!-- ### 🔮 Coming Soon

- **Token Generator** — PCI-compliant tokenization patterns
- **Payment Gateway Client** — Auth, capture, refund flows with idempotency
- **Transaction Ledger** — Settlement and reconciliation reporting
- **Async Processor** — High-throughput payment handling
- **Terminal Simulator** — Full-stack capstone with hardware integration -->
