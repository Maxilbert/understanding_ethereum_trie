from ethereum import trie
from ethereum.db import DB
import codecs


triedb = DB()
state = trie.Trie(triedb, trie.BLANK_ROOT)
print('root hash', state.root_hash)
print('root hash', codecs.encode(state.root_hash, 'hex'))
state.update(b'\x01\x02\x03', b'\x01\x02\x03')
print('root hash', state.root_hash)
print('root hash', codecs.encode(state.root_hash, 'hex'))
k, v = state.root_node
print('root node:', [k, v])
print('hp encoded key, in hex:', k)
