from ethereum.trie import Trie, BLANK_ROOT
from ethereum.db import DB
import codecs


db = DB()
trie = Trie(db, BLANK_ROOT)
print('root hash', trie.root_hash)
print('root hash', codecs.encode(trie.root_hash, 'hex'))
trie.update(b'\x01\x02\x03', b'\x01\x02\x03')
print('root hash', trie.root_hash)
print('root hash', codecs.encode(trie.root_hash, 'hex'))
k, v = trie.root_node
print('root node:', [k, v])
print('hp encoded key, in hex:', k)
