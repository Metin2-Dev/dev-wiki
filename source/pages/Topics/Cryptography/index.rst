Cryptography
=============

In this section its listed information about known algorithms,
their details and aliases

To make naming simple, the algorithms are categorized by types
followed by their successive number

To classify how strong the algorithms are **within each other**
(not real time security grades), the following classifications
are defined:


:bdg-success:`Very Strong`
:bdg-primary:`Strong`
:bdg-warning:`Medium`
:bdg-danger:`Weak`
:bdg-secondary:`Inexistent`


And how much the algorithms are recommended for use:

:bdg-success-line:`Strongly Recommended`
:bdg-info-line:`Recommended`
:bdg-warning-line:`Not Recommended (unless legacy support)`
:bdg-danger-line:`Not Recommended`


Some types might have symbols behind words and be embraces in
parentheses, the have a signification meanings as:

The symbol **~** means that the word after is an encryption/cipher
algorithm and the **-** means that the word after is a compression
algorithm

For example, **-LZO** means that the LZO algorythm is applied to
a set of data, or for example **~XTEA(-LZO)** means that
an LZO algorithm is applied to a set of data and the result has then
as the **XTEA** encryption algorythm applied to it


Algorythm Types
################
.. toctree::
   :maxdepth: 1

   type_0
   type_1
   type_2
   type_3
   type_4
   type_5
   type_6

