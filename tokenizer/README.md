## Token Vault with Bidirectional Mapping

Replaces sensitive data with non-sensitive tokens to reduce scope of PCI compliance. 

### Features
- Generates random token with UUIDv4
- Tokens are useless outside of the vault
- Limits PCI compliance scope to the vault
- Prevents duplicates (same card -> same token)

### Production Notes
This demo uses in-memory storage. 

Scaling to production requires:
- Encrypted database with access controls
- Access logging for audit trails
- Implementation of token expiration
