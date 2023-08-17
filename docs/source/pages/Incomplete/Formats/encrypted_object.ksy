meta:
  id: encrypted_object
  endian: le

seq:
  - id: header
    type: header

  - id: compression_magic_check
    type: u4
    if: header.ciphered_size == 0
    enum: compression_magic

  - id: ciphered_magic_check
    type: u4
    if: header.ciphered_size != 0

  - id: object_data
    size: header.ciphered_size
    if: header.ciphered_size > 0

  - id: compressed_content
    size: header.compressed_size - 4
    if: header.ciphered_size == 0

types:
  header:
    seq:
      - id: compression_magic
        type: u4
        enum: compression_magic

      - id: ciphered_size
        type: u4

      - id: compressed_size
        type: u4

      - id: raw_size
        type: u4

enums:
  compression_magic:
    1515144013: mcoz
    1347633997: mcsp


