
## Contributing
Making contributions to the repo is simple.

First fork the repo and then clone to a local directory. 
```
git clone https://github.com/csteinmetz1/AutomaticMixingPapers.git
```
Then open `mixingpapers.tsv` and add the following attributes on a new line
```
Year	Title	Author	Paper	Resources	Category	Approach
```
Save the file and then run the python script which will update the files.
```
python mixingpapers.py
```
Finally make a pull request with your changes after sucesffully updating the files.

### Some notes
* Ensure when adding entries to `mixingpapers.tsv` that your editor is using tabs not spaces
* `mixingpapers.tsv` will be sorted by year every time you run the python script
* If you encouter any errors with the python script ensure that you have used tabs and not left any trailing tabs or spaces.