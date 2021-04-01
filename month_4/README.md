# Challenge Month 4

## Problem Statement
The Jokester has kidnapped a high-profile individual.
You, the police, have intercepted two encrypted messages he sent 
to his friends, which you suspect contains the password to his
encrypted hard-drive you seized from his house before he fled.

Your mole on the inside gives you intel and says that he brags
that he uses "The most secure encryption in the world, the one-time-pad".

He has also told you that the messages are pictures in the pbm image file format.

The pbm file format is an image file format which has the header
`P6\n1366 768\n255\n`, where `\n` is the `\x0a` byte and both files start with this header.

Your job is to somehow crack the "most secure encryption in the world"
and figure out the password!

Hint: The challenge this month is easy and doesn't really warrant a paper. Just look into One-Time-Pads and the properties of the Exclusive Or. You may also be interested in looking into "Vernam's Cipher".

As a brief summary, a One-Time-Pad is just a stream of completely random
data that is the same size of the plaintext, which is then mixed with the plaintext (usually with an Exclusive Or (XOR)) to get the ciphertext. The
stream of random data will act as the "key" that both parties would need
to know.

The Exclusive Or is a logical operation, similar to OR, but differs in that 
it is not true when both inputs are 1. The reason we can use XOR in the
One Time Pad is because it has the property such that given P XOR K = C 
(where P is the plaintext, K is the one-time-pad and C is the ciphertext),
P = K XOR C.

Additionally, I have used the RAW Binary data of PBM. The file format is 
extremely simple. It starts with the header I gave above, where 1366 is the image width, 768 is the image height, and 255 is the "maximum colour value", here we have 255, so 0 to 255 is 256, and that is 256 bits, so for each colour component (red, green and blue) we have one byte.

The data proceeding that would simply be the red, green and blue values for
each pixel starting from the top left going all the way to to the bottom right
in a zig-zag pattern, going left-to-right, down one row, and left-to-right again.

For example: 
`P6\n2 2\n255\n\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\x00\x00` would
result is a file that is 2 by 2 pixels, the top left being red (0xFF red, 0x00 green and 0x00 blue), the top right
being green (0x00 red, 0xFF green, 0x00 blue), bottom right being blue, and the bottom right being red.

Note that you may want to replace the encrypted header with a valid header, perhaps with a hex editor,
just to visualise how it looks like (there is no error-checking or decompression going on, so assuming you have a valid header, it will show an image), and keep doing this while you're playing around with the values to see what happens.

Alternatively, you can open the image as raw image data in a phote-editing tool or use a library in your preferred programming language to quickly visualise it.

The files can be found in `./jokes_on_you_ppm2.bin` and `./jokes_on_you_ppm1.bin`.
