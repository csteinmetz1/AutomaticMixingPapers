# Automatic mixing research 
Tracking academic work in the field of automatic multitrack audio mixing.

View the live site [csteinmetz1.github.io/AutomaticMixingPapers](https://csteinmetz1.github.io/AutomaticMixingPapers/).

## Contributing
To add new publications follow the instructions below:

1. Fork the repo.

2. Clone your fork to a local directory.
```
git clone https://github.com/YOUR-USERNAME/AutomaticMixingPapers.git
```

3. Edit the data/research.json file and add a new entry, for example:
```
{
    "title" : "A real-time semiautonomous audio panning system for music mixing",
    "author" : "E. Perez Gonzalez and J. D. Reiss",
    "year" : 2010,
    "category" : "Panning",
    "approach" : "KBS",
    "pdf" : "https://asp-eurasipjournals.springeropen.com/articles/10.1155/2010/436895",
    "code" : "",
    "demo" : ""
}
```

4. Stage and commit your changes, then push them to your fork.
```
git add data/datasets.json
git commit -m "adding panning paper from E. Perez Gonzalez and J. D. Reiss"
git push
```

5. Make a pull request with your changes after successfully pushing the changes.

## Acknowledgments
Special thanks to [Brecht De Man](http://www.brechtdeman.com/index.html), [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), and [Ryan Stables](http://www.ryanstables.co.uk) as their publication [Ten Years of Automatic Mixing](http://www.brechtdeman.com/publications/pdf/WIMP3.pdf) served as the foundation for this repository.