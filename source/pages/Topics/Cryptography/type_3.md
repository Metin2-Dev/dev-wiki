<!-- LINKS -->
[history:type_3]: https://history.metin2.dev/topics/cryptography/type_3


# Panama (Type 3)

Security {octicon}`key;1em;sd-text-info`
{bdg-danger}`Weak`
{bdg-danger-line}`Not Recommended`
|
Compression {octicon}`three-bars;1em;sd-text-info`
{bdg-warning}`Medium`
{bdg-warning-line}`Not Recommended`
{octicon}`circle;1em;sd-text-warning`


History {octicon}`book;1em;sd-text-info`
{bdg-secondary-line}`Unexistent`
|
RFC Standard {octicon}`comment;1em;sd-text-info`
{bdg-secondary-line}`Unexistent`
___


## Composition
Compute the CRC32 of the filename 
AND the CRC with the integer 3
Pick a cipher by index based on the AND above

Filename Ciphers:

| Index | Name      | Description |
|-------|-----------|-------------|
| 0     | Whirlpool |             |
| 1     | Tiger     |             | 
| 2     | Sha1      |             |
 | 3     | RIPEMD128 |             |


Filename is encrypted using the selected cipher
The first 4 bytes of the result ciphered filename are AND'ed
Pick a cipher by index based on the AND above

| Index | Name      | Description |
|-------|-----------|-------------|
| 0     | SHA1      |             |
| 1     | RIPEMD128 |             | 
| 2     | Whirlpool |             |
 | 3     | Tiger     |             |


Appendix A (Python Representation)
```python
filename_crc = crc32(filename)

filename_ciphers = {
    0: Whirlpool,
    1: Tiger,
    2: Sha1,
    3: RIPEMD128
}

# Make an AND operation on the filename by 4 to act as an index
# And use the index to decide the cipher to use
filename_cipher_index = filename & 4
filename_cipher = filename_ciphers[filename_cipher_index]

ciphered_filename = filename_cipher(filename)

# The panama cipher picker is the first 4 bytes of the ciphered filename
panama_cipher_picker = filename_cipher[4:]

data_ciphers = {
    0: Sha1,
    1: RIPEMD128,
    2: Whirlpool,
    3: Tiger
}

# The panama key IV is the remainder slice of the ciphered filename
ciphered_filename_remainder = filename_cipher[:4]

# And the index to decide the cipher to use is an AND operation by 3
panama_key_cipher_index = ciphered_filename_remainder & 3
panama_key_cipher = filename_ciphers[filename_cipher_index]

# Cipher the remainder slice and get a 32-bytes key named the Panama key
panama_key = panama_key_cipher(ciphered_filename_remainder)
```


Appendix B (Python Representation)
```python

```

