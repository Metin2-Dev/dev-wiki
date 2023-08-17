<!-- LINKS -->


# Eter VFS
Eter is the default virtual file system, it handles with loading files from the disk and index
their locations, which are called units, security and compression procedures

Units are also called 'Packs', and these units contain information about files inside them such as
their virtual paths and data files that can be raw/compressed/encrypted


## Disk Indexing
To know which files on the disk belong to which virtual spaces there is an index which normally
is located at `pack/Index`, it has information about which virtual paths belong to a Unit Name


## Virtual Indexing


## Unit Handlers


### Cryptography

