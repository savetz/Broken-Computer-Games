# Broken Computer Games

[Broken Computer Games](https://archive.org/details/broken-computer-games) is a generated book for [NaNoGenMo2022](https://github.com/NaNoGenMo/2022) (National Novel Generation Month).

"Broken" is based on the real book [Basic Computer Games by David Ahl](https://www.atariarchives.org/basicgames/). That book was published by Dave Ahl in 1978, and he [put it into the public domain](https://blog.adafruit.com/2022/06/16/david-ahl-places-all-his-classic-computing-publications-into-the-public-domain/) in 2022. Basic Computer Games was the first computer book to sell one million copies, and taught a generation of budding programers how to program in the BASIC language.

This little python script randomly selects two of the Basic computer games and mashes them up by choosing a few lines of code from each program. I generated hundreds of these, then ran the programs in [pybasic](https://github.com/richpl/PyBasic).

    for i in {001..500}; do python3 mashup.py > program$i.bas ; echo "load program$i\nrun\n2\n3\n4\nexit\n" \
    | python3 pybasic/interpreter.py | tail +10 | sed 's/^.*###/###/' | grep -v "Program read from file" \
    > output/output$i.txt ; echo "----" ; done

I chose the programs with the most interesting output. Finially, I used [Text to PDF](http://rootrisetech.com/product/text-to-pdf) to generate the PDF.

[Read Broken Computer Games](https://archive.org/details/broken-computer-games)

[Read BASIC Computer Games](https://archive.org/details/Basic_Computer_Games_Microcomputer_Edition_1978_Creative_Computing)

[Code from the book came from vintage-basic.net](http://www.vintage-basic.net/games.html)

[Dot Matrix Font](https://www.dafont.com/dot-matrix.font) 

[What Font Is?](https://www.whatfontis.com) identified fonts for the cover

which are [FattiPattiFLF](https://www.whatfontis.com/FF_FattiPattiFLF.font?text=BASIC)

and [OptiPlanet-Light](https://www.ffonts.net/OPTIPlanet-Light.font?text=101 Great Games)

and I didn't end up using [Trumania EEN](https://www.ffonts.net/Trumania-EEN-Plain.font?text=Blackjack) but you know you want to
