# Challenge Month 0
## Problem Statement
You are the top Cryptographer in the country. Shortly after reading up the mailing list "The Cryptographer's Message Digest" before bed, you decide to check your emails. Surprisingly, you find a PGP Encrypted official email from the government.
``````

Subject Header: Government Request
Greetings,

I am Secretary Rachel writing on behalf of Chairman R. Anderson of the National Security Council.

Our nation's future is at stake! My former superior, Mr Warded Densnow, has defected to the government of, our public adversary, Genovia. Our intelligence has gathered that Mr Densnow has been leaking national secrets on the W1NKEY forums, under the guise of "concerns for the Public's privacy", though truly there has been a paper trail of cryptocurrency going into his wallet originating from known wallet addresses of Genovia's royalty. This is with no doubt, a plot from Genovia's Prime Minister Julian Andrews, to stir up doubt with the government in the community and disrupt the upcoming elections.

For our fellow citizens' safety, we wish to keep Mr Densnow's arrest as quiet as possible, and to do this we would need to submit a fake post posing as Mr Densnow on the W1NKEY forums, saying he would retire himself from the community.

Unfortunately, Mr Densnow uses RSA Cryptography to verify his messages. We have uncovered his 3 public keys, attached to this email.

You are required to find his private keys, so that a fake message can be sent on his behalf, or else his correspondents will realise he has been arrested and will leak the source code of our sophisticated surveillance programs that we have invested billions on!

You are required to work on this exclusively (or, with aid from the NSC) on your own. We will hash out the details of your compensation in the future. Your country thanks you.

Regards,

Ross

Acting President of the National Security Council

---- Attachments: Note that the X digits refer to the amount of digits of p and q, not the decryption key. 9 digit public key
e=65537
n=171019909643746679

10 digit public key
e=65537
n=21777440010282826951

11 digit public key
e=65537
n=4971964884032795251133
``````
## Out-Of-Universe Details:
Of course you could cheat and use existing tools to find the private key, but that won't be fun now, won't it? You win bragging rights to being the first to get the private key. You can verify it is the correct private key using by going to my website https://b1te.my/rsa/ look under the "Out-Of-Universe Details" section I suggest using python since that's what we're learning. Alternatively you can use Java I suppose, though you would need a BigInteger library since the numbers you'll be working with won't fit into the 64 bit range, even for unsigned values. The time it takes for you to brute-force the private key will depend on how fast your computer is, but you can optimise the code to do so in less time if you have an even less powerful computer than mine. See the Wikipedia article on RSA: https://en.wikipedia.org/wiki/RSA_(cryptosystem) I also believe RSA was briefly partially explained in one of the lectures. Basically what you need to do is brute-force to find 'd', the decryption key, given n and e, and we know that d is the modular multiplicative inverse of e. e=65537 d=? n=... I have written a short paper on the subject if you need further help. You can find my paper in the "paper" directory. Email me your answers at naavinravi@gmail.com along with the name you want to be credited as on the leaderboard below, and optionally a message. Each key is worth 5 points each. You can also send me a public write-up (on a blog or something) on how you did it, which will net you 3 additional points for each method you describe for finding the private key. You don't have find all private keys before emailing me.

 On my main machine (Ryzen 7 4700U), using a very basic naive algorithm (although it does skip even numbers) in python it can do between 2.3 million to 2.7 million checks per second (including the skips for even numbers) , although this is not a very fair test as I have a Virtual Machine on, a web browser with many tabs open, as well as several other things. My secondary machine (a first-generation Surface Go) manages just slightly over 2 million checks per second, although this isn't an apt comparison since on this machine, I'm not running any intensive programs. On a Raspberry Pi 3B+ running Ubuntu MATE, it does around 450,000 checks per second. So all-in-all, unless you somehow use a computer worse than a Raspberry Pi, I'm sure you can at least brute-force the first key.

On my primary machine (the one which in python does around 2.3 million to 2.7 million checks per second), I tested it with C++ code using the same method and it did around 17 million checks per second (Again, still with all the other programs running)

So, for a 9 digit p and q, for my worst machine, the raspberry pi, let's see what the worst case scenario is.

so the worst case is that p or q is 999999999. Now divide it by the 450k that the rpi does in a second and it turns out to be rougly 2222 seconds, which is just a mere 37 minutes. So you likely have a much more powerful laptop, so there is no excuse for not solving that.

The 10 digits takes a bit longer, although should still be feasible if you let your laptop run it in the background for just a short while. I recommend printing the currently being tested number every few seconds. It'll probably slow it down a bit, but having random numbers flowing away at your terminal looks cool, and let's you know it hasn't somehow got stuck in an infinite loop.

The 11 digits version is a bit trickier. You could run the same program as you did in the previous versions, but it might take a while (unless I underestimated how much having my web browser and Virtual Machine on affects things and it is actually very fast to do so.). I suggest either using a compiled language or getting creative somehow. Perhaps some clever factorisation attacks (Fermat's factorisation?), or generating a list of primes and using that to your advantage, or since I include a checker perhaps you can take a look at my messy code and figure out if there is a way to attack that, or perhaps distribute your workload among several computers! Do let me know how you did it, I would love to hear about it.

All in all, I have taken careful consideration that it can be brute-forced in a very reasonable amount of time, so I don't want to hear complaints that it would take far too long to brute-force on your computer. :P Happy Programming!
