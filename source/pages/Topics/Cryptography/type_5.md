<!-- LINKS -->
[history:type_5]: https://history.metin2.dev/topics/cryptography/type_5


# HybridCrypt+ (Type 5)

Strength {octicon}`key;1em;sd-text-info` :
{bdg-warning}`Medium`
{bdg-info-line}`Recommended`

History {octicon}`book;1em;sd-text-info`:
[Hybrid Encryption][history:hybrid-crypt]
|
RFC Standard {octicon}`comment;1em;sd-text-info`:
{bdg-secondary-line}`Unexistent`
___


This algorithm is based on [HybridCrypt](type_4.md), adding
a few more steps that make the base construct slightly better


## Distinction
A portion of the file to be encrypted/decrypted is sliced
and stored in the server

This ensures that it's impossible to fully retrieve the content of
a file without making a valid request to the server, despite being
more consuming in terms of bandwidth.

## Composition
The algorithm makes the sames procedures as its base only adding
a slicing step

### Slicing

Before the base algorithm is performed, the file is sliced in two,
the slice starts from the end of the file length to a range of
64 to 128 bytes (how this is decided is unknown)

Then the first part of the slice is processed by the base algorithm,
leaving the second part of the slice untouched.

The second part should be output to a file and named
`filename_hybridcript`

[//]: # (TODO: Finish explanation)
### Deployment


### Decryption
The extra data will be sent to the client once the client has
successfully logged in (same as the HybridCrypt keys)

The data sent from the Server is not encrypted in any form.
