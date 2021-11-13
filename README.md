# Python-DIY-BIP39-Key-gen
DIY Bitcoin Private Key Project: BIP0039

This project was inspired by this post: https://bitcoinmagazine.com/culture/diy-bitcoin-private-key-project

The 2048 english word list is hosted at: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

Download into the same local directory as this script

Use the cli command: `wget https://github.com/bitcoin/bips/raw/master/bip-0039/english.txt`

**Advice:** make the local file 'read only'

---

## **Some Notes:**
As is, this script creates a local file called "word_list.txt" which contains the generated, 24 seed words.

This I acknowledge is not best practise, as it's a security risk, but it's there for convenience (which is the enemy of security) and needs to be securely erased if this is used for a live wallet.

Moving forward (some details are in the To-Do file) I will address this.
